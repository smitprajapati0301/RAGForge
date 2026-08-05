"""
Semantic Retriever

Converts a user query into an embedding and
retrieves the most relevant chunks from ChromaDB.
"""

from app.core.config import config
from app.embeddings.embedding_service import EmbeddingService
from app.vectorstore.chroma_store import ChromaStore


class Retriever:
    """Semantic retriever using ChromaDB."""

    def __init__(self):

        self.embedding_service = EmbeddingService()
        self.vector_store = ChromaStore()

    def retrieve(self, query: str):
        """
        Retrieve the Top-K most relevant chunks.

        Args:
            query: User question.

        Returns:
            ChromaDB search results.
        """

        # Convert the user query into an embedding
        query_embedding = self.embedding_service.embed(query)

        # Search ChromaDB
        results = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=config["retrieval"]["top_k"],
        )

        return results