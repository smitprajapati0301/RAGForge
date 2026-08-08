"""
ChromaDB wrapper.

Handles storing and retrieving document embeddings.
"""

import chromadb

from app.core.config import config
from app.preprocessing.chunk import Chunk


class ChromaStore:
    """Wrapper around a ChromaDB collection."""

    def __init__(self):
        self.client = chromadb.PersistentClient(
            path=config["vector_db"]["persist_directory"]
        )

        self.collection = self.client.get_or_create_collection(
            name=config["vector_db"]["collection_name"]
        )
        
    def get_all_chunks(self):
        """Return all stored documents and metadata."""
        return self.collection.get(
            include=["documents", "metadatas"]
        )

    def add_chunks(
        self,
        chunks: list[Chunk],
        embeddings: list[list[float]],
    ):
        """
        Store chunks and their embeddings.
        """

        self.collection.add(
            ids=[chunk.chunk_id for chunk in chunks],
            documents=[chunk.text for chunk in chunks],
            embeddings=embeddings,
            metadatas=[chunk.metadata for chunk in chunks],
        )

    def search(
        self,
        query_embedding: list[float],
        top_k: int,
    ):
        """
        Search the vector database using a query embedding.

        Returns the most semantically similar chunks.
        """

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )

        return results
    
    