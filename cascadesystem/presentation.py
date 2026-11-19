"""Bilingual output and conservative sentence boundaries, without extra dependencies."""
import re


def detect_language(question, preferred="auto"):
    if preferred in {"zh", "en"}:
        return preferred
    if preferred != "auto":
        raise ValueError("Language must be auto, zh, or en")
    english_question = re.match(r"\s*(?:who|what|where|when|why|how|which|is|are|was|were|does|do|did|can|could|please|tell)\b", question, re.I)
    if english_question:
        return "en"
    return "zh" if re.search(r"[\u3400-\u9fff]", question) else "en"


def matches_language(text, language):
    """Coarse script check, allowing Latin proper names inside Chinese sentences."""
    has_han = bool(re.search(r"[\u3400-\u9fff]", text))
    return has_han if language == "zh" else not has_han


def finish_sentence(text, language):
    text = text.strip()
    if text and text[-1] not in ".!?。！？…\"'”’」』":
        text += "。" if language == "zh" else "."
    return text


def split_sentences(text):
    """Keep decimals, initials, abbreviations, and closing quotation marks intact."""
    abbreviations = {"mr", "mrs", "ms", "dr", "prof", "sr", "jr", "st", "vs", "etc", "e.g", "i.e", "a.m", "p.m"}
    closers = '\"\'”’」』)]}'
    sentences, start, index = [], 0, 0
    while index < len(text):
        char = text[index]
        boundary = char in "。！？!?"
        if char == ".":
            token = re.search(r"([A-Za-z.]+)\.$", text[:index + 1])
            word = token.group(1) if token else ""
            decimal = index > 0 and index + 1 < len(text) and text[index - 1].isdigit() and text[index + 1].isdigit()
            abbreviated = word.lower() in abbreviations or len(word) == 1 or bool(re.fullmatch(r"(?:[A-Za-z]\.){2,}", word + "."))
            boundary = not decimal and not abbreviated and (index + 1 == len(text) or text[index + 1].isspace() or text[index + 1] in closers)
        if boundary:
            end = index + 1
            while end < len(text) and text[end] in "。！？!?" + closers:
                end += 1
            sentence = text[start:end].strip()
            if sentence:
                sentences.append(sentence)
            start = index = end
        else:
            index += 1
    if text[start:].strip():
        sentences.append(text[start:].strip())
    return sentences


def sentence_events(event):
    sentences = split_sentences(event["text"])
    return [{**event, "text": text, "sentence_index": index + 1, "sentence_count": len(sentences)}
            for index, text in enumerate(sentences)]


def ready_line(event):
    if event.get("language") == "zh":
        action = {"Backchannel": "确认", "Progress": "进度", "Partial Answer": "部分回答",
                  "Final Answer": "最终回答", "Correction": "更正"}.get(event["action"], event["action"])
        if event.get("feedback_source"):
            action += "·动态" if event["feedback_source"] == "model" else "·兜底"
        return f"[文本就绪 {event['time_s']:.2f}秒 | {action} | {event['sentence_index']}/{event['sentence_count']}] {event['text']}"
    action = event["action"]
    if event.get("feedback_source"):
        action += " (dynamic)" if event["feedback_source"] == "model" else " (fallback)"
    return f"[Ready {event['time_s']:.2f}s | {action} | {event['sentence_index']}/{event['sentence_count']}] {event['text']}"
