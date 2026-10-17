

import pytest

from database import (
    get_candidate_profile,
    get_resume,
    initialize_database,
    insert_resume,
    save_candidate_profile,
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


def test_save_and_get_candidate_profile(tmp_path):
    db_path = tmp_path / "profile_test.db"

    resume_id = insert_resume(
        "candidate.pdf",
        "Python Developer with SQL skills",
        db_path,
    )

    profile = {
        "emails": ["alex@gmail.com"],
        "phone_numbers": ["9876543210"],
        "skills": ["Python", "SQL"],
        "education": ["MCA"],
    }

    save_candidate_profile(resume_id, profile, db_path)

    saved_profile = get_candidate_profile(resume_id, db_path)

    assert saved_profile is not None
    assert saved_profile["resume_id"] == resume_id
    assert saved_profile["emails"] == ["alex@gmail.com"]
    assert saved_profile["phone_numbers"] == ["9876543210"]
    assert saved_profile["skills"] == ["Python", "SQL"]
    assert saved_profile["education"] == ["MCA"]


def test_save_candidate_profile_updates_existing_profile(tmp_path):
    db_path = tmp_path / "profile_update_test.db"

    resume_id = insert_resume("candidate.pdf", "Resume text", db_path)

    first_profile = {
        "emails": ["old@gmail.com"],
        "phone_numbers": [],
        "skills": ["Java"],
        "education": ["BCA"],
    }

    updated_profile = {
        "emails": ["new@gmail.com"],
        "phone_numbers": ["9876543210"],
        "skills": ["Python", "SQL"],
        "education": ["MCA"],
    }

    save_candidate_profile(resume_id, first_profile, db_path)
    save_candidate_profile(resume_id, updated_profile, db_path)

    saved_profile = get_candidate_profile(resume_id, db_path)

    assert saved_profile["emails"] == ["new@gmail.com"]
    assert saved_profile["phone_numbers"] == ["9876543210"]
    assert saved_profile["skills"] == ["Python", "SQL"]
    assert saved_profile["education"] == ["MCA"]


def test_save_candidate_profile_rejects_invalid_profile(tmp_path):
    db_path = tmp_path / "invalid_profile_test.db"

    with pytest.raises(
        TypeError,
        match="Candidate profile must be a dictionary.",
    ):
        save_candidate_profile(1, None, db_path)

    with pytest.raises(
        ValueError,
        match="Profile must contain all required list fields.",
    ):
        save_candidate_profile(
            1,
            {"emails": [], "skills": [], "education": []},
            db_path,
        )
