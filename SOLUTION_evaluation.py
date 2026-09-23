import json
import os
from openai import OpenAI
from rouge_score import rouge_scorer

MODEL = "gemini-3.5-flash-lite"
SAMPLE_SIZE = 5

api_key = ""
client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

with open("data/summarization_samples.json") as f:
    data = json.load(f)

samples = data[:SAMPLE_SIZE]

scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)

print(f"{'Ex':<5} {'ROUGE-1':>8} {'ROUGE-2':>8} {'ROUGE-L':>8}")
print("-" * 35)

for item in samples:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": f"Summarize the following project update in one sentence:\n\n{item['text']}"}
        ]
    )
    generated = response.choices[0].message.content.strip()
    reference = item["reference_summary"]

    scores = scorer.score(reference, generated)
    r1 = scores["rouge1"].fmeasure
    r2 = scores["rouge2"].fmeasure
    rl = scores["rougeL"].fmeasure

    print(f"\nExample {item['id']}")
    print(f"  Original : {item['text']}")
    print(f"  Reference: {reference}")
    print(f"  Generated: {generated}")
    print(f"  ROUGE-1={r1:.3f}  ROUGE-2={r2:.3f}  ROUGE-L={rl:.3f}")
