"""
RAGForge Evaluation

Evaluates the complete RAG pipeline using Ragas 0.4.3.

Metrics:
- Faithfulness
- Answer Relevancy
- Context Precision
- Context Recall

Ragas 0.4 collections metrics are evaluated directly
using .ascore() instead of the older evaluate() API.
"""

import asyncio
import json
from datetime import datetime
from pathlib import Path

from ragas.metrics.collections import (
    Faithfulness,
    AnswerRelevancy,
    ContextPrecision,
    ContextRecall,
)

from app.core.config import config
from app.evaluation.rag_evaluator import RAGEvaluator
from app.evaluation.ragas_llm import create_ragas_llm
from app.evaluation.ragas_embeddings import (
    create_ragas_embeddings,
)


async def evaluate_record(
    record: dict,
    metrics: dict,
) -> dict:
    """
    Evaluate one RAGForge response using all metrics.

    Each Ragas 0.4 collection metric receives the
    individual fields it needs.
    """

    question = record["question"]
    answer = record["answer"]
    contexts = record["contexts"]
    ground_truth = record["ground_truth"]

    scores = {}

    # --------------------------------------------------
    # 1. Faithfulness
    # --------------------------------------------------
    #
    # Measures whether the generated answer is supported
    # by the retrieved context.
    #

    faithfulness_result = await metrics[
        "faithfulness"
    ].ascore(
        user_input=question,
        response=answer,
        retrieved_contexts=contexts,
    )

    scores["faithfulness"] = float(
        faithfulness_result.value
    )

    # --------------------------------------------------
    # 2. Answer Relevancy
    # --------------------------------------------------
    #
    # Measures whether the generated answer actually
    # addresses the user's question.
    #

    relevancy_result = await metrics[
        "answer_relevancy"
    ].ascore(
        user_input=question,
        response=answer,
    )

    scores["answer_relevancy"] = float(
        relevancy_result.value
    )

    # --------------------------------------------------
    # 3. Context Precision
    # --------------------------------------------------
    #
    # Measures whether relevant retrieved chunks
    # appear higher in the ranking.
    #
    # A reference answer is required by this metric.
    #

    precision_result = await metrics[
        "context_precision"
    ].ascore(
        user_input=question,
        reference=ground_truth,
        retrieved_contexts=contexts,
    )

    scores["context_precision"] = float(
        precision_result.value
    )

    # --------------------------------------------------
    # 4. Context Recall
    # --------------------------------------------------
    #
    # Measures whether the retrieved context contains
    # the information required by the reference answer.
    #

    recall_result = await metrics[
        "context_recall"
    ].ascore(
        user_input=question,
        reference=ground_truth,
        retrieved_contexts=contexts,
    )

    scores["context_recall"] = float(
        recall_result.value
    )

    return {
        "question": question,
        "ground_truth": ground_truth,
        "answer": answer,
        "scores": scores,
    }


async def main():
    """Run the complete RAGForge evaluation."""

    print("\n" + "=" * 70)
    print("RAGForge Evaluation")
    print("=" * 70)

    # --------------------------------------------------
    # 1. Run RAGForge against evaluation dataset
    # --------------------------------------------------

    print(
        "\nRunning RAGForge on evaluation questions...\n"
    )

    evaluator = RAGEvaluator()

    records = evaluator.run()

    if not records:

        print(
            "No evaluation records were generated."
        )

        return

    print(
        f"\nGenerated {len(records)} evaluation records."
    )

    # --------------------------------------------------
    # 2. Load Ragas evaluator LLM
    # --------------------------------------------------

    print(
        "\nLoading Ragas evaluator LLM..."
    )

    evaluator_llm = create_ragas_llm()

    print(
        "Ragas evaluator LLM loaded."
    )

    # --------------------------------------------------
    # 3. Load Ragas embedding model
    # --------------------------------------------------

    print(
        "\nLoading Ragas embedding model..."
    )

    evaluator_embeddings = (
        create_ragas_embeddings()
    )

    print(
        "Ragas embedding model loaded."
    )

    # --------------------------------------------------
    # 4. Initialize Ragas metrics
    # --------------------------------------------------

    metrics = {
        "faithfulness": Faithfulness(
            llm=evaluator_llm
        ),

        "answer_relevancy": AnswerRelevancy(
            llm=evaluator_llm,
            embeddings=evaluator_embeddings,
        ),

        "context_precision": ContextPrecision(
            llm=evaluator_llm
        ),

        "context_recall": ContextRecall(
            llm=evaluator_llm
        ),
    }

    print("\nMetrics configured:")
    print("  - Faithfulness")
    print("  - Answer Relevancy")
    print("  - Context Precision")
    print("  - Context Recall")

    # --------------------------------------------------
    # 5. Evaluate every record
    # --------------------------------------------------

    evaluation_results = []

    total = len(records)

    print(
        "\n" + "=" * 70
    )

    print(
        "Running metric evaluation..."
    )

    print(
        "=" * 70
    )

    for index, record in enumerate(
        records,
        start=1,
    ):

        print(
            f"\nEvaluating sample "
            f"{index}/{total}"
        )

        try:

            result = await evaluate_record(
                record,
                metrics,
            )

            evaluation_results.append(
                result
            )

            scores = result["scores"]

            print(
                f"  Faithfulness       : "
                f"{scores['faithfulness']:.4f}"
            )

            print(
                f"  Answer Relevancy   : "
                f"{scores['answer_relevancy']:.4f}"
            )

            print(
                f"  Context Precision  : "
                f"{scores['context_precision']:.4f}"
            )

            print(
                f"  Context Recall     : "
                f"{scores['context_recall']:.4f}"
            )

        except Exception as error:

            print(
                f"  ERROR: {error}"
            )

            # Continue evaluating other questions
            # instead of stopping the entire evaluation.
            continue

    # --------------------------------------------------
    # 6. Make sure we received results
    # --------------------------------------------------

    if not evaluation_results:

        print(
            "\nNo evaluation results were generated."
        )

        return

    # --------------------------------------------------
    # 7. Calculate average scores
    # --------------------------------------------------

    metric_names = [
        "faithfulness",
        "answer_relevancy",
        "context_precision",
        "context_recall",
    ]

    averages = {}

    for metric_name in metric_names:

        values = [
            result["scores"][metric_name]
            for result in evaluation_results
            if metric_name in result["scores"]
        ]

        if values:

            averages[metric_name] = (
                sum(values) / len(values)
            )

    # --------------------------------------------------
    # 8. Display final results
    # --------------------------------------------------

    print(
        "\n" + "=" * 70
    )

    print(
        "RAGForge Evaluation Results"
    )

    print(
        "=" * 70
    )

    for metric_name, score in averages.items():

        print(
            f"{metric_name:<25}: "
            f"{score:.4f}"
        )

    print(
        "=" * 70
    )

    # --------------------------------------------------
    # 9. Prepare output
    # --------------------------------------------------

    output = {
        "project": config["project"]["name"],
        "evaluation_timestamp": (
            datetime.now().isoformat()
        ),
        "dataset_size": len(records),
        "successful_evaluations": len(
            evaluation_results
        ),
        "average_scores": averages,
        "individual_results": evaluation_results,
    }

    # --------------------------------------------------
    # 10. Create results directory
    # --------------------------------------------------

    results_dir = Path(
        config["evaluation"]["results_path"]
    )

    results_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    # --------------------------------------------------
    # 11. Create timestamped result file
    # --------------------------------------------------

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    result_path = (
        results_dir
        / f"evaluation_{timestamp}.json"
    )

    # --------------------------------------------------
    # 12. Save results
    # --------------------------------------------------

    with open(
        result_path,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            output,
            file,
            indent=2,
        )

    print(
        f"\nEvaluation results saved to:"
    )

    print(
        result_path
    )


if __name__ == "__main__":

    asyncio.run(main())