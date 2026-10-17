
import pytest

from database import get_candidate_profile, get_resume
from resume_service import process_resume
from resume_service import process_resume_with_profile



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


def test_process_resume_with_profile_stores_resume_and_returns_profile(tmp_path):
    db_path = tmp_path / "profile_test.db"

    result = process_resume_with_profile(
        "candidate.pdf",
        """
        Email: alex@gmail.com
        Phone: 9876543210
        Skills: Python, Java, Spring Boot, SQL
        Education: MCA
        """,
        db_path,
    )

    assert isinstance(result["resume_id"], int)
    assert result["filename"] == "candidate.pdf"
    assert result["cleaned_text"]

    assert result["profile"]["emails"] == ["alex@gmail.com"]
    assert result["profile"]["phone_numbers"] == ["9876543210"]
    assert result["profile"]["skills"] == [
        "Python", "Java", "SQL", "Spring Boot"
    ]
    assert result["profile"]["education"] == ["MCA"]

    saved_resume = get_resume(result["resume_id"], db_path)
    assert saved_resume is not None
    assert saved_resume["filename"] == "candidate.pdf"


def test_process_resume_with_profile_handles_empty_text(tmp_path):
    db_path = tmp_path / "empty_profile_test.db"

    result = process_resume_with_profile(
        "empty.pdf",
        "",
        db_path,
    )

    assert result["cleaned_text"] == ""
    assert result["profile"]["emails"] == []
    assert result["profile"]["phone_numbers"] == []
    assert result["profile"]["skills"] == []
    assert result["profile"]["education"] == []


def test_process_resume_with_profile_persists_profile_in_database(tmp_path):
    db_path = tmp_path / "integration_test.db"

    result = process_resume_with_profile(
        "candidate.pdf",
        """
        Email: alex@gmail.com
        Phone: 9876543210
        Skills: Python, Java, SQL
        Education: MCA
        """,
        db_path,
    )

    saved_profile = get_candidate_profile(
        result["resume_id"],
        db_path,
    )

    assert saved_profile is not None
    assert saved_profile["resume_id"] == result["resume_id"]
    assert saved_profile["emails"] == ["alex@gmail.com"]
    assert saved_profile["phone_numbers"] == ["9876543210"]
    assert saved_profile["skills"] == ["Python", "Java", "SQL"]
    assert saved_profile["education"] == ["MCA"]
