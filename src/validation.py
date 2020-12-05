import re


def validate_german_plate(plate_string):
    return re.match(r'([A-Z]){1,3}-([A-Z]){1,2}([1-9])([0-9]){0,3}', plate_string)
