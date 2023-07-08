#!/usr/bin/env python3

"""
Lets duck type an iterrable object, shall We?
"""


from typing import Iterable, Sequence, List, Tuple

lst_type = Iterable[Sequence]
return_type = List[Tuple[Sequence, int]]


def element_length(lst: lst_type) -> return_type:
    return [(i, len(i)) for i in lst]
