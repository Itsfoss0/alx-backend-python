#!/usr/bin/env python3

"""
Type annotated function
for adding two numbers
"""


def add(a: float, b: float) -> float:
    """
    Function to add two numbers together
    Args:
        a (float): first number to add
        b (float): second number to add
    Returns:
        returns a float
   """
    if isinstance(a, float) and isinstance(b, float):
        return float(a + b)
    raise TypeError('Enter float values')
