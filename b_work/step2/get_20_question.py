import json

path = "prepared/samples_debug.jsonl"

with open(path, "r", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        record = json.loads(line)

        print("\nQuestion", number)
        print("ID:", record["sample_id"])
        print("Question:", record["question"])
        print("Answer:", record["answer"])

        paragraphs = {}
        for title, sentences in record["context"]:
            paragraphs[title] = sentences

        print("Supporting sentences:")
        for title, index in record["supporting_facts"]:
            print("-", title, ":", paragraphs[title][index])