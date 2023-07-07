#!/usr/bin/env python3

"""
type annotated funtion to sum list items
if they are floats
"""

from functools import reduce
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    function to sum list items
    Args:
        input_list (list): a list of floats
    Returns
        returns a float
    """
    if not isinstance(input_list, list):
        raise TypeError("expected a list as input")
    return float(reduce(lambda x, y: x + y, input_list))


if __name__ == "__main__":
    print(sum_list([1, 2, 3, 4]))
