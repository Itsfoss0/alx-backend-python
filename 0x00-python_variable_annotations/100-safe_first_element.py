#!/usr/bin/env python3

"""
Guess I couldn't have done it without a docstring now could I?
"""

from typing import Sequence, Any, Union

lst_type = Sequence[Any]
return_type = Union[Any, None]


def safe_first_element(lst: lst_type) -> return_type:
    """
    Get the first element in a sequence safely
    If the there's no elements, return None
    Args:
        lst (list): A list of elements of any type
    Returns:
        if  element != None; Return first element
        else return None
    """
    if lst:
        return lst[0]
    else:
        return None
