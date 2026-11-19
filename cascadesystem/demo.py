"""Fictional integration fixture. No network, credentials, or benchmark data."""
import asyncio


QUESTION = "星舟号什么时候发射，什么时候返回？"


class DemoLLM:
    def __init__(self):
        self.calls = []

    async def complete_feedback(self, purpose, system, payload):
        if purpose == "feedback_verify":
            return {"safe": True}
        chinese = payload["output_language"] == "zh"
        if payload["kind"] == "opening":
            return {"text": "我来查询星舟号的发射和返回时间。" if chinese else "I'll look up the launch and return times.", "status_claim": "intent"}
        return {"text": "我还在处理这次任务的时间信息。" if chinese else "I'm still working on the mission timing question.", "status_claim": "processing"}

    async def complete(self, purpose, system, payload):
        self.calls.append({"purpose": purpose, "status": "fixture", "latency_s": 0.0})
        if purpose == "decompose":
            return {"units": [
                {"unit_id": "u1", "description": "星舟号发射日期", "necessary": True, "depends_on": [], "queries": ["Starboat launch"]},
                {"unit_id": "u2", "description": "星舟号返回日期", "necessary": True, "depends_on": [], "queries": ["Starboat return"]}]}
        if purpose in {"judge", "judge_repair"}:
            rows = []
            for uid, keyword, value in [("u1", "发射", "2040年5月12日"), ("u2", "返回", "2040年5月20日")]:
                source = next((e for e in payload["evidence"] if keyword in e["text"]), None)
                rows.append({"unit_id": uid, "label": "SUPPORTED" if source else "UNRESOLVED", "value": value if source else "",
                             "citations": [source["evidence_id"]] if source else [],
                             "quotes": [{"evidence_id": source["evidence_id"], "text": source["text"]}] if source else []})
            return {"judgments": rows}
        if purpose == "generate":
            return {"text": " ".join(f"{f['description']}是{f['value']}。" for f in payload["APPROVED_FACTS"])}
        if purpose == "verify":
            return {"approved": True, "facts_valid": True,
                    "expressed_unit_ids": payload['output_unit_ids'], "reason": "Fictional fixture"}
        raise ValueError("Unknown demo purpose")


class DemoSearch:
    async def search(self, query):
        launch = "launch" in query
        await asyncio.sleep(0.05 if launch else 0.25)
        return [{"title": "虚构星舟号任务", "url": "https://example.invalid/starboat/" + ("launch" if launch else "return"),
                 "text": "星舟号于2040年5月12日发射。" if launch else "星舟号于2040年5月20日返回。"}]
