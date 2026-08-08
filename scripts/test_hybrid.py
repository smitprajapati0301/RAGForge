"""
Test Hybrid Retrieval
"""

from app.retrieval.hybrid_retriever import HybridRetriever


def main():

    retriever = HybridRetriever()

    while True:

        query = input("\nQuestion: ")

        if query.lower() == "exit":
            break

        results = retriever.retrieve(query)

        print("\nHybrid Retrieval Results\n")

        for rank, result in enumerate(
            results,
            start=1,
        ):

            chunk = result["chunk"]
            score = result["rrf_score"]

            print("=" * 80)

            print(f"Rank      : {rank}")
            print(f"RRF Score : {score:.6f}")
            print(
                f"Source    : "
                f"{chunk.metadata.get('filename', 'unknown')}"
            )
            print(
                f"Chunk     : "
                f"{chunk.metadata.get('chunk_index', 'unknown')}"
            )

            print("\nContent:\n")

            print(chunk.text[:500])

            print()


if __name__ == "__main__":
    main()