
import pytest

from text_cleaner import clean_resume_text


def test_clean_resume_text_trims_outer_whitespace():
    text = "   Python Developer   "
    assert clean_resume_text(text) == "Python Developer"


def test_clean_resume_text_collapses_spaces_and_tabs():
    text = "Python    Developer\t\twith SQL"
    assert clean_resume_text(text) == "Python Developer with SQL"


def test_clean_resume_text_normalizes_newlines():
    text = "Name  \n\n\n\nSkills   \n Python"
    assert clean_resume_text(text) == "Name\n\nSkills\nPython"


def test_clean_resume_text_replaces_nonbreaking_spaces():
    text = "Python\u00a0Developer"
    assert clean_resume_text(text) == "Python Developer"


def test_clean_resume_text_removes_control_characters():
    text = "Python\x00Developer\x07"
    assert clean_resume_text(text) == "PythonDeveloper"


def test_clean_resume_text_handles_empty_input():
    assert clean_resume_text("") == ""


def test_clean_resume_text_rejects_non_string_input():
    with pytest.raises(TypeError, match="Resume text must be a string."):
        clean_resume_text(None)
