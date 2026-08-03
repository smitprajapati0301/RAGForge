import sys
from pathlib import Path


# Add project root to Python path when running this file directly.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.ingestion.factory import LoaderFactory
from app.preprocessing.cleaner import TextCleaner
from app.preprocessing.chunker import Chunker


def main():

    file_path = Path("data/raw/sample.txt")

    loader = LoaderFactory.get_loader(str(file_path))

    document = loader.load(str(file_path))

    cleaned_text = TextCleaner.clean(document.content)

    document.content = cleaned_text

    chunker = Chunker(
        chunk_size=100,
        chunk_overlap=20,
    )

    chunks = chunker.split(document)

    print(f"\nTotal Chunks: {len(chunks)}\n")

    for chunk in chunks:

        print("=" * 80)

        print("Chunk ID:", chunk.chunk_id)

        print("Metadata:", chunk.metadata)

        print("\nText:\n")

        print(chunk.text)

        print()


if __name__ == "__main__":
    main()