"""
Document API Schemas

Defines request/response models related to
document uploading and indexing.
"""

from pydantic import BaseModel


class DocumentUploadResponse(BaseModel):
    """Response returned after a document is indexed."""

    message: str
    filename: str
    filetype: str
    chunks_created: int