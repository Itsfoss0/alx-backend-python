#!/usr/bin/env python3

""""
Practicing async programming and concurrency
using the asyncio library
"""

import asyncio

async def hi_mom():
    """
    Simple function to say Hi Mom
    a couple of times
    """
    print("Hi Mom One")
    await asyncio.sleep(1)
    print("Hi Mom once again (2)")

async def run_function_n_times(function, n_times):
    """
    Repeatedly run a function a specified number of times
    """
    for _ in range(int(n_times)):
        await function()


if __name__ == "__main__":
    