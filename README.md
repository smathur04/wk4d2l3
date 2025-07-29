# Lab: Evaluation Metrics for Generative AI Outputs

---

## Table of Contents

* [Scenario / Background](#scenario--background)
* [Objectives](#objectives)
* [Task Overview](#task-overview)
* [Requirements](#requirements)
* [Data Guidance](#data-guidance)
* [Deliverables](#deliverables)
* [Steps & Recommendations](#steps--recommendations)
* [Extension / Stretch Goals](#extension--stretch-goals)
* [References & Resources](#references--resources)

---

### Scenario / Background

When deploying generative models in real applications, it's not enough to eyeball outputs—you need objective measures of quality. Metrics such as **ROUGE** and **BLEU** are widely used to evaluate summarization and translation by comparing machine‑generated text with human references.&#x20;

For classification or other tasks with discrete labels, **accuracy** measures the proportion of correct predictions.&#x20;

In this lab you will build a small evaluation pipeline that computes these metrics for your chosen tasks and compares automatic scores with subjective judgements.

### Objectives

After completing this lab you will be able to:

* **Select appropriate evaluation metrics** for different tasks: ROUGE for summarization, BLEU for translation, accuracy for classification.
* **Prepare evaluation datasets** by selecting suitable open‑source datasets with input texts and reference outputs.
* **Implement automated scoring** using Python libraries (e.g., `rouge_score`, `nltk`) to compute ROUGE, BLEU and accuracy.
* **Compare automated scores to subjective assessment**, discussing how well metrics capture quality and where they fall short.

### Task Overview

You will choose one task among summarization, translation or classification and build an evaluation pipeline. For example, you might evaluate how well a model summarises news articles, translates sentences from another language, or classifies movie reviews as positive or negative. You will:

1. **Select a dataset** with both input texts and reference outputs (summaries, translations or labels).
2. **Run your model** or API to generate outputs for a sample of the dataset.
3. **Compute evaluation metrics** (ROUGE, BLEU or accuracy) for the generated outputs.
4. **Conduct a subjective assessment**, reading a subset of outputs to judge quality by human standards.
5. **Compare findings** from automated metrics and human judgement; discuss strengths and limitations of each metric.

### Requirements

To meet the lab requirements you must:

* Evaluate **at least one generative task** (summarization, translation or classification).
* Use **an open‑source dataset** with clearly defined reference outputs. Datasets must be sourced by you from platforms such as Hugging Face Datasets, Kaggle or data.gov.
* Compute **appropriate metric(s)**: ROUGE‑1, ROUGE‑2 or ROUGE‑L for summarization; BLEU‑n for translation; accuracy (and optionally precision/recall/F1) for classification.
* Perform **subjective evaluation** on a sample of at least five outputs and summarise your impressions (e.g., quality, fluency, factual accuracy).
* **Reflect on metric suitability**: discuss whether the metric aligns with your subjective judgement, and note any issues such as sensitivity to sentence length or class imbalance.
  [Accuracy & More](https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall#:~:text=Accuracy%20is%20a%20metric%20that,the%20total%20number%20of%20predictions)

### Data Guidance

This lab requires you to select your own dataset. When searching for datasets, look for the following characteristics:

* **Input and reference output**: The dataset must include both the input text and the corresponding reference output (summary, translation or label) so you can compute metrics.
* **Size and manageability**: Aim for a dataset with 500--1,000 examples or take a reasonable subset of a larger dataset to keep processing time manageable.
* **Open licence**: Choose datasets that are openly licensed for educational use. Recommended sources include:

  * **Hugging Face Datasets**—the hub hosts many datasets for tasks like summarization, translation and classification.
    [Hugging Face Datasets](https://huggingface.co/docs/hub/en/datasets-overview#:~:text=Datasets%20on%20the%20Hub)
  * **Kaggle**—offers competitions and public datasets; check the metadata for licencing and reference outputs.
  * **data.gov**—the U.S. Government's open data repository with over 300k datasets.
    [data.gov](https://data.gov/#:~:text=The%20Home%20of%20the%20U,Government%27s%20Open%20Data)

### Deliverables

Submit the following:

* A **notebook or script** that loads your chosen dataset, generates model outputs, computes metrics, and displays results. Include code for calculating ROUGE, BLEU or accuracy as appropriate.

### Steps & Recommendations

1. **Select your task and model.** Choose summarization, translation or classification. For summarization or translation, you might use a pre‑trained model from Hugging Face; for classification, choose a dataset with labelled text and a generative model that can output class labels.
2. **Choose a dataset.** Use the Hugging Face Hub search or other data platforms to find a dataset meeting the criteria above. Ensure you have access to both inputs and reference outputs.
3. **Generate outputs.** For each example (or a subset), run the model to produce a summary, translation or label. Save the outputs.
4. **Compute metrics.** Use Python libraries such as `rouge_score` for ROUGE, `nltk.translate` for BLEU, or `sklearn.metrics` for accuracy. ROUGE measures how much of the important content from the reference summary appears in your summary.
5. **Perform subjective evaluation.** Read a sample of outputs and evaluate fluency, informativeness and correctness. Note any differences between your impressions and the metric scores (e.g., high BLEU but poor grammar, or high accuracy but low recall on minority classes).
6. **Analyse and reflect.** Compare metric results with subjective impressions. Discuss how each metric captures or misses aspects of quality. Highlight limitations such as ROUGE's focus on n‑gram overlap rather than coherence, BLEU's sensitivity to phrase variation, or accuracy's vulnerability to class imbalance.

### Extension / Stretch Goals

* **Additional metrics**: Explore F1‑score, precision, recall or METEOR for translation. Compare results across metrics.
* **Human evaluation guidelines:** Develop a simple rubric for human evaluation (e.g., 1--5 scale on fluency and informativeness) and compute correlations with automatic scores.
* **Hyperparameter tuning:** Experiment with different model settings (temperature, max tokens) to see how they affect metrics and human judgement.
* **Visualisation:** Create plots or bar charts to visualise score distributions across your dataset. Investigate whether particular document lengths or topics correlate with lower scores.

### References & Resources

* **ROUGE metric**: Recall‑oriented measure of content overlap used for summarization evaluation.
  [ROUGE Details](https://dev.to/aws-builders/mastering-rouge-matrix-your-guide-to-large-language-model-evaluation-for-summarization-with-examples-jjg#:~:text=ROUGE%20and%20BLEU%20are%20tools,this%20in%20the%20next%20article)
* **BLEU metric**: Evaluates machine translation by comparing candidate translations to references; scores from 0 to 1 indicate closeness.
  [BLEU Details](https://en.wikipedia.org/wiki/BLEU#:~:text=BLEU%20,popular%20automated%20and%20inexpensive%20metrics)
* **Accuracy**: Simple ratio of correct predictions to total predictions; widely used but sensitive to class imbalance.
  [Accuracy Details](https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall#:~:text=Accuracy%20is%20a%20metric%20that,the%20total%20number%20of%20predictions)
* **Hugging Face datasets**, **Kaggle** and **data.gov**: repositories for open datasets.
  [Hugging Face Datasets](https://huggingface.co/docs/hub/en/datasets-overview#:~:text=Datasets%20on%20the%20Hub)
  [data.gov](https://data.gov/#:~:text=The%20Home%20of%20the%20U,Government%27s%20Open%20Data)
