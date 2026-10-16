
import re


def extract_email(text: str) -> list[str]:
    """Extract email addresses from resume text."""
    if not isinstance(text, str):
        raise TypeError("Resume text must be a string.")

    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

    return re.findall(pattern, text)


def extract_phone_numbers(text: str) -> list[str]:
    """Extract common Indian mobile phone numbers from resume text."""
    if not isinstance(text, str):
        raise TypeError("Resume text must be a string.")

    pattern = r"(?<!\d)(?:(?:\+91|0)[\s-]?)?[6-9]\d{4}[\s-]?\d{5}(?!\d)"

    return re.findall(pattern, text)


TECHNICAL_SKILLS = [
    "Python",
    "Java",
    "JavaScript",
    "TypeScript",
    "SQL",
    "MySQL",
    "PostgreSQL",
    "Spring Boot",
    "Spring",
    "Hibernate",
    "REST API",
    "React",
    "Angular",
    "HTML",
    "CSS",
    "Pandas",
    "NumPy",
    "Machine Learning",
    "Deep Learning",
    "NLP",
    "Power BI",
    "Docker",
    "AWS",
    "Git",
]



def extract_technical_skills(text: str) -> list[str]:
    """Extract recognized technical skills without overlapping matches."""
    if not isinstance(text, str):
        raise TypeError("Resume text must be a string.")

    found_skills = set()
    matched_spans = []

    # Check longer skill names before shorter ones.
    skills_by_length = sorted(
        TECHNICAL_SKILLS,
        key=len,
        reverse=True,
    )

    for skill in skills_by_length:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        for match in re.finditer(pattern, text, re.IGNORECASE):
            start, end = match.span()

            overlaps = any(
                start < existing_end and end > existing_start
                for existing_start, existing_end in matched_spans
            )

            if not overlaps:
                matched_spans.append((start, end))
                found_skills.add(skill)

    # Return results in the original skill-list order.
    return [
        skill
        for skill in TECHNICAL_SKILLS
        if skill in found_skills
    ]


EDUCATION_QUALIFICATIONS = [
    "Bachelor of Technology",
    "B.Tech",
    "Bachelor of Engineering",
    "B.E.",
    "Bachelor of Science",
    "B.Sc.",
    "Bachelor of Computer Applications",
    "BCA",
    "Master of Technology",
    "M.Tech",
    "Master of Engineering",
    "M.E.",
    "Master of Science",
    "M.Sc.",
    "Master of Computer Applications",
    "MCA",
    "Master of Business Administration",
    "MBA",
    "Ph.D.",
    "PhD",
    "Diploma",
    "Higher Secondary",
    "Secondary School",
]


def extract_education(text: str) -> list[str]:
    """Extract recognized education qualifications from resume text."""
    if not isinstance(text, str):
        raise TypeError("Resume text must be a string.")

    found_qualifications = set()
    matched_spans = []

    qualifications_by_length = sorted(
        EDUCATION_QUALIFICATIONS,
        key=len,
        reverse=True,
    )

    for qualification in qualifications_by_length:
        pattern = (
            r"(?<!\w)"
            + re.escape(qualification)
            + r"(?!\w)"
        )

        for match in re.finditer(pattern, text, re.IGNORECASE):
            start, end = match.span()

            overlaps = any(
                start < existing_end and end > existing_start
                for existing_start, existing_end in matched_spans
            )

            if not overlaps:
                matched_spans.append((start, end))
                found_qualifications.add(qualification)

    return [
        qualification
        for qualification in EDUCATION_QUALIFICATIONS
        if qualification in found_qualifications
    ]
