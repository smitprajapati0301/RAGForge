"""
End-to-end RAG test.

Pipeline:

Query
→ Hybrid Retrieval
→ RRF
→ Cross-Encoder Re-ranking
→ Citation Generation
→ Prompt Builder
→ LLM
"""

from app.citations.citation_builder import CitationBuilder
from app.llm.groq_client import GroqClient
from app.prompts.prompt_builder import PromptBuilder
from app.reranking.reranking_pipeline import RerankingPipeline


def main():

    pipeline = RerankingPipeline()
    llm = GroqClient()

    while True:

        question = input("\nQuestion: ")

        if question.lower() == "exit":
            break

        # Retrieve and re-rank the most relevant chunks.
        results = pipeline.retrieve(question)

        if not results:

            print(
                "\nI couldn't find relevant information "
                "in the provided documents."
            )

            continue

        # Generate citations from actual chunk metadata.
        citations = CitationBuilder.build(results)

        # Build a grounded prompt.
        prompt = PromptBuilder.build(
            question=question,
            results=results,
            citations=citations,
        )

        # Generate the final answer.
        answer = llm.generate(prompt)

        print("\n" + "=" * 80)

        print("\nAnswer:\n")

        print(answer)

        print("\nSources:\n")

        for citation in citations:

            if citation.get("page") is not None:

                print(
                    f"[{citation['id']}] "
                    f"{citation['filename']}, "
                    f"page {citation['page']}"
                )

            else:

                print(
                    f"[{citation['id']}] "
                    f"{citation['filename']}"
                )

        print()


if __name__ == "__main__":
    main()