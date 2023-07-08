#!/usr/bin/env python3

"""
This module provides a function to zoom in on an array.

Usage:
    zoom_array(lst: Tuple, factor: int = 2) -> Tuple

Examples:
    array = [12, 72, 91]

    zoom_2x = zoom_array(array)
    # zoom_2x: (12, 12, 72, 72, 91, 91)

    zoom_3x = zoom_array(array, 3)
    # zoom_3x: (12, 12, 12, 72, 72, 72, 91, 91, 91)
"""

from typing import Any, List


def zoom_array(lst: List, factor: int = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
