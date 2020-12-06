import unittest

from src import app


class TestRoutes(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()

    # Correctly save valid plate
    def test_valid_post(self):
        data = {
            'plate': 'MP-PP123'
        }

        response = self.client.post('/plate', json=data)
        self.assertEqual(200, response.status_code)

    # Returns 400 for malformed or missing plate field
    def test_invalid_plate_field(self):
        data = {
            'plate': 10
        }

        response = self.client.post('/plate', json=data)
        self.assertEqual(400, response.status_code)

        data = {}

        response = self.client.post('/plate', json=data)
        self.assertEqual(400, response.status_code)

    # Returns 422 for plate with invalid format
    def test_invalid_plate_format(self):
        data = {
            'plate': 'M-PP023'
        }

        response = self.client.post('plate', json=data)
        self.assertEqual(422, response.status_code)

        data = {
            'plate': 'M-PP012345'
        }

        response = self.client.post('plate', json=data)
        self.assertEqual(422, response.status_code)

        data = {
            'plate': 'M-123'
        }

        response = self.client.post('plate', json=data)
        self.assertEqual(422, response.status_code)

        data = {
            'plate': '-PP123'
        }

        response = self.client.post('plate', json=data)
        self.assertEqual(422, response.status_code)
