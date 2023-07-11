#!/usr/bin/env python3

"""
basics of concurent programming in python
using the asyncio library
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    This couroutine waits for a random number of seconds
    and returns the number of seconds waited
    Args:
        max_delay (int): Maximum delay
    Returns:
        returns a float
    """
    if not isinstance(max_delay, int):
        raise TypeError('Max wait should be an int')
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
