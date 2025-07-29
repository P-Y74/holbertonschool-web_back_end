#!/usr/bin/env python3
"""
measure_runtime module

This module defines a coroutine that measures the total execution time
of running an asynchronous comprehension coroutine four times in parallel.
"""


import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of four parallel async comprehensions.

    This coroutine uses asyncio.gather to run the async_comprehension
    coroutine four times concurrently. It measures the total elapsed
    time for all four to complete.

    Returns:
        float: The total time taken to execute the four coroutines in seconds.
    """
    start = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time()
    return end - start
