"""
Chunker

Splits cleaned document text into smaller chunks that are ready
for embedding and retrieval.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.config import config
from app.ingestion.document import Document
from app.preprocessing.chunk import Chunk


class Chunker:
    """Splits a document into overlapping chunks."""

    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config["preprocessing"]["chunk_size"],
            chunk_overlap=config["preprocessing"]["chunk_overlap"],
            length_function=len,
        )

    def split(self, document: Document) -> list[Chunk]:
        """
        Split a document into chunks.

        Args:
            document: Document object.

        Returns:
            List of Chunk objects.
        """

        texts = self.text_splitter.split_text(document.content)

        chunks = []

        for index, text in enumerate(texts):

            # Copy document metadata so every chunk keeps
            # information about its original source.
            metadata = document.metadata.copy()

            metadata.update(
                {
                    "chunk_index": index,
                    "chunk_count": len(texts),
                }
            )

            chunks.append(
                Chunk(
                    document_id=document.document_id,
                    text=text,
                    metadata=metadata,
                )
            )

        return chunks