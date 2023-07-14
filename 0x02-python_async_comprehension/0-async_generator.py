#!/usr/bin/env python3

"""
Module with an async generator
Generates random numbers between
one and ten
"""

from asyncio import sleep
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Generate numbers between one and ten
    Args:
        None
    Returns:
        Generator
    """
    for _ in range(0, 10):
        await sleep(1)
        yield random() * 10

