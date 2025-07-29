#!/usr/bin/env python3
"""Asynchronous coroutine utilities using wait_random.

This module provides an asynchronous function to concurrently run
multiple wait_random coroutines and collect their results in the
order of completion.
"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run wait_random n times concurrently with a maximum delay and
    return the list of delays in order of completion.

    Args:
        n (int): Number of concurrent wait_random coroutines to run.
        max_delay (int): Maximum delay value to pass to each wait_random call.

    Returns:
        List[float]: List of delays (float) in the order the coroutines
        finished.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    result = []
    for finished_coroutines in asyncio.as_completed(coroutines):
        delay = await finished_coroutines
        result.append(delay)
    return result
