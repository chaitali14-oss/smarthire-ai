
import unittest

from fastapi.testclient import TestClient

from api import app


class TestSmartHireAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_home_endpoint(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "message": "Welcome to SmartHire AI API",
                "status": "running",
            },
        )

    def test_health_endpoint(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "status": "healthy",
                "service": "SmartHire AI API",
            },
        )


if __name__ == "__main__":
    unittest.main()
