import json
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock

A_WORK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(A_WORK))

from turntaking.cascade import Heard, PiperTTS, RateTTS, Speech, load_tts  # noqa: E402
from turntaking.generate import Generator  # noqa: E402
from turntaking.judge import OracleJudge  # noqa: E402
from turntaking.llm import CallRecord, ChatClient, FakeClient, TapeMiss, load_tape  # noqa: E402
from turntaking.policies import EvidenceAware, WaitAll  # noqa: E402
from turntaking.replay import replay, units_without_gold  # noqa: E402

TRACE = {"schema_version": "1.0", "data_version": "t", "sample_id": "s", "trace_id": "s_long", "question": "Who and when?",
         "time_origin": "question_end", "clock": "simulated", "trace_type": "controlled_mock",
         "events": [{"evidence_id": "e1", "visible_time_s": 2.0, "text": "Led by Alice.", "source": {"document_id": "Alpha"}},
                    {"evidence_id": "e2", "visible_time_s": 8.0, "text": "Released in 1969.", "source": {"document_id": "Alpha"}}],
         "retrieval_complete_time_s": 8.0}
GOLD = {"sample_id": "s", "units": [
    {"unit_id": "u1", "description": "leader", "necessary": True, "expected_answer": "Alice", "depends_on": [], "support_sets": [["e1"]]},
    {"unit_id": "u2", "description": "release year", "necessary": True, "expected_answer": "1969", "depends_on": [], "support_sets": [["e2"]]}]}


class Client(FakeClient):
    def __init__(self, latency=0.0):
        super().__init__([])
        self.latency = latency

    def chat_json(self, messages, *, purpose, schema=None, max_tokens=None):
        self.messages.append(messages)
        self.calls.append(CallRecord(purpose, self.latency, None, None))
        request = messages[-1]["content"]
        if "Evidence so far" in request:
            return {"text": "It was Alice in 1969.", "answers": ["Alice", "1969"]}
        return {"text": "It is Alice." if "- leader: Alice" in request else "It came out in 1969."}


class SlowTTS:
    """Two seconds per utterance after half a second of synthesis; values are spoken in the second half."""

    def __init__(self):
        self.texts = []

    def synthesize(self, text):
        self.texts.append(text)
        return Speech(2.0, 0.5, lambda i: 1.0 + i / len(text))


def ours(**kw):
    return replay(TRACE, units_without_gold(GOLD), EvidenceAware(OracleJudge([GOLD])), generator=Generator(Client()), **kw)


class SpeechTimingTest(unittest.TestCase):
    def test_rate_tts_is_the_default(self):
        speech = RateTTS().synthesize("one two three four five")
        self.assertEqual((speech.duration_s, speech.latency_s, speech.time_at(0)), (2.0, 0.0, 0.0))
        self.assertEqual(RateTTS().synthesize("Yes.").duration_s, 1.0)
        partial = next(r for r in ours() if r["action"] == "Partial Answer")
        self.assertAlmostEqual(partial["output_end_time_s"] - partial["output_start_time_s"], 1.2)  # "It is Alice."

    def test_tts_latency_delays_speech_and_audio_sets_its_length(self):
        records = ours(tts=SlowTTS())
        partial = next(r for r in records if r["action"] == "Partial Answer")
        self.assertEqual((partial["decision_time_s"], partial["tts_cost_s"], partial["output_start_time_s"],
                          partial["output_end_time_s"]), (2.0, 0.5, 2.5, 4.5))
        claim = partial["claim_spans"][0]
        self.assertEqual(claim["start"], 2.5 + 1.0 + 6 / 12)  # where the TTS says "Alice" is spoken

    def test_fixed_utterances_are_rendered_ahead_of_time(self):
        first = ours(tts=SlowTTS())[0]
        self.assertEqual((first["action"], first["tts_cost_s"], first["output_start_time_s"], first["output_end_time_s"]),
                         ("Backchannel", 0.0, 0.0, 2.0))

    def test_placeholder_replay_needs_no_tts(self):
        tts = SlowTTS()
        replay(TRACE, units_without_gold(GOLD), EvidenceAware(OracleJudge([GOLD])), tts=tts)
        self.assertEqual(tts.texts, [])


class HeardTest(unittest.TestCase):
    def test_models_get_the_question_as_heard(self):
        client = Client()
        replay(TRACE, units_without_gold(GOLD), WaitAll(), generator=Generator(client), heard=Heard("Who and one?", 0.4))
        self.assertIn("Question: Who and one?", client.messages[0][-1]["content"])

    def test_nothing_is_judged_before_the_transcript(self):
        early = dict(TRACE, events=[dict(e, visible_time_s=0.0) for e in TRACE["events"]], retrieval_complete_time_s=0.0)
        policy = EvidenceAware(OracleJudge([GOLD]))
        records = replay(early, units_without_gold(GOLD), policy, generator=Generator(Client()), heard=Heard("q", 1.3))
        self.assertEqual([r["action"] for r in records], ["Backchannel", "Final Answer"])  # hearing a turn end needs no text
        self.assertEqual(records[-1]["decision_time_s"], 1.5)  # first tick after the transcript

    def test_baseline_cannot_answer_before_the_transcript(self):
        early = dict(TRACE, events=[dict(e, visible_time_s=0.0) for e in TRACE["events"]], retrieval_complete_time_s=0.0)
        final = replay(early, units_without_gold(GOLD), WaitAll(), generator=Generator(Client(1.0)), heard=Heard("q", 0.4))[-1]
        self.assertEqual((final["decision_time_s"], final["output_start_time_s"]), (0.4, 1.4))


class PiperTest(unittest.TestCase):
    """PiperTTS against a stand-in voice: one phoneme per letter, and a digit takes five."""

    class Voice:
        config = types.SimpleNamespace(sample_rate=10)

        def phonemize(self, text):
            return [[p for c in text for p in ("#####" if c.isdigit() else c)]]

        def synthesize(self, text):
            for sentence in text.split(". "):
                yield types.SimpleNamespace(audio_int16_bytes=b"\0\0" * 10 * len(sentence.split()))

    def tts(self):
        module = types.SimpleNamespace(PiperVoice=types.SimpleNamespace(load=lambda path: self.Voice()))
        with mock.patch.dict(sys.modules, {"piper": module}):
            return load_tts("piper:voice.onnx")

    def test_duration_is_the_audio_and_numbers_take_longer(self):
        tts = self.tts()
        speech = tts.synthesize("ab 12")
        self.assertEqual((speech.duration_s, speech.sample_rate, len(speech.audio)), (2.0, 10, 40))
        self.assertEqual(speech.time_at(0), 0.0)
        self.assertAlmostEqual(speech.time_at(3), 2.0 * 3 / 13)  # "ab " is 3 of 13 phonemes, not 3 of 5 characters
        self.assertEqual(speech.time_at(5), 2.0)

    def test_repeated_text_is_synthesised_once(self):
        tts = self.tts()
        self.assertIs(tts.synthesize("ab"), tts.synthesize("ab"))
        self.assertEqual(list(tts.spoken), ["ab"])

    def test_unknown_tts_is_refused(self):
        self.assertIsInstance(load_tts(None), RateTTS)
        with self.assertRaises(ValueError):
            load_tts("festival")


class TapeTest(unittest.TestCase):
    def recorded(self):
        """A client that has made one real call, with the network replaced by a canned reply."""
        client = ChatClient("http://x/v1", "m")
        reply = json.dumps({"choices": [{"message": {"content": '{"text": "hi"}'}}], "usage": {}}).encode()
        response = mock.MagicMock()
        response.__enter__.return_value.read.return_value = reply
        with mock.patch("urllib.request.urlopen", return_value=response):
            client.chat_json([{"role": "user", "content": "a"}], purpose="generate")
        return client

    def test_replayed_call_returns_the_reply_and_its_latency(self):
        live = self.recorded()
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "llm_calls.jsonl"
            path.write_text("\n".join(json.dumps(row) for row in live.tape), encoding="utf-8")
            offline = ChatClient("unused", "m", replay=load_tape([path]))
        with mock.patch("urllib.request.urlopen", side_effect=AssertionError("network used")):
            self.assertEqual(offline.chat_json([{"role": "user", "content": "a"}], purpose="generate"), {"text": "hi"})
        self.assertEqual(offline.calls[0].latency_s, live.tape[0]["latency_s"])

    def test_request_missing_from_the_tape_stops_the_run(self):
        offline = ChatClient("unused", "m", replay={row["key"]: row for row in self.recorded().tape})
        with self.assertRaises(TapeMiss):
            offline.chat_json([{"role": "user", "content": "b"}], purpose="generate")
        with self.assertRaises(TapeMiss):  # another model's reply is not this model's
            ChatClient("unused", "other", replay=offline.replay).chat_json([{"role": "user", "content": "a"}], purpose="generate")

    def test_allowed_miss_is_an_unusable_reply_and_is_counted(self):
        offline = ChatClient("unused", "m", replay={}, allow_misses=True)
        text, _ = Generator(offline).grounded("q", [("leader", "Alice")], [], True)
        self.assertEqual((text, offline.misses), ("leader: Alice.", 1))


class RunReplayCascadeTest(unittest.TestCase):
    DECOMP = {"question_type": "single", "units": [{"unit_id": "u1", "description": "answer", "necessary": True, "depends_on": []}]}

    def run_main(self, *extra):
        import run_replay
        asked = []

        class C(FakeClient):
            def __init__(self, *a, **k):
                super().__init__([])

            def chat_json(self, messages, *, purpose, schema=None, max_tokens=None):
                self.calls.append(CallRecord(purpose, 0.1, None, None))
                asked.append(messages[-1]["content"])
                return {"decompose": RunReplayCascadeTest.DECOMP, "judge": {"units": []},
                        "generate": {"text": "Yes.", "answers": ["yes"]}}[purpose]

        with tempfile.TemporaryDirectory() as out, mock.patch.object(run_replay, "ChatClient", C), \
                mock.patch.object(sys, "argv", ["run_replay.py", "--out", out, "--generate", *extra]), mock.patch("builtins.print"):
            run_replay.main()
            rows = [json.loads(l) for l in (Path(out) / "trace_metrics.jsonl").read_text(encoding="utf-8").splitlines()]
            summary = (Path(out) / "summary.md").read_text(encoding="utf-8")
        return rows, summary, asked

    def test_concurrent_adds_copies_of_our_policies_only(self):
        rows, summary, _ = self.run_main("--concurrent")
        policies = {r["policy"] for r in rows}
        self.assertLessEqual({"evidence_aware+oracle", "evidence_aware+oracle+concurrent", "evidence_aware+prompt+concurrent",
                              "evidence_aware+prompt_real", "evidence_aware+prompt_real+concurrent", "wait_all"}, policies)
        self.assertNotIn("wait_all+concurrent", policies)
        self.assertIn("## Paired with Wait-All", summary)

    def test_asr_file_replaces_the_question(self):
        import run_replay
        samples = {t["sample_id"] for t in run_replay.load_jsonl(A_WORK / "mock/trace.jsonl")}
        with tempfile.TemporaryDirectory() as folder:
            asr = Path(folder) / "asr.jsonl"
            asr.write_text("\n".join(json.dumps({"sample_id": s, "text": "What was heard?", "latency_s": 0.3})
                                     for s in samples), encoding="utf-8")
            rows, _, asked = self.run_main("--asr", str(asr))
        self.assertEqual({r["asr_cost_s"] for r in rows}, {0.3})
        self.assertTrue(all("What was heard?" in a for a in asked if a.startswith("Question:")))


if __name__ == "__main__":
    unittest.main()
