"""
Semantic Retriever

Retrieves chunks using vector similarity search.
"""

from app.core.config import config
from app.embeddings.embedding_service import EmbeddingService
from app.vectorstore.chroma_store import ChromaStore


class Retriever:
    """Semantic retriever using ChromaDB."""

    def __init__(self):

        self.embedding_service = EmbeddingService()
        self.vector_store = ChromaStore()

    def retrieve(
        self,
        query: str,
        top_k: int | None = None,
    ):
        """
        Retrieve the most relevant chunks using semantic search.
        """

        if top_k is None:
            top_k = config["retrieval"]["top_k"]

        # Convert the user's query into a vector.
        query_embedding = self.embedding_service.embed(query)

        # Search the vector database.
        return self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k,
        )

    def retrieve_ids(
        self,
        query: str,
        top_k: int | None = None,
    ) -> list[str]:
        """
        Return only the ranked chunk IDs.

        This format is useful for hybrid retrieval and RRF.
        """

        results = self.retrieve(query, top_k)

        return results["ids"][0]