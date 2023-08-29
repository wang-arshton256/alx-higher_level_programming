#!/usr/bin/python3

def safe_print_integer(value):
    """Print an interger with "{:d}.format().

    Args:
        value (int): The interger to print.

    Returns:
        If a TypeError of ValueErro occurs -false,
        otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
