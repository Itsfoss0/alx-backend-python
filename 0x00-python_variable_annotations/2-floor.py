#!/usr/bin/env python3

"""
Type annotated float function
to cast a float to an int
"""


def floor(n: float) -> int:
    """
    Cast a float to an int
    Args:
        n (float): the value to cast
    Returns:
       returns an int
    """
    if not isinstance(n, float):
        raise TypeError('An invalid parameter passed, float was expected')
    return int(n)
