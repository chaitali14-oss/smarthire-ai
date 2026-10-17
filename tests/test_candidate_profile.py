
from resume_service import build_candidate_profile


def test_build_candidate_profile_extracts_candidate_information():
    text = """
    Email: alex@gmail.com
    Phone: 9876543210
    Skills: Python, Java, Spring Boot, SQL
    Education: MCA
    """

    profile = build_candidate_profile(text)

    assert profile["emails"] == ["alex@gmail.com"]
    assert profile["phone_numbers"] == ["9876543210"]
    assert profile["skills"] == ["Python", "Java", "SQL", "Spring Boot"]
    assert profile["education"] == ["MCA"]


def test_build_candidate_profile_handles_missing_information():
    profile = build_candidate_profile("Worked at ABC Company")

    assert profile["emails"] == []
    assert profile["phone_numbers"] == []
    assert profile["skills"] == []
    assert profile["education"] == []


def test_build_candidate_profile_cleans_text_before_extraction():
    profile = build_candidate_profile(
        "   Email: alex@gmail.com   "
    )

    assert profile["emails"] == ["alex@gmail.com"]
