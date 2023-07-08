#!/usr/bin/env python3

"""
Type annotated function that returns another function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function to return a callable
    Args:
        multiplier (float): value to multiply with
    Returns:
        returns a callable
    """
    def call_back_func(arg: float) -> float:
        """
        The callback function
        Args:
            arg (float)
        Returns:
            Returns a float
        """
        if isinstance(arg, float):
            return multiplier * arg
        raise TypeError('expected a float value')

    if not isinstance(multiplier, float):
        raise TypeError('expected a float value')
    return call_back_func
