
from database import insert_resume, save_candidate_profile
from text_cleaner import clean_resume_text
from resume_extractor import (
    extract_email,
    extract_phone_numbers,
    extract_technical_skills,
    extract_education,
)


def build_candidate_profile(extracted_text: str) -> dict:
    """Build a structured candidate profile from resume text."""
    cleaned_text = clean_resume_text(extracted_text)

    return {
        "emails": extract_email(cleaned_text),
        "phone_numbers": extract_phone_numbers(cleaned_text),
        "skills": extract_technical_skills(cleaned_text),
        "education": extract_education(cleaned_text),
    }


def process_resume(filename: str, extracted_text: str, db_path=None) -> int:
    """Clean extracted resume text and store it in SQLite."""
    cleaned_text = clean_resume_text(extracted_text)

    if db_path is None:
        return insert_resume(filename, cleaned_text)

    return insert_resume(filename, cleaned_text, db_path)



def process_resume_with_profile(
    filename: str,
    extracted_text: str,
    db_path=None,
) -> dict:
    """Store a resume and its structured candidate profile in SQLite."""
    cleaned_text = clean_resume_text(extracted_text)
    profile = build_candidate_profile(cleaned_text)

    if db_path is None:
        resume_id = insert_resume(filename, cleaned_text)
        save_candidate_profile(resume_id, profile)
    else:
        resume_id = insert_resume(filename, cleaned_text, db_path)
        save_candidate_profile(resume_id, profile, db_path)

    return {
        "resume_id": resume_id,
        "filename": filename,
        "cleaned_text": cleaned_text,
        "profile": profile,
    }
