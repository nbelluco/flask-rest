import unittest

from src.validation import validate_german_plate


class TestInvalidPlate(unittest.TestCase):

    # Returns False for empty string
    def test_empty_string(self):
        self.assertFalse(validate_german_plate(''))

    # Returns False for plate containing non-letter characters
    def test_extra_chars(self):
        self.assertFalse(validate_german_plate('M&-PP123'))

    # Returns False for plate with extra digits
    def test_extra_digits(self):
        self.assertFalse(validate_german_plate('M-PP23456'))

    # Returns False for plate digits starting with 0
    def test_zero_leading_digit(self):
        self.assertFalse(validate_german_plate('M-PP0123'))

    # Returns False for plate with invalid length
    def test_invalid_length(self):
        self.assertFalse(validate_german_plate('M-PPP123'))
        self.assertFalse(validate_german_plate('-1234'))
        self.assertFalse(validate_german_plate('MPPPPP-PP123'))

    # Returns False for plat missing ending digits
    def test_invalid_ending(self):
        self.assertFalse(validate_german_plate('M-PP'))

    # Returns False for multiple valid plates concat together
    def test_multiple_plates(self):
        self.assertFalse(validate_german_plate('PPP-PP123\nPPP-PP123'))

