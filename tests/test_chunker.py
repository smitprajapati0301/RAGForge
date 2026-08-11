"""
Tests for the RAGForge chunking pipeline.
"""

from app.ingestion.document import Document
from app.preprocessing.chunker import Chunker


def test_chunker_creates_chunks():
    """
    Verify that a document is split into chunks.
    """

    text = (
        "RAGForge is a production-oriented "
        "retrieval augmented generation system. "
        * 100
    )

    document = Document(
        content=text,
        metadata={
            "filename": "test.txt",
            "filetype": "txt",
        },
    )

    chunker = Chunker()

    chunks = chunker.split(document)

    assert len(chunks) > 0


def test_chunk_metadata():
    """
    Verify that chunk metadata is created correctly.
    """

    document = Document(
        content="This is a test document. " * 100,
        metadata={
            "filename": "test.txt",
            "filetype": "txt",
        },
    )

    chunker = Chunker()

    chunks = chunker.split(document)

    assert len(chunks) > 0

    first_chunk = chunks[0]

    assert first_chunk.document_id == document.document_id
    assert first_chunk.metadata["chunk_index"] == 0
    assert "chunk_count" in first_chunk.metadata