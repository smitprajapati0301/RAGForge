"""
Query API Schemas

Defines request and response models for
RAGForge question answering.
"""

from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    """User question sent to the RAG pipeline."""

    question: str = Field(
        ...,
        min_length=1,
        description="Question to ask about indexed documents.",
    )


class Source(BaseModel):
    """Citation information for a retrieved source."""

    id: int
    filename: str
    page: int | None = None
    chunk_index: int | None = None


class QueryResponse(BaseModel):
    """Final response returned by RAGForge."""

    question: str
    answer: str
    sources: list[Source]