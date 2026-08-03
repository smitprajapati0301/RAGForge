from fastapi import FastAPI

app = FastAPI(
    title="RAGForge",
    description="Production-Grade Enterprise RAG Platform",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {
        "project": "RAGForge",
        "status": "running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "project": "RAGForge",
        "version": "1.0.0"
    }