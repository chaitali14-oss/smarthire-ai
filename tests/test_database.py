
import pytest

from database import (
    get_resume,
    initialize_database,
    insert_resume,
)


def test_initialize_database_creates_table(tmp_path):
    db_path = tmp_path / "test.db"

    initialize_database(db_path)

    resume = get_resume(1, db_path)
    assert resume is None


def test_insert_resume_returns_id_and_stores_record(tmp_path):
    db_path = tmp_path / "test.db"

    resume_id = insert_resume(
        "sample_resume.pdf",
        "Python Developer with SQL skills",
        db_path,
    )

    assert isinstance(resume_id, int)
    assert resume_id > 0

    resume = get_resume(resume_id, db_path)

    assert resume is not None
    assert resume["id"] == resume_id
    assert resume["filename"] == "sample_resume.pdf"
    assert resume["cleaned_text"] == "Python Developer with SQL skills"
    assert resume["created_at"]


def test_get_resume_returns_none_for_missing_id(tmp_path):
    db_path = tmp_path / "test.db"

    initialize_database(db_path)

    assert get_resume(999, db_path) is None


def test_insert_resume_rejects_empty_filename(tmp_path):
    db_path = tmp_path / "test.db"

    with pytest.raises(ValueError, match="Filename must be a non-empty string."):
        insert_resume("   ", "Some resume text", db_path)


def test_insert_resume_rejects_non_string_text(tmp_path):
    db_path = tmp_path / "test.db"

    with pytest.raises(TypeError, match="Cleaned resume text must be a string."):
        insert_resume("resume.pdf", None, db_path)
