"""
RAGForge Evaluation Quality Gate

Checks whether RAGForge evaluation scores
meet the minimum quality thresholds.

This script can be executed by GitHub Actions.

If any metric falls below its threshold,
the script exits with a non-zero status code.
"""

import json
import sys
from pathlib import Path

from app.core.config import config


# --------------------------------------------------
# Minimum acceptable evaluation scores
# --------------------------------------------------

THRESHOLDS = {
    "faithfulness": 0.30,
    "answer_relevancy": 0.30,
    "context_precision": 0.35,
    "context_recall": 0.35,
}


def get_latest_result():
    """
    Find the most recent evaluation result.
    """

    results_dir = Path(
        config["evaluation"]["results_path"]
    )

    result_files = sorted(
        results_dir.glob("evaluation_*.json"),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )

    if not result_files:
        raise FileNotFoundError(
            "No evaluation result files found."
        )

    return result_files[0]


def main():
    """
    Check evaluation scores against thresholds.
    """

    print("=" * 70)
    print("RAGForge Evaluation Quality Gate")
    print("=" * 70)

    try:

        result_file = get_latest_result()

        print(
            f"\nUsing result:\n{result_file}"
        )

        with open(
            result_file,
            "r",
            encoding="utf-8",
        ) as file:

            results = json.load(file)

    except Exception as error:

        print(
            f"\nFailed to load evaluation results: "
            f"{error}"
        )

        sys.exit(1)

    scores = results.get(
        "average_scores",
        {},
    )

    failed = False

    print("\nMetric Results:")
    print("-" * 70)

    for metric, threshold in THRESHOLDS.items():

        score = scores.get(metric)

        if score is None:

            print(
                f"{metric:<25} "
                f"NOT FOUND"
            )

            failed = True

            continue

        status = (
            "PASS"
            if score >= threshold
            else "FAIL"
        )

        print(
            f"{metric:<25} "
            f"{score:.4f} "
            f"(minimum: {threshold:.2f}) "
            f"{status}"
        )

        if score < threshold:
            failed = True

    print("-" * 70)

    if failed:

        print(
            "\n❌ Evaluation quality gate FAILED."
        )

        print(
            "One or more metrics are below "
            "the required threshold."
        )

        sys.exit(1)

    print(
        "\n✅ Evaluation quality gate PASSED."
    )


if __name__ == "__main__":
    main()