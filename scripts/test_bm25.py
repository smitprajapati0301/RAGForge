"""
Test BM25 Retrieval
"""

from app.preprocessing.chunk import Chunk
from app.retrieval.bm25_retriever import BM25Retriever
from app.vectorstore.chroma_store import ChromaStore


def main():

    store = ChromaStore()

    data = store.get_all_chunks()

    chunks = []

    for doc, meta, chunk_id in zip(
        data["documents"],
        data["metadatas"],
        data["ids"],
    ):

        chunks.append(
            Chunk(
                chunk_id=chunk_id,
                text=doc,
                metadata=meta,
            )
        )

    retriever = BM25Retriever(chunks)

    while True:

        query = input("\nQuestion: ")

        if query.lower() == "exit":
            break

        results = retriever.retrieve(query)

        print()

        for rank, (chunk, score) in enumerate(results, start=1):

            print("=" * 80)

            print(f"Rank   : {rank}")
            print(f"Score  : {score:.4f}")
            print(f"Source : {chunk.metadata['filename']}")

            print("\nContent:\n")

            print(chunk.text[:400])

            print()


if __name__ == "__main__":
    main()