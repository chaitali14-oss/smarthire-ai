
import unittest

from app import get_welcome_message


class TestSmartHireApp(unittest.TestCase):

    def test_project_name(self):
        message = get_welcome_message()
        self.assertIn("SMARTHIRE AI", message)

    def test_day_one_status(self):
        message = get_welcome_message()
        self.assertIn("Day 1 - Setup complete", message)

    def test_next_milestone(self):
        message = get_welcome_message()
        self.assertIn("Resume PDF text extraction", message)


if __name__ == "__main__":
    unittest.main()
