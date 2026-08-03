import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).parent.parent))

from app.ingestion.factory import LoaderFactory


RAW_DATA = Path("data/raw")


def main():

    files = list(RAW_DATA.iterdir())

    for file in files:

        if file.is_dir():
            continue

        print("=" * 60)

        print(f"Loading: {file.name}")

        loader = LoaderFactory.get_loader(str(file))

        document = loader.load(str(file))

        print("Metadata:")

        print(document.metadata)

        print()

        print("Characters:", len(document.content))

        print()

        print("Preview:")

        print(document.content[:500])

        print()


if __name__ == "__main__":
    main()