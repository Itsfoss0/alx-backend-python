#!/usr/bin/env python3

"""
Randomly spawn up the previous coroutine
"""


from asyncio import as_completed
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function runs the wait_random coroutine 'n' times
    Args:
        n (int): number of times to run the coroutine
        max_delay (int): Maximum delay when running the wait_random
    """
    if not isinstance(n, int) or not isinstance(max_delay, int):
        raise TypeError('expected integer values to be passed')

    tasks = [wait_random(max_delay) for round in range(n)]
    return [await task for task in as_completed(tasks)]
