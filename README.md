# Lab: Evaluation Metrics for Generative AI Outputs

## Scenario

This lab evaluates the quality of generated summaries. The repository includes a
small original dataset in `data/summarization_samples.json`, so students can focus
on evaluation instead of downloading and cleaning a large dataset.

Each record contains a project update and a concise human-written reference summary.
The example solution asks a model to summarize the first five records, calculates
ROUGE scores, and prints the outputs for human review.

## Learning objectives

- Use a reference dataset to evaluate generated text.
- Calculate ROUGE-1, ROUGE-2, and ROUGE-L.
- Compare automatic scores with human judgments.
- Explain why overlap metrics do not fully measure quality.

## Student task

1. Load the included JSON dataset.
2. Generate a summary for each selected project update.
3. Calculate ROUGE scores against the reference summary.
4. Review at least five outputs for fluency, coverage, and factual accuracy.
5. Reflect on whether the scores agree with your human assessment.

The included dataset is synthetic and created for this educational exercise. You may
replace it with an openly licensed dataset, but document its source and license.

## Metrics

Use ROUGE-1, ROUGE-2, and ROUGE-L. ROUGE measures token overlap with the reference;
a higher score does not automatically mean that a summary is more useful or factual.

## Running the example solution

Install the dependencies:

```bash
pip install openai rouge-score
```

Set a Gemini API key without placing it in the repository:

```bash
export GEMINI_API_KEY="your-key"
python3 SOLUTION_evaluation.py
```

The model name and sample size are hardcoded at the top of the solution file. The
solution makes five model calls, so it is suitable for a small free-tier test.

## Human review

For each output, record a short judgment for:

- Fluency: Is it clear and readable?
- Coverage: Does it include the important facts?
- Factual accuracy: Does it add, remove, or distort information?

Compare those judgments with the ROUGE values in a table such as:

| Example | ROUGE-1 | ROUGE-2 | ROUGE-L | Fluency | Coverage | Accuracy |
|---|---:|---:|---:|---|---|---|
| 1 |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |

## Reflection questions

- Did the highest-scoring summaries also seem best to you?
- Did a summary with different wording receive a low overlap score?
- Did any summary omit or invent an important fact?
- What would you change in the prompt or evaluation process?

## Optional extensions

- Evaluate all ten records instead of the default five.
- Add a second reference summary for selected records.
- Compare ROUGE with a simple human score.
- Try BLEU or classification accuracy with a separate dataset.
