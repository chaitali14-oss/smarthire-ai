
import tempfile
import unittest
from pathlib import Path

import pymupdf

from resume_parser import extract_text_from_pdf


class TestResumeParser(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.pdf_path = Path(self.temp_dir.name) / "sample.pdf"

        with pymupdf.open() as document:
            page = document.new_page()
            page.insert_text(
                (72, 72),
                "Candidate: Alex Morgan\n"
                "Skills: Python, SQL, Machine Learning",
            )
            document.save(self.pdf_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_extracts_resume_text(self):
        text = extract_text_from_pdf(self.pdf_path)

        self.assertIn("Alex Morgan", text)
        self.assertIn("Python", text)
        self.assertIn("Machine Learning", text)

    def test_missing_file_raises_error(self):
        missing_path = Path(self.temp_dir.name) / "missing.pdf"

        with self.assertRaises(FileNotFoundError):
            extract_text_from_pdf(missing_path)

    def test_non_pdf_file_raises_error(self):
        text_path = Path(self.temp_dir.name) / "resume.txt"
        text_path.write_text("This is not a PDF.", encoding="utf-8")

        with self.assertRaises(ValueError):
            extract_text_from_pdf(text_path)

    def test_empty_pdf_raises_error(self):
        empty_pdf_path = Path(self.temp_dir.name) / "empty.pdf"

        with pymupdf.open() as document:
            document.new_page()
            document.save(empty_pdf_path)

        with self.assertRaises(ValueError):
            extract_text_from_pdf(empty_pdf_path)


if __name__ == "__main__":
    unittest.main()
