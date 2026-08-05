"""
Test Semantic Retrieval
"""

from app.retrieval.retriever import Retriever


def main():

    retriever = Retriever()

    while True:

        print("\nType 'exit' to quit.\n")

        query = input("Question: ")

        if query.lower() == "exit":
            break

        results = retriever.retrieve(query)

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        print("\nTop Results\n")

        for i, (doc, meta, distance) in enumerate(
            zip(documents, metadatas, distances),
            start=1,
        ):

            print("=" * 80)

            print(f"Rank      : {i}")
            print(f"Distance  : {distance:.4f}")
            print(f"Source    : {meta['filename']}")
            print(f"Chunk     : {meta['chunk_index']}")

            print("\nContent:\n")

            print(doc[:500])

            print()


if __name__ == "__main__":
    main()