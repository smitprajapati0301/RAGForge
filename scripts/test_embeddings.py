from pathlib import Path

from app.ingestion.factory import LoaderFactory
from app.preprocessing.cleaner import TextCleaner
from app.preprocessing.chunker import Chunker
from app.embeddings.embedding_service import EmbeddingService
from app.vectorstore.chroma_store import ChromaStore


def main():

    file_path = Path("data/raw/sample.txt")

    loader = LoaderFactory.get_loader(str(file_path))
    document = loader.load(str(file_path))

    document.content = TextCleaner.clean(document.content)

    chunker = Chunker()

    chunks = chunker.split(document)

    embedding_service = EmbeddingService()

    embeddings = embedding_service.embed_batch(
        [chunk.text for chunk in chunks]
    )

    chroma = ChromaStore()

    chroma.add_chunks(
        chunks,
        embeddings,
    )

    print(f"Stored {len(chunks)} chunks in ChromaDB.")

    print(f"Embedding Dimension: {len(embeddings[0])}")


if __name__ == "__main__":
    main()