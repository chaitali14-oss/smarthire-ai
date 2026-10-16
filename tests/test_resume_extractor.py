
import pytest

from resume_extractor import (
    extract_email,
    extract_phone_numbers,
    extract_technical_skills,
    extract_education,
)
def test_extracts_single_email():
    assert extract_email("Contact: alex@gmail.com") == [
        "alex@gmail.com"
    ]


def test_extracts_multiple_emails():
    text = "alex@gmail.com and sam@yahoo.com"

    assert extract_email(text) == [
        "alex@gmail.com",
        "sam@yahoo.com",
    ]


def test_returns_empty_list_when_no_email_exists():
    assert extract_email("No email provided") == []


def test_rejects_non_string_input():
    with pytest.raises(TypeError, match="Resume text must be a string."):
        extract_email(None)


def test_extracts_indian_mobile_number():
    assert extract_phone_numbers("Phone: 9876543210") == [
        "9876543210"
    ]


def test_extracts_multiple_phone_formats():
    text = "+91 87654 32109 and 098765-43210"

    assert extract_phone_numbers(text) == [
        "+91 87654 32109",
        "098765-43210",
    ]


def test_ignores_long_digit_sequences_and_missing_numbers():
    text = "Experience: 2024, ID: 1234567890123"

    assert extract_phone_numbers(text) == []
    assert extract_phone_numbers("No phone available") == []


def test_phone_extractor_rejects_non_string_input():
    with pytest.raises(TypeError, match="Resume text must be a string."):
        extract_phone_numbers(None)


def test_extracts_technical_skills():
    text = "Python, JavaScript, Spring Boot, SQL, Docker"

    assert extract_technical_skills(text) == [
        "Python",
        "JavaScript",
        "SQL",
        "Spring Boot",
        "Docker",
    ]


def test_skill_extraction_is_case_insensitive():
    assert extract_technical_skills("python and SPRING BOOT") == [
        "Python",
        "Spring Boot",
    ]


def test_does_not_match_java_inside_javascript():
    assert extract_technical_skills("JavaScript") == [
        "JavaScript",
    ]


def test_extracts_education_qualifications():
    text = "B.Tech, MCA, and MBA"

    assert extract_education(text) == [
        "B.Tech",
        "MCA",
        "MBA",
    ]


def test_education_extraction_is_case_insensitive():
    assert extract_education("BACHELOR OF TECHNOLOGY") == [
        "Bachelor of Technology",
    ]


def test_education_extraction_handles_missing_and_invalid_input():
    assert extract_education("Worked at ABC Company") == []

    with pytest.raises(TypeError, match="Resume text must be a string."):
        extract_education(None)
