import evaluate
from transformers import pipeline

# --- BLEU ---
def bleu_score(reference_text: str, generated_text: str):
    bleu = evaluate.load("bleu")
    results = bleu.compute(predictions=[generated_text], references=[reference_text])
    return results["bleu"]

# --- Truthfulness (Zero-shot factual check) ---
def truthfulness_score(text: str):
    print("🔎 Checking truthfulness...")
    try:
        classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        result = classifier(
            sequences=text,
            candidate_labels=["truthful", "false", "exaggerated"],
        )
        return {"label": result["labels"][0], "score": round(result["scores"][0], 3)}
    except Exception as e:
        print(f"⚠️ Truthfulness evaluation failed: {e}")
        return {"label": "unknown", "score": 0.0}

# --- Combined Evaluation ---
def evaluate_output_metrics(generated_text: str, reference_text: str = None):
    print("\n🔍 Evaluating quantitative metrics...")
    metrics = {}
    try:
        # BLEU
        if reference_text:
            metrics["BLEU"] = bleu_score(reference_text, generated_text)
        else:
            metrics["BLEU"] = "N/A (no reference provided)"

        # Truthfulness
        metrics["Truthfulness"] = truthfulness_score(generated_text)

        print("\n✅ Metrics:")
        for k, v in metrics.items():
            print(f"{k}: {v}")

        return metrics
    except Exception as e:
        print(f"\n❌ Error during evaluation: {e}")
        return None
