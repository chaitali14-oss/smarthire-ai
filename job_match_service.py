
from database import get_resume
from job_matcher import match_resume_to_job


def match_saved_resume_to_job(
    resume_id: int,
    job_description: str,
    db_path=None,
) -> dict:
    """Match a saved resume against a job description."""

    if not isinstance(resume_id, int) or isinstance(resume_id, bool):
        raise TypeError("Resume ID must be an integer.")

    if resume_id <= 0:
        raise ValueError("Resume ID must be a positive integer.")

    if not isinstance(job_description, str):
        raise TypeError("Job description must be a string.")

    if not job_description.strip():
        raise ValueError("Job description cannot be empty.")

    if db_path is None:
        resume = get_resume(resume_id)
    else:
        resume = get_resume(resume_id, db_path)

    if resume is None:
        raise ValueError(f"No resume found with ID {resume_id}.")

    result = match_resume_to_job(
        resume["cleaned_text"],
        job_description,
    )

    return {
        "resume_id": resume["id"],
        "filename": resume["filename"],
        **result,
    }
