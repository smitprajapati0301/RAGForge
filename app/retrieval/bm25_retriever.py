"""
BM25 Retriever

Indexes document chunks using BM25 and performs keyword search.
"""

from rank_bm25 import BM25Okapi

from app.preprocessing.chunk import Chunk
from app.retrieval.tokenizer import Tokenizer


class BM25Retriever:
    """Keyword-based retriever using BM25."""

    def __init__(self, chunks: list[Chunk]):

        self.chunks = chunks

        # Tokenize all chunks once to build the BM25 index.
        tokenized_corpus = [
            Tokenizer.tokenize(chunk.text)
            for chunk in chunks
        ]

        self.bm25 = BM25Okapi(tokenized_corpus)

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[tuple[Chunk, float]]:
        """
        Retrieve the most relevant chunks using BM25.
        """

        query_tokens = Tokenizer.tokenize(query)

        scores = self.bm25.get_scores(query_tokens)

        ranked = sorted(
            zip(self.chunks, scores),
            key=lambda x: x[1],
            reverse=True,
        )

        return ranked[:top_k]