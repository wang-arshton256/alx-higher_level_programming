#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        "{:d}".format(value)
        return True
    except (stderr):
        return False
