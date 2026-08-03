import re


class TextCleaner:
    """
    Cleans extracted text before chunking.
    """

    @staticmethod
    def clean(text: str) -> str:

        # Normalize Windows line endings
        text = text.replace("\r\n", "\n")

        # Remove multiple spaces/tabs
        text = re.sub(r"[ \t]+", " ", text)

        # Remove excessive blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Remove leading/trailing whitespace
        text = text.strip()

        return text