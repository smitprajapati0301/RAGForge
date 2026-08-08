"""
Cross-Encoder Re-ranker

Takes candidate chunks retrieved by the hybrid retriever
and re-ranks them according to query-document relevance.
"""

from sentence_transformers import CrossEncoder

from app.core.config import config


class Reranker:
    """Re-ranks retrieved chunks using a Cross-Encoder."""

    def __init__(self):
        # Load the model once and reuse it for all queries.
        model_name = config["reranking"]["model_name"]

        self.model = CrossEncoder(model_name)

    def rerank(
        self,
        query: str,
        results: list[dict],
        top_k: int | None = None,
    ) -> list[dict]:
        """
        Re-rank retrieved chunks based on query relevance.

        Args:
            query: Original user query.
            results: Candidate results from hybrid retrieval.
            top_k: Number of final results to return.

        Returns:
            Re-ranked results with relevance scores.
        """

        if not results:
            return []

        if top_k is None:
            top_k = config["reranking"]["top_k"]

        # Create query-document pairs for the Cross-Encoder.
        pairs = [
            (query, result["chunk"].text)
            for result in results
        ]

        # Score how relevant each chunk is to the query.
        scores = self.model.predict(pairs)

        reranked_results = []

        for result, score in zip(results, scores):

            reranked_results.append(
                {
                    "chunk": result["chunk"],
                    "rrf_score": result["rrf_score"],
                    "rerank_score": float(score),
                }
            )

        # Sort by Cross-Encoder relevance score.
        reranked_results.sort(
            key=lambda item: item["rerank_score"],
            reverse=True,
        )

        return reranked_results[:top_k]