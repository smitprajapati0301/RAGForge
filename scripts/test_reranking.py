"""
Test the complete retrieval + re-ranking pipeline.
"""

from app.reranking.reranking_pipeline import RerankingPipeline


def main():

    pipeline = RerankingPipeline()

    while True:

        query = input("\nQuestion: ")

        if query.lower() == "exit":
            break

        results = pipeline.retrieve(query)

        print("\nRe-ranked Results\n")

        for rank, result in enumerate(results, start=1):

            chunk = result["chunk"]

            print("=" * 80)

            print(f"Rank          : {rank}")
            print(f"RRF Score     : {result['rrf_score']:.6f}")
            print(
                f"Re-rank Score : "
                f"{result['rerank_score']:.6f}"
            )

            print(
                f"Source        : "
                f"{chunk.metadata.get('filename', 'unknown')}"
            )

            print(
                f"Chunk         : "
                f"{chunk.metadata.get('chunk_index', 'unknown')}"
            )

            print("\nContent:\n")

            print(chunk.text[:500])

            print()


if __name__ == "__main__":
    main()