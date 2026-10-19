
from resume_extractor import TECHNICAL_SKILLS, extract_technical_skills


def match_resume_to_job(
    resume_text: str,
    job_description: str,
) -> dict:
    """Compare resume skills with skills required in a job description."""

    if not isinstance(resume_text, str):
        raise TypeError("Resume text must be a string.")

    if not isinstance(job_description, str):
        raise TypeError("Job description must be a string.")

    if not job_description.strip():
        raise ValueError("Job description cannot be empty.")

    # Extract recognized skills from both texts.
    candidate_skills = extract_technical_skills(resume_text)
    required_skills = extract_technical_skills(job_description)

    # Compare skills without considering letter case.
    candidate_skill_map = {
        skill.casefold(): skill for skill in candidate_skills
    }

    matched_skills = [
        skill
        for skill in required_skills
        if skill.casefold() in candidate_skill_map
    ]

    missing_skills = [
        skill
        for skill in required_skills
        if skill.casefold() not in candidate_skill_map
    ]

    # Calculate the percentage of recognized required skills matched.
    total_required = len(required_skills)

    match_score = (
        round((len(matched_skills) / total_required) * 100, 2)
        if total_required > 0
        else 0.0
    )

    return {
        "candidate_skills": candidate_skills,
        "required_skills": required_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "total_required_skills": total_required,
        "match_score": match_score,
    }
