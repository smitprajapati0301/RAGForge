from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.ingestion.document import Document
from app.preprocessing.chunk import Chunk


class Chunker:

    def __init__(
        self,
        chunk_size: int = 700,
        chunk_overlap: int = 100,
    ):

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
        )

    def split(self, document: Document):

        texts = self.text_splitter.split_text(document.content)

        chunks = []

        for index, text in enumerate(texts):

            metadata = document.metadata.copy()

            metadata.update(
                {
                    "chunk_index": index,
                    "chunk_count": len(texts),
                }
            )

            chunks.append(
                Chunk(
                    text=text,
                    metadata=metadata,
                )
            )

        return chunks