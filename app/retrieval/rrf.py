"""
Reciprocal Rank Fusion (RRF)
"""

from app.core.config import config


def reciprocal_rank_fusion(
    rankings: list[list[str]],
    k: int | None = None,
) -> list[tuple[str, float]]:
    """
    Combine multiple ranked lists using RRF.
    """

    if k is None:
        k = config["retrieval"]["hybrid"]["rrf_k"]

    scores = {}

    for ranking in rankings:

        for rank, document_id in enumerate(
            ranking,
            start=1,
        ):

            # RRF gives higher scores to higher-ranked results.
            score = 1 / (k + rank)

            scores[document_id] = (
                scores.get(document_id, 0) + score
            )

    return sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True,
    )