
import unittest

from job_matcher import match_resume_to_job


class TestJobMatcher(unittest.TestCase):

    def test_all_required_skills_match(self):
        result = match_resume_to_job(
            "Python SQL Java",
            "Python SQL Java",
        )

        self.assertEqual(result["match_score"], 100.0)
        self.assertEqual(
            result["matched_skills"],
            ["Python", "Java", "SQL"],
        )
        self.assertEqual(result["missing_skills"], [])

    def test_partial_skill_match(self):
        result = match_resume_to_job(
            "Python SQL Java",
            "Python SQL Java Spring Boot",
        )

        self.assertEqual(result["match_score"], 75.0)
        self.assertEqual(
            result["missing_skills"],
            ["Spring Boot"],
        )

    def test_no_matching_skills(self):
        result = match_resume_to_job(
            "HTML CSS",
            "Python Java SQL",
        )

        self.assertEqual(result["match_score"], 0.0)
        self.assertEqual(result["matched_skills"], [])
        self.assertEqual(
            result["missing_skills"],
            ["Python", "Java", "SQL"],
        )

    def test_case_insensitive_matching(self):
        result = match_resume_to_job(
            "python sql",
            "PYTHON SQL",
        )

        self.assertEqual(result["match_score"], 100.0)

    def test_javascript_alias_matches_canonical_skill(self):
        result = match_resume_to_job(
            "Python JS",
            "Python JavaScript",
        )

        self.assertEqual(result["match_score"], 100.0)
        self.assertEqual(
            result["matched_skills"],
            ["Python", "JavaScript"],
        )
        self.assertEqual(result["missing_skills"], [])

    def test_job_without_recognized_skills(self):
        result = match_resume_to_job(
            "Python Java",
            "We are looking for a motivated candidate.",
        )

        self.assertEqual(result["match_score"], 0.0)
        self.assertEqual(result["total_required_skills"], 0)

    def test_empty_job_description_raises_error(self):
        with self.assertRaises(ValueError):
            match_resume_to_job("Python SQL", "   ")

    def test_invalid_resume_input_raises_error(self):
        with self.assertRaises(TypeError):
            match_resume_to_job(None, "Python SQL")

    def test_invalid_job_input_raises_error(self):
        with self.assertRaises(TypeError):
            match_resume_to_job("Python SQL", None)


if __name__ == "__main__":
    unittest.main()
