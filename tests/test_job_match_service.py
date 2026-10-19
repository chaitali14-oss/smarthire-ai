
import sqlite3
import tempfile
import unittest
from pathlib import Path

from database import insert_resume
from job_match_service import match_saved_resume_to_job


class TestJobMatchService(unittest.TestCase):

    def setUp(self):
        temp_file = tempfile.NamedTemporaryFile(
            suffix=".db",
            delete=False,
        )
        temp_file.close()

        self.db_path = Path(temp_file.name)

        self.resume_id = insert_resume(
            "candidate.pdf",
            "Python SQL Java",
            self.db_path,
        )

    def tearDown(self):
        connection = sqlite3.connect(self.db_path)
        try:
            connection.execute("PRAGMA wal_checkpoint(TRUNCATE)")
        finally:
            connection.close()

        self.db_path.unlink(missing_ok=True)

    def test_matches_saved_resume_to_job(self):
        result = match_saved_resume_to_job(
            self.resume_id,
            "Python SQL Java Spring Boot",
            self.db_path,
        )

        self.assertEqual(result["resume_id"], self.resume_id)
        self.assertEqual(result["filename"], "candidate.pdf")
        self.assertEqual(result["match_score"], 75.0)
        self.assertEqual(
            result["matched_skills"],
            ["Python", "Java", "SQL"],
        )
        self.assertEqual(result["missing_skills"], ["Spring Boot"])

    def test_missing_resume_raises_error(self):
        with self.assertRaises(ValueError):
            match_saved_resume_to_job(
                999,
                "Python SQL",
                self.db_path,
            )

    def test_invalid_resume_id_raises_error(self):
        with self.assertRaises(TypeError):
            match_saved_resume_to_job(
                "invalid",
                "Python SQL",
                self.db_path,
            )

    def test_empty_job_description_raises_error(self):
        with self.assertRaises(ValueError):
            match_saved_resume_to_job(
                self.resume_id,
                "   ",
                self.db_path,
            )


if __name__ == "__main__":
    unittest.main()
