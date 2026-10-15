
import sqlite3
from pathlib import Path


DEFAULT_DB_PATH = Path(__file__).parent / "data" / "smarthire.db"


def initialize_database(db_path=DEFAULT_DB_PATH):
    """Create the resumes table if it does not already exist."""
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(db_path) as connection:
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


def insert_resume(filename, cleaned_text, db_path=DEFAULT_DB_PATH):
    """Save resume metadata and cleaned text; return the new record ID."""
    if not isinstance(filename, str) or not filename.strip():
        raise ValueError("Filename must be a non-empty string.")

    if not isinstance(cleaned_text, str):
        raise TypeError("Cleaned resume text must be a string.")

    initialize_database(db_path)

    with sqlite3.connect(db_path) as connection:
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

    with sqlite3.connect(db_path) as connection:
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
