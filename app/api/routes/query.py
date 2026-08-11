"""
Query API Routes

Handles user questions and returns
RAGForge generated answers with citations.
"""

from fastapi import (
    APIRouter,
    HTTPException,
)

from app.api.dependencies import rag_service
from app.api.schemas.query import (
    QueryRequest,
    QueryResponse,
)


router = APIRouter(
    prefix="/query",
    tags=["Query"],
)


@router.post(
    "",
    response_model=QueryResponse,
)
def query_rag(
    request: QueryRequest,
):
    """
    Ask a question about indexed documents.

    Runs:

    Hybrid Retrieval
        ↓
    RRF
        ↓
    Re-ranking
        ↓
    Citation Builder
        ↓
    Prompt Builder
        ↓
    Groq LLM
    """

    try:

        result = rag_service.query(
            request.question
        )

        return QueryResponse(
            **result
        )

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error),
        )

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=(
                "RAG query failed: "
                f"{str(error)}"
            ),
        )