"""
Document API Routes

Handles document uploading and indexing.
"""

from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import (
    APIRouter,
    File,
    HTTPException,
    UploadFile,
)

from app.api.dependencies import rag_service
from app.api.schemas.document import (
    DocumentUploadResponse,
)


router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


# Supported document types.
ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".txt",
    ".md",
}


@router.post(
    "/upload",
    response_model=DocumentUploadResponse,
)
def upload_document(
    file: UploadFile = File(...),
):
    """
    Upload and index a document.

    Supported:
    - PDF
    - DOCX
    - TXT
    - Markdown
    """

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Filename is required.",
        )

    extension = Path(
        file.filename
    ).suffix.lower()

    # Validate file type.
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Unsupported file type: {extension}. "
                f"Supported types: "
                f"{', '.join(sorted(ALLOWED_EXTENSIONS))}"
            ),
        )

    temporary_path = None

    try:

        # Create a temporary file.
        with NamedTemporaryFile(
            delete=False,
            suffix=extension,
        ) as temporary_file:

            temporary_path = temporary_file.name

            # Copy uploaded file contents.
            while True:

                chunk = file.file.read(
                    1024 * 1024
                )

                if not chunk:
                    break

                temporary_file.write(chunk)

        # Run complete ingestion pipeline.
        chunks_created = rag_service.ingest_document(
            file_path=temporary_path,
            original_filename=file.filename,
)

        return DocumentUploadResponse(
            message="Document indexed successfully.",
            filename=file.filename,
            filetype=extension.lstrip("."),
            chunks_created=chunks_created,
        )

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error),
        )

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=(
                "Document processing failed: "
                f"{str(error)}"
            ),
        )

    finally:

        # Remove temporary uploaded file.
        if temporary_path:

            path = Path(
                temporary_path
            )

            if path.exists():
                path.unlink()