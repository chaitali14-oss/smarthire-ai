
from database import insert_resume
from text_cleaner import clean_resume_text


def process_resume(filename: str, extracted_text: str, db_path=None) -> int:
    """Clean extracted resume text and store it in SQLite."""
    cleaned_text = clean_resume_text(extracted_text)

    if db_path is None:
        return insert_resume(filename, cleaned_text)

    return insert_resume(filename, cleaned_text, db_path)
