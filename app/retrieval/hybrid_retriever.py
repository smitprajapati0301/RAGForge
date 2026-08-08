"""
Hybrid Retriever

Combines semantic retrieval and BM25 keyword retrieval
using Reciprocal Rank Fusion (RRF).
"""

from app.core.config import config
from app.retrieval.bm25_retriever import BM25Retriever
from app.retrieval.rrf import reciprocal_rank_fusion
from app.retrieval.retriever import Retriever
from app.preprocessing.chunk import Chunk
from app.vectorstore.chroma_store import ChromaStore


class HybridRetriever:
    """Combines semantic and BM25 retrieval."""

    def __init__(self):

        self.semantic_retriever = Retriever()

        self.vector_store = ChromaStore()

        # Load all indexed chunks so BM25 can build its corpus.
        data = self.vector_store.get_all_chunks()

        chunks = []

        for document, metadata, chunk_id in zip(
            data["documents"],
            data["metadatas"],
            data["ids"],
        ):

            chunks.append(
                Chunk(
                    chunk_id=chunk_id,
                    text=document,
                    metadata=metadata,
                )
            )

        self.chunks = chunks

        self.bm25_retriever = BM25Retriever(chunks)

    def retrieve(
        self,
        query: str,
        top_k: int | None = None,
    ):
        """
        Perform hybrid retrieval using semantic search,
        BM25, and RRF.
        """

        if top_k is None:
            top_k = config["retrieval"]["top_k"]

        # Get rankings from semantic search.
        semantic_ids = self.semantic_retriever.retrieve_ids(
            query,
            top_k,
        )

        # Get rankings from BM25.
        bm25_ids = self.bm25_retriever.retrieve_ids(
            query,
            top_k,
        )

        # Combine both rankings using RRF.
        fused_results = reciprocal_rank_fusion(
            rankings=[
                semantic_ids,
                bm25_ids,
            ]
        )

        # Keep only the required number of final results.
        fused_results = fused_results[:top_k]

        # Create a lookup table so we can recover the actual chunks.
        chunk_lookup = {
            chunk.chunk_id: chunk
            for chunk in self.chunks
        }

        results = []

        for chunk_id, score in fused_results:

            chunk = chunk_lookup.get(chunk_id)

            if chunk is not None:

                results.append(
                    {
                        "chunk": chunk,
                        "rrf_score": score,
                    }
                )

        return results