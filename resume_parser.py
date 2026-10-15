
"""PDF text extraction utilities for SmartHire AI."""

from pathlib import Path

import pymupdf


def extract_text_from_pdf(pdf_path: str | Path) -> str:
    """Extract text from all pages of a PDF resume.

    Args:
        pdf_path: Path to the resume PDF file.

    Returns:
        Extracted text from the PDF.

    Raises:
        FileNotFoundError: If the PDF file does not exist.
        ValueError: If the file is not a PDF or contains no extractable text.
    """
    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {path}")

    if not path.is_file() or path.suffix.lower() != ".pdf":
        raise ValueError("Please provide a valid PDF file path.")

    extracted_pages = []

    with pymupdf.open(path) as document:
        for page in document:
            page_text = page.get_text("text").strip()
            if page_text:
                extracted_pages.append(page_text)

    extracted_text = "\n\n".join(extracted_pages).strip()

    if not extracted_text:
        raise ValueError(
            "No extractable text found. The PDF may be empty or scanned."
        )

    return extracted_text
