"""
Embedding Service

Generates dense vector embeddings for text using a SentenceTransformer model.
"""

from sentence_transformers import SentenceTransformer

from app.core.config import config


class EmbeddingService:
    """Service for generating text embeddings."""

    def __init__(self):
        model_name = config["embedding"]["model_name"]

        # Load the embedding model once and reuse it.
        self.model = SentenceTransformer(model_name)

    def embed(self, text: str) -> list[float]:
        """
        Generate an embedding for a single text.
        """

        return self.model.encode(
            text,
            normalize_embeddings=config["embedding"]["normalize_embeddings"],
        ).tolist()

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """
        Generate embeddings for multiple texts.

        Batch embedding is significantly faster than embedding
        one text at a time.
        """

        return self.model.encode(
            texts,
            normalize_embeddings=config["embedding"]["normalize_embeddings"],
        ).tolist()