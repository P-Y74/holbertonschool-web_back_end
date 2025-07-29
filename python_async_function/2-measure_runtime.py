#!/usr/bin/env python3
"""
Module to measure the average execution time of asynchronous coroutines.

This script imports the wait_n coroutine and uses it to compute the average
runtime for n concurrent executions of wait_random with a given max_delay.
"""


import asyncio
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average runtime of wait_n with given parameters.

    This function runs the `wait_n` coroutine with the given number of
    tasks `n`
    and a maximum delay `max_delay`. It measures the total execution time
    for all
    the coroutines to complete and returns the average execution time
    per coroutine.

    Args:
        n (int): Number of times to run wait_random concurrently.
        max_delay (int): Maximum delay for each wait_random call.

    Returns:
        float: Average time per coroutine (total execution time divided by n).
    """
    start = time()
    asyncio.run(wait_n(n, max_delay))
    end = time()
    return (end - start) / n
