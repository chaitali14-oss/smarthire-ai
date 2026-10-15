
import pytest

from database import get_resume
from resume_service import process_resume


def test_process_resume_cleans_and_stores_text(tmp_path):
    db_path = tmp_path / "service_test.db"

    resume_id = process_resume(
        "candidate.pdf",
        "   Python    Developer\n\n\nSkills: SQL   ",
        db_path,
    )

    resume = get_resume(resume_id, db_path)

    assert resume is not None
    assert resume["filename"] == "candidate.pdf"
    assert resume["cleaned_text"] == "Python Developer\n\nSkills: SQL"


def test_process_resume_handles_empty_text(tmp_path):
    db_path = tmp_path / "empty_test.db"

    resume_id = process_resume("empty.pdf", "", db_path)

    resume = get_resume(resume_id, db_path)

    assert resume is not None
    assert resume["cleaned_text"] == ""


def test_process_resume_rejects_non_string_text(tmp_path):
    db_path = tmp_path / "invalid_test.db"

    with pytest.raises(TypeError, match="Resume text must be a string."):
        process_resume("candidate.pdf", None, db_path)
