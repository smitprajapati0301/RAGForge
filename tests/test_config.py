"""
Tests for RAGForge configuration.
"""

from app.core.config import config


def test_project_configuration():
    """
    Verify that the main project configuration exists.
    """

    assert "project" in config
    assert config["project"]["name"] == "RAGForge"


def test_embedding_configuration():
    """
    Verify that the embedding configuration exists.
    """

    assert "embedding" in config
    assert "model_name" in config["embedding"]


def test_retrieval_configuration():
    """
    Verify that retrieval configuration exists.
    """

    assert "retrieval" in config
    assert "top_k" in config["retrieval"]


def test_reranking_configuration():
    """
    Verify that re-ranking configuration exists.
    """

    assert "reranking" in config
    assert "model_name" in config["reranking"]


def test_evaluation_configuration():
    """
    Verify that evaluation configuration exists.
    """

    assert "evaluation" in config
    assert config["evaluation"]["enabled"] is True