"""Build A's interim mock data in interface v1 format until B's traces arrive.

    python3 a_work/mock/build_mock.py   -> a_work/mock/trace.jsonl, a_work/mock/gold.jsonl

Sources: the 12 SimpleQA pilot questions (one reference at 8 s) and the 18 two-evidence
questions used in the MoshiRAG control experiment (3 s, 8 s). Gold units follow
a_work/unit_schema.md; they are A's own annotation, not B's.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
CTRL = REPO / "a_work/moshirag_control/configs"
PILOT = REPO / "experiments/async_retrieval_latency/configs/samples_hard_pilot.jsonl"
VERSIONS = {"schema_version": "1.0", "data_version": "a-mock-v0"}


def u(uid, desc, necessary, answer, support, deps=()):
    return {"unit_id": uid, "description": desc, "necessary": necessary, "expected_answer": answer,
            "depends_on": list(deps), "support_sets": [list(support)]}


def bridge(first, final, a1, a2):
    return [u("u1", first, False, a1, ["e1"]), u("u2", final, True, a2, ["e2"], ["u1"])]


def comparison(f1, f2, concl, a1, a2, a3):
    return [u("u1", f1, False, a1, ["e1"]), u("u2", f2, False, a2, ["e2"]),
            u("u3", concl, True, a3, [], ["u1", "u2"])]


def bridge_comparison(b1, f1, b2, f2, concl, answers):
    a1, a2, a3, a4, a5 = answers
    return [u("u1", b1, False, a1, ["e1"]), u("u2", f1, False, a2, ["e1"], ["u1"]),
            u("u3", b2, False, a3, ["e2"]), u("u4", f2, False, a4, ["e2"], ["u3"]),
            u("u5", concl, True, a5, [], ["u2", "u4"])]


def multipart(d1, d2, a1, a2):
    return [u("u1", d1, True, a1, ["e1"]), u("u2", d2, True, a2, ["e2"])]


GOLD = {
    "custom_alpha001": ("multipart", multipart("leader of Alpha", "release date of Alpha", "Alice", "June 1")),
    "2wikimultihopqa_062884f40bb011ebab90acde48001122": ("bridge", bridge(
        "father of Caroline Emily Nevill", "father of {u1}",
        "William Nevill, 4th Earl of Abergavenny", "Henry Nevill, 2nd Earl of Abergavenny")),
    "2wikimultihopqa_37a7af5a0bb011ebab90acde48001122": ("bridge", bridge(
        "father of Margaret Fiennes, 11th Baroness Dacre", "father of {u1}",
        "Thomas Fiennes, 9th Baron Dacre", "Sir Thomas Fiennes")),
    "2wikimultihopqa_378759440bdd11eba7f7acde48001122": ("bridge", bridge(
        "director of the film Being Twenty", "birthplace of {u1}", "Fernando Di Leo", "San Ferdinando di Puglia")),
    "2wikimultihopqa_d2f969d40bd911eba7f7acde48001122": ("bridge", bridge(
        "director of A Nightmare on Elm Street 5: The Dream Child", "birthplace of {u1}",
        "Stephen Hopkins", "Jamaica")),
    "hotpotqa_5a852cd05542997b5ce3ffb0": ("bridge", bridge(
        "birthplace of George McCall Theal", "bay that {u1} is a port city of", "Saint John, New Brunswick",
        "Bay of Fundy")),
    "hotpotqa_5ae641f65542992ae0d162a3": ("bridge", bridge(
        "Filipino singer who released the album My Inspiration", "mononym of {u1}", "Jake Zyrus", "Charice")),
    "2wikimultihopqa_39751c8a08d811ebbd9aac1f6bf848b6": ("comparison", comparison(
        "birth date of Mark Gurr", "birth date of William Eythe", "who was born later",
        "February 18, 1966", "April 7, 1918", "Mark Gurr")),
    "2wikimultihopqa_94415cd008e911ebbda7ac1f6bf848b6": ("comparison", comparison(
        "country of Brian Part", "country of John Mosca", "whether they are from the same country",
        "United States", "United States", "yes")),
    "hotpotqa_5a8335d95542993344745ff1": ("comparison", comparison(
        "first Olympics of Piet Norval", "first Olympics of Emilio Sanchez", "who appeared in the Olympics first",
        "1992", "1988", "Emilio Sanchez")),
    "hotpotqa_5adf72d35542992d7e9f9369": ("comparison", comparison(
        "whether William Kronick is a television writer", "whether Jon Turteltaub is a television writer",
        "whether both are television writers", "yes", "no", "no")),
    "hotpotqa_5ae3f4fe5542995ad6573ce8": ("comparison", comparison(
        "family of the genus Gordonia", "family of the genus Osbeckia", "whether they are in the same family",
        "Theaceae", "Melastomataceae", "no")),
    "2wikimultihopqa_36ec2b3a086411ebbd5eac1f6bf848b6": ("bridge_comparison", bridge_comparison(
        "director of The Obsessed of Catule", "death date of {u1}", "director of Countess Ironing-Maid",
        "death date of {u3}", "which film's director died later",
        ("Anselmo Duarte", "November 7, 2009", "Constantin J. David", "February 19, 1964", "The Obsessed of Catule"))),
    "2wikimultihopqa_4f8e349e08e111ebbda2ac1f6bf848b6": ("bridge_comparison", bridge_comparison(
        "director of Hotel Paradis", "death date of {u1}", "director of Devil's Doorway", "death date of {u3}",
        "which film's director died later",
        ("George Schneevoigt", "February 6, 1961", "Anthony Mann", "April 29, 1967", "Devil's Doorway"))),
    "custom_nasa_apollo11": ("multipart", multipart(
        "launch date of Apollo 11", "splashdown date of Apollo 11", "July 16, 1969", "July 24, 1969")),
    "custom_nasa_perseverance": ("multipart", multipart(
        "launch date of Perseverance", "Mars landing date of Perseverance", "July 30, 2020", "February 18, 2021")),
    "custom_nasa_voyager1": ("multipart", multipart(
        "launch date of Voyager 1", "date of Voyager 1's closest approach to Jupiter",
        "September 5, 1977", "March 5, 1979")),
    "custom_nasa_voyager2": ("multipart", multipart(
        "launch date of Voyager 2", "date of Voyager 2's Neptune flyby", "August 20, 1977", "August 25, 1989")),
}


def source_of(event):
    src = event.get("source")
    if isinstance(src, list) and src and isinstance(src[0], list):
        return {"sentences": [{"document_id": d, "sentence_index": i} for d, i in src]}
    if isinstance(src, list):
        return {"document_id": src[0], "sentence_index": src[1]}
    return {"document_id": "unspecified", "sentence_index": None}


def records():
    for line in PILOT.read_text(encoding="utf-8").splitlines():
        r = json.loads(line)
        events = [{"evidence_id": "e1", "visible_time_s": 8.0, "text": r["reference_text"],
                   "source": {"document_id": "simpleqa_reference", "sentence_index": 0}}]
        units = [u("u1", r["question"], True, r["answer"][0], ["e1"])]
        yield r["sample_id"], r["question"], events, "single", units
    for name in ("multihop.json", "multipart_debug.json"):
        for s in json.loads((CTRL / name).read_text(encoding="utf-8")):
            qtype, units = GOLD[s["sample_id"]]
            yield s["sample_id"], s["question"], s["events"], qtype, units


def main():
    traces, golds = [], []
    for sid, question, events, qtype, units in records():
        evs = [{"evidence_id": e["evidence_id"], "scheduled_time_s": e["visible_time_s"],
                "visible_time_s": e["visible_time_s"], "text": e["text"], "source": source_of(e)} for e in events]
        traces.append({**VERSIONS, "sample_id": sid, "trace_id": f"{sid}__mock", "question": question,
                       "time_origin": "question_end", "clock": "simulated", "trace_type": "controlled_mock",
                       "events": evs, "retrieval_complete_time_s": max(e["visible_time_s"] for e in evs)})
        golds.append({**VERSIONS, "sample_id": sid, "question_type": qtype, "units": units})
    for name, rows in (("trace.jsonl", traces), ("gold.jsonl", golds)):
        with open(HERE / name, "w", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"wrote {len(traces)} traces and gold records to {HERE}")


if __name__ == "__main__":
    main()
