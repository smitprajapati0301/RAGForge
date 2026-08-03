from abc import ABC, abstractmethod

from app.ingestion.document import Document


class BaseLoader(ABC):
    """
    Abstract base class for all document loaders.
    """

    @abstractmethod
    def load(self, file_path: str) -> Document:
        """
        Load a document and return a unified Document object.
        """
        pass