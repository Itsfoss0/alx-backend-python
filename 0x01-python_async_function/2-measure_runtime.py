#!/usr/bin/env python3


"""
module with a fuction to compute the
average excetion time for running a subroutine
"""

from asyncio import run
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the excetution time of a subroutine
    Args:
        n (int): number of times to run the subroutine
        max_delay (int): maximum amout of time to delay
    Returns:
        returns a float
    """
    if isinstance(n, int) and isinstance(max_delay, int):
        c_time: float = time()
        run(wait_n(n, max_delay))
        return (time() - c_time) / n
    raise TypeError('expected integer values to be passed!')
