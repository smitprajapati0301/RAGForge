"""
Tests for document loaders.
"""

from pathlib import Path

import pytest

from app.ingestion.factory import LoaderFactory


def test_supported_pdf_loader():
    """
    Verify that the PDF loader can be created.
    """

    loader = LoaderFactory.get_loader(
        "sample.pdf"
    )

    assert loader is not None


def test_supported_docx_loader():
    """
    Verify that the DOCX loader can be created.
    """

    loader = LoaderFactory.get_loader(
        "sample.docx"
    )

    assert loader is not None