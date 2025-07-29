#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine to wait for a random delay.

It defines a single coroutine function `wait_random` that takes a maximum delay
in seconds and waits for a random duration between 0 and max_delay.
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds (inclusive)
    asynchronously.

    Args:
        max_delay (int, optional): The maximum number of seconds to wait.
        Defaults to 10.

    Returns:
        float: The actual delay (in seconds) that was waited, as a float value.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
