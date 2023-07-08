#!/usr/bin/env python3

"""
Safely get a dictionary value by key
If the key doesn't exist, return a default value
"""

from typing import TypeVar, Union, Mapping, Any

T = TypeVar('T')
dict_type = Mapping
key_type = Any
def_type = Union[T, None]
ret_type = Union[Any, T]


def safely_get_value(
    dct: dict_type,
    key: key_type,
    default: def_type = None
        ) -> ret_type:
    """
    Function to safely get a dictionary value given a key
    Args:
        dct (dict): the dictionary to lookup a value
        key (string): the key we want to lookup
        default (Any): the default value to return if no key
    Returns:
        Returns dict[key] if key in dict.keys()
        else; returns default
    """
    if key in dct:
        return dct[key]
    else:
        return default
