import unittest

from src.validation import validate_german_plate


class TestValidation(unittest.TestCase):

    # Returns False for empty string
    def test_empty_string(self):
        result = validate_german_plate('')
        self.assertEqual(False, result)

    # Returns False for plate containing non-letter characters
    def test_extra_chars(self):
        result = validate_german_plate('M&-PP123')
        self.assertEqual(False, result)

    # Returns False for plate of invalid length
    def test_invalid_length(self):
        result = validate_german_plate('M-PPP123')
        self.assertEqual(False, result)

        result = validate_german_plate('MPPPPP-PP123')
        self.assertEqual(False, result)

    # Returns False for multiple valid plates concat together
    def test_multiple_plates(self):
        result = validate_german_plate('PPP-PP123\nPPP-PP123')
        self.assertEqual(False, result)
