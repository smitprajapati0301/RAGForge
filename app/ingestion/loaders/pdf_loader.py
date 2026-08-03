from pathlib import Path

import fitz

from app.ingestion.document import Document
from app.ingestion.loaders.base_loader import BaseLoader


class PDFLoader(BaseLoader):
    """
    Loader for PDF documents using PyMuPDF.
    """

    def load(self, file_path: str) -> Document:
        with fitz.open(file_path) as pdf:
            text = "\n".join(page.get_text() for page in pdf)

            metadata = {
                "filename": Path(file_path).name,
                "filepath": str(Path(file_path).resolve()),
                "filetype": "pdf",
                "pages": len(pdf),
            }

            return Document(
                content=text,
                metadata=metadata,
            )