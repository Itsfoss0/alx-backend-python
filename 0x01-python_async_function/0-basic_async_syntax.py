#!/usr/bin/env python3

"""
basics of concurent programming in python
using the asyncio library
"""

from random import random
from asyncio import sleep


async def wait_random(max_delay: int = 10) -> float:
    """
    This coroutine waits for a few seconds
    Args:
        max_delay (int)
    """
    wait_time = random() * max_delay
    await sleep(wait_time)
    return float(wait_time)
