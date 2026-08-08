"""
Tokenizer

Converts text into lowercase word tokens for BM25 indexing.
"""

import re


class Tokenizer:
    """Simple tokenizer for BM25."""

    @staticmethod
    def tokenize(text: str) -> list[str]:
        """
        Convert text into lowercase tokens.
        """

        text = text.lower()

        # Extract words while ignoring punctuation
        return re.findall(r"\b\w+\b", text)