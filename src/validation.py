import re


def validate_german_plate(plate_string):
    """
    Given a string, returns True if it matches german plate's format

    :param str plate_string: plate string code
    """

    result = re.search(r'^([A-Z]){1,3}-([A-Z]){1,2}([1-9])([0-9]){0,3}$', plate_string)
    return True if result else False
