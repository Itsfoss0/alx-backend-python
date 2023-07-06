#!/usr/bin/env python3

"""
type annotated function to add two strings
"""


def concat(str1: str, str2: str) -> str:
    """
    function to add two strings
    Args:
        str1 (str): first string
        str2 (str): second string
    Returns:
        return a string
    """

    if isinstance(str1, str) and isinstance(str2, str):
        return f"{str1}{str2}"
    raise TypeError("Only strings should be passed")
