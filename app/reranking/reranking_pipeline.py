"""
Reranking Pipeline

Combines hybrid retrieval with Cross-Encoder re-ranking.
"""

from app.core.config import config
from app.retrieval.hybrid_retriever import HybridRetriever
from app.reranking.reranker import Reranker


class RerankingPipeline:
    """Hybrid retrieval followed by Cross-Encoder re-ranking."""

    def __init__(self):

        self.hybrid_retriever = HybridRetriever()
        self.reranker = Reranker()

    def retrieve(
        self,
        query: str,
    ) -> list[dict]:
        """
        Retrieve candidate chunks and re-rank them.
        """

        # First retrieve a larger candidate set.
        candidate_k = config["reranking"]["candidate_k"]

        candidates = self.hybrid_retriever.retrieve(
            query=query,
            top_k=candidate_k,
        )

        # Then use the Cross-Encoder to find the most relevant chunks.
        return self.reranker.rerank(
            query=query,
            results=candidates,
            top_k=config["reranking"]["top_k"],
        )