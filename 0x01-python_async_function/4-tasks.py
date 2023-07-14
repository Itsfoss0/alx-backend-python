#!/usr/bin/env python3

"""
Module with a function (couroutine) that returns
the length of delays as a list
"""

from asyncio import as_completed
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    run the wait_random coroutine n times
    Args:
        n (int): Refer to the previous module
        max_delay (int): Check the previous module
    Returns:
        returns a list of floats
    """
    if not isinstance(n, int) or not isinstance(max_delay, int):
        raise TypeError('Expected integer values to be passed')

    tasks: list = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in as_completed(tasks)]
