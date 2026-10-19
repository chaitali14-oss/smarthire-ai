
import sqlite3
from pathlib import Path
import json
from contextlib import closing, contextmanager


DEFAULT_DB_PATH = Path(__file__).parent / "data" / "smarthire.db"

@contextmanager
def database_connection(db_path):
    """Manage a SQLite transaction and always close its connection."""
    with closing(sqlite3.connect(db_path)) as connection:
        with connection:
            yield connection


def initialize_database(db_path=DEFAULT_DB_PATH):
    """Create the resumes table if it does not already exist."""
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    with database_connection(db_path) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS resumes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                cleaned_text TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS candidate_profiles (
                resume_id INTEGER PRIMARY KEY,
                emails TEXT NOT NULL,
                phone_numbers TEXT NOT NULL,
                skills TEXT NOT NULL,
                education TEXT NOT NULL,
                FOREIGN KEY (resume_id) REFERENCES resumes(id)
                    ON DELETE CASCADE
            )
            """
        )


def insert_resume(filename, cleaned_text, db_path=DEFAULT_DB_PATH):
    """Save resume metadata and cleaned text; return the new record ID."""
    if not isinstance(filename, str) or not filename.strip():
        raise ValueError("Filename must be a non-empty string.")

    if not isinstance(cleaned_text, str):
        raise TypeError("Cleaned resume text must be a string.")

    initialize_database(db_path)

    with database_connection(db_path) as connection:
        cursor = connection.execute(
            """
            INSERT INTO resumes (filename, cleaned_text)
            VALUES (?, ?)
            """,
            (filename.strip(), cleaned_text),
        )
        return cursor.lastrowid


def get_resume(resume_id, db_path=DEFAULT_DB_PATH):
    """Retrieve one resume by ID, or return None if it does not exist."""
    initialize_database(db_path)

    with database_connection(db_path) as connection:
        connection.row_factory = sqlite3.Row
        row = connection.execute(
            """
            SELECT id, filename, cleaned_text, created_at
            FROM resumes
            WHERE id = ?
            """,
            (resume_id,),
        ).fetchone()

        return dict(row) if row else None

def save_candidate_profile(resume_id, profile, db_path=DEFAULT_DB_PATH):
    """Save a structured candidate profile linked to a resume."""
    if not isinstance(profile, dict):
        raise TypeError("Candidate profile must be a dictionary.")

    required_fields = (
        "emails",
        "phone_numbers",
        "skills",
        "education",
    )

    if any(
        field not in profile or not isinstance(profile[field], list)
        for field in required_fields
    ):
        raise ValueError("Profile must contain all required list fields.")

    initialize_database(db_path)

    with database_connection(db_path) as connection:
        connection.execute(
            """
            INSERT INTO candidate_profiles (
                resume_id, emails, phone_numbers, skills, education
            )
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(resume_id) DO UPDATE SET
                emails = excluded.emails,
                phone_numbers = excluded.phone_numbers,
                skills = excluded.skills,
                education = excluded.education
            """,
            (
                resume_id,
                json.dumps(profile["emails"]),
                json.dumps(profile["phone_numbers"]),
                json.dumps(profile["skills"]),
                json.dumps(profile["education"]),
            ),
        )


def get_candidate_profile(resume_id, db_path=DEFAULT_DB_PATH):
    """Retrieve a structured candidate profile, or None if missing."""
    initialize_database(db_path)

    with database_connection(db_path) as connection:
        connection.row_factory = sqlite3.Row
        row = connection.execute(
            """
            SELECT resume_id, emails, phone_numbers, skills, education
            FROM candidate_profiles
            WHERE resume_id = ?
            """,
            (resume_id,),
        ).fetchone()

    if row is None:
        return None

    return {
        "resume_id": row["resume_id"],
        "emails": json.loads(row["emails"]),
        "phone_numbers": json.loads(row["phone_numbers"]),
        "skills": json.loads(row["skills"]),
        "education": json.loads(row["education"]),
    }