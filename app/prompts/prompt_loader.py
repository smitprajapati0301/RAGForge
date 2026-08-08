"""
Prompt Loader

Loads prompt templates from prompts.yaml.
"""

from pathlib import Path

import yaml


class PromptLoader:
    """Loads prompt templates from YAML."""

    def __init__(self):

        prompt_file = Path("configs/prompts.yaml")

        with open(prompt_file, "r", encoding="utf-8") as file:
            self.prompts = yaml.safe_load(file)

    def get_prompt(self, name: str) -> str:
        """
        Return a prompt template by name.
        """

        return self.prompts[name]


prompt_loader = PromptLoader()