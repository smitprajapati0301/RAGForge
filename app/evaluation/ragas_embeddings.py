"""
Ragas Embedding Configuration

Creates the embedding model used by Ragas
for embedding-based evaluation metrics.
"""

from ragas.embeddings import HuggingFaceEmbeddings

from app.core.config import config


def create_ragas_embeddings():
    """
    Create the embedding model used by Ragas.

    RAGForge already uses BAAI/bge-base-en-v1.5
    for document embeddings, so we reuse the same
    model for evaluation.
    """

    return HuggingFaceEmbeddings(
        model=config["embedding"]["model_name"],
        normalize_embeddings=config["embedding"][
            "normalize_embeddings"
        ],
        batch_size=config["embedding"]["batch_size"],
    )