#!/usr/bin/env python3

"""
Module with annoated function
With Union types
"""

from functools import reduce
from typing import Union, List

mdx_list_type = List[Union[int, float]]


def sum_mixed_list(mxd_list: mdx_list_type) -> float:
    """
    Sum a list of mixed values (int and floats)
    Args:
        mxd_list (list): List of the values to sum
    Returns:
        returns a float
    """
    return float(reduce(lambda x, y: x + y, mxd_list))
