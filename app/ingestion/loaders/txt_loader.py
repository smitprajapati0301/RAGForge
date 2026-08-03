from pathlib import Path

from app.ingestion.document import Document
from app.ingestion.loaders.base_loader import BaseLoader


class TXTLoader(BaseLoader):

    def load(self, file_path: str) -> Document:

        with open(
            file_path,
            "r",
            encoding="utf-8",
        ) as file:

            text = file.read()

        metadata = {
            "filename": Path(file_path).name,
            "filetype": "txt",
        }

        return Document(
            content=text,
            metadata=metadata,
        )