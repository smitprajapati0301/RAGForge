"""
Prompt Builder

Builds grounded prompts using retrieved context and source citations.
"""

from app.prompts.prompt_loader import prompt_loader
from app.citations.citation_formatter import CitationFormatter


class PromptBuilder:
    """Builds prompts for grounded RAG responses."""

    @staticmethod
    def build(
        question: str,
        results: list[dict],
        citations: list[dict],
    ) -> str:
        """
        Build the final grounded prompt.

        Args:
            question: User's question.
            results: Re-ranked retrieval results.
            citations: Generated source citations.

        Returns:
            Prompt string for the LLM.
        """

        context_parts = []

        for result in results:

            chunk = result["chunk"]

            citation_id = None

            # Find the citation associated with this chunk.
            for citation in citations:

                if (
                    citation["filename"]
                    == chunk.metadata.get("filename")
                    and citation.get("page")
                    == chunk.metadata.get("page")
                ):
                    citation_id = citation["id"]
                    break

            if citation_id is not None:

                context_parts.append(
                    f"[{citation_id}]\n"
                    f"{chunk.text}"
                )

            else:

                context_parts.append(chunk.text)

        context = "\n\n".join(context_parts)

        citation_text = CitationFormatter.format(
            citations
        )

        template = prompt_loader.get_prompt(
            "rag_prompt"
        )

        return template.format(
            context=context,
            question=question,
            citations=citation_text,
        )