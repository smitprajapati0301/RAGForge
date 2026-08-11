"""
RAGForge FastAPI Application

Provides the HTTP API for the RAGForge platform.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.documents import router as documents_router
from app.api.routes.query import router as query_router


app = FastAPI(
    title="RAGForge",
    description=(
        "Production-Grade Enterprise "
        "Retrieval-Augmented Generation Platform"
    ),
    version="1.0.0",
)


# --------------------------------------------------
# CORS
# --------------------------------------------------
#
# Allows the React frontend running on Vite
# to communicate with the FastAPI backend.
#

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# Routes
# --------------------------------------------------

app.include_router(
    documents_router
)

app.include_router(
    query_router
)


# --------------------------------------------------
# Root endpoint
# --------------------------------------------------

@app.get("/")
async def root():
    return {
        "project": "RAGForge",
        "status": "running",
    }


# --------------------------------------------------
# Health endpoint
# --------------------------------------------------

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "project": "RAGForge",
        "version": "1.0.0",
    }