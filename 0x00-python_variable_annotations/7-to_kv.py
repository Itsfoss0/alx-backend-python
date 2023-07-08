#!/usr/bin/env python3

"""
Module with a type annotated function
that returns a tuple
"""


from typing import Tuple, Union

v_type = Union[int, float]
return_type = Tuple[str, float]


def to_kv(k: str, v: v_type) -> return_type:
    """
    conver k, v to a tuple
    Args:
        k (str): any valid string value
        v (int/float): An int or float value
    """
    if not isinstance(k, str):
        raise TypeError('expected a string')
    v_squared: float = v * v
    return tuple([k, v_squared])
