#!/usr/bin/env python3

"""
Type annotated typecasting function
"""


def to_str(n: float) -> str:
    """
    Function to cast a float into an int
    Args:
        n (float): the value to cast to string
    Returns:
       returns a string
    """
    if not isinstance(n, float):
        raise TypeError('Invalid argument passed, expected a float')
    return str(n)
