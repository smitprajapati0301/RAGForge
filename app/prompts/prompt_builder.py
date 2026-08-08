"""
Prompt Builder

Builds prompts using templates stored in prompts.yaml.
"""

from app.prompts.prompt_loader import prompt_loader


class PromptBuilder:
    """Builds prompts for the LLM."""

    @staticmethod
    def build(
        question: str,
        contexts: list[str],
    ) -> str:
        """
        Build the final prompt using the YAML template.
        """

        context = "\n\n".join(contexts)

        template = prompt_loader.get_prompt("rag_prompt")

        return template.format(
            context=context,
            question=question,
        )