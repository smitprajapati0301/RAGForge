"""
Citation Formatter

Converts citation metadata into human-readable citation text.
"""


class CitationFormatter:
    """Formats citation information for prompts and responses."""

    @staticmethod
    def format(citations: list[dict]) -> str:
        """
        Format citations as numbered sources.
        """

        if not citations:
            return "No source information available."

        lines = []

        for citation in citations:

            citation_id = citation["id"]
            filename = citation["filename"]
            page = citation.get("page")

            if page is not None:

                lines.append(
                    f"[{citation_id}] "
                    f"{filename}, page {page}"
                )

            else:

                lines.append(
                    f"[{citation_id}] "
                    f"{filename}"
                )

        return "\n".join(lines)