from pathlib import Path

from app.ingestion.loaders.docx_loader import DOCXLoader
from app.ingestion.loaders.markdown_loader import MarkdownLoader
from app.ingestion.loaders.pdf_loader import PDFLoader
from app.ingestion.loaders.txt_loader import TXTLoader


class LoaderFactory:

    @staticmethod
    def get_loader(file_path: str):

        extension = Path(file_path).suffix.lower()

        loaders = {
            ".pdf": PDFLoader(),
            ".docx": DOCXLoader(),
            ".txt": TXTLoader(),
            ".md": MarkdownLoader(),
        }

        if extension not in loaders:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        return loaders[extension]