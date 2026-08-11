"""
RAGForge API Dependencies

Provides the shared RAG service used by FastAPI routes.

The existing RAGForge components are reused here rather than
duplicating the RAG logic inside individual API routes.
"""

from app.embeddings.embedding_service import EmbeddingService
from app.ingestion.factory import LoaderFactory
from app.preprocessing.chunker import Chunker
from app.vectorstore.chroma_store import ChromaStore

from app.reranking.reranking_pipeline import RerankingPipeline

from app.citations.citation_builder import CitationBuilder

from app.prompts.prompt_builder import PromptBuilder

from app.llm.groq_client import GroqClient


class RAGService:
    """
    Orchestrates the complete RAGForge pipeline.

    Document pipeline:

        Loader
          ↓
        Chunker
          ↓
        Embeddings
          ↓
        Chroma

    Query pipeline:

        Hybrid Retrieval
          ↓
        RRF
          ↓
        Re-ranking
          ↓
        Citations
          ↓
        Prompt
          ↓
        Groq
    """

    def __init__(self):

        # --------------------------------------------------
        # Shared services
        # --------------------------------------------------

        # Chunking service.
        self.chunker = Chunker()

        # Embedding model.
        # Loaded once and reused.
        self.embedding_service = EmbeddingService()

        # Persistent Chroma database.
        self.vector_store = ChromaStore()

        # Groq LLM client.
        self.groq_client = GroqClient()

        # Retrieval pipeline is created when needed.
        #
        # This is important because BM25 builds its corpus
        # from the currently indexed documents.
        self.reranking_pipeline = None

    # ======================================================
    # DOCUMENT INGESTION
    # ======================================================

    def ingest_document(
    self,
    file_path: str,
    original_filename: str | None = None,
    ) -> int:
        """
        Load, chunk, embed and store a document.

        Args:
            file_path: Path to the uploaded document.

        Returns:
            Number of chunks created.
        """

        # --------------------------------------------------
        # 1. Select the appropriate document loader
        # --------------------------------------------------

        loader = LoaderFactory.get_loader(
            file_path
        )

        # --------------------------------------------------
        # 2. Extract text and metadata
        # --------------------------------------------------

        document = loader.load(file_path)

        # Preserve the original filename uploaded by the user.
        # The loader receives a temporary file path, so without
        # this the citation could show a temporary filename.
        if original_filename:
            document.metadata["filename"] = original_filename
        # --------------------------------------------------
        # 3. Split document into chunks
        # --------------------------------------------------

        chunks = self.chunker.split(
            document
        )

        if not chunks:
            raise ValueError(
                "No text could be extracted from the document."
            )

        # --------------------------------------------------
        # 4. Generate embeddings
        # --------------------------------------------------

        texts = [
            chunk.text
            for chunk in chunks
        ]

        embeddings = (
            self.embedding_service.embed_batch(
                texts
            )
        )

        # --------------------------------------------------
        # 5. Store chunks and embeddings in Chroma
        # --------------------------------------------------

        self.vector_store.add_chunks(
            chunks=chunks,
            embeddings=embeddings,
        )

        # --------------------------------------------------
        # 6. Refresh retrieval pipeline
        # --------------------------------------------------
        #
        # HybridRetriever creates its BM25 corpus when
        # it is initialized. Therefore, after adding new
        # documents we recreate it so the new chunks become
        # searchable.
        #

        self.reranking_pipeline = (
            RerankingPipeline()
        )

        return len(chunks)

    # ======================================================
    # QUERY
    # ======================================================

    def query(
        self,
        question: str,
    ) -> dict:
        """
        Run the complete RAGForge query pipeline.

        Args:
            question: User's question.

        Returns:
            Dictionary containing answer and citations.
        """

        # --------------------------------------------------
        # 1. Check whether documents exist
        # --------------------------------------------------

        data = self.vector_store.get_all_chunks()

        if not data.get("ids"):
            raise ValueError(
                "No documents have been indexed yet."
            )

        # --------------------------------------------------
        # 2. Create retrieval pipeline if necessary
        # --------------------------------------------------

        if self.reranking_pipeline is None:

            self.reranking_pipeline = (
                RerankingPipeline()
            )

        # --------------------------------------------------
        # 3. Hybrid retrieval + RRF + re-ranking
        # --------------------------------------------------

        results = (
            self.reranking_pipeline.retrieve(
                query=question
            )
        )

        # --------------------------------------------------
        # 4. Handle no relevant results
        # --------------------------------------------------

        if not results:

            return {
                "question": question,
                "answer": (
                    "I could not find relevant "
                    "information in the indexed "
                    "documents."
                ),
                "sources": [],
            }

        # --------------------------------------------------
        # 5. Build citations
        # --------------------------------------------------

        citations = (
            CitationBuilder.build(
                results
            )
        )

        # --------------------------------------------------
        # 6. Build grounded prompt
        # --------------------------------------------------

        prompt = PromptBuilder.build(
            question=question,
            results=results,
            citations=citations,
        )

        # --------------------------------------------------
        # 7. Generate answer
        # --------------------------------------------------

        answer = self.groq_client.generate(
            prompt
        )

        # --------------------------------------------------
        # 8. Return API response
        # --------------------------------------------------

        return {
            "question": question,
            "answer": answer,
            "sources": citations,
        }


# ==========================================================
# SHARED RAG SERVICE
# ==========================================================
#
# This is the object imported by:
#
#   documents.py
#   query.py
#
# ----------------------------------------------------------

rag_service = RAGService()