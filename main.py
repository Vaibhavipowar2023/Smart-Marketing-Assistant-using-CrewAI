from crew import marketing_crew
from evaluation_matrix import evaluate_output_metrics
import os, re

# disable tracing issues
os.environ["CREWAI_TRACING_ENABLED"] = "false"

if __name__ == "__main__":
    topic = input("Enter your product or campaign focus: ")

    print("\n🤖 Launching Smart Marketing Assistant Crew...\n")
    result = marketing_crew.kickoff(inputs={"topic": topic})

    try:
        output_text = result.raw_output
    except AttributeError:
        output_text = str(result)

    output_text = re.sub(r"<\|.*?\|>", "", output_text).strip()

    print("\n=== Final Campaign Strategy ===\n")
    print(output_text)

    reference_text = None
    if os.path.exists("reference_strategy.txt"):
        with open("reference_strategy.txt", "r", encoding="utf-8") as f:
            reference_text = f.read()

    print("\n📊 Evaluating output quality...\n")
    metrics = evaluate_output_metrics(output_text, reference_text)

    if metrics:
        print("\n✅ Evaluation complete!")
    else:
        print("\n⚠️ Evaluation failed, please check logs.")
