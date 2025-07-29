#!/usr/bin/env python3
"""
async_generator module

This module defines a coroutine that generates 10 random floating-point numbers
between 0 and 10, yielding one every second in an asynchronous manner.
"""


import asyncio
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Asynchronously yield 10 random float numbers between 0 and 10.

    This coroutine loops 10 times. On each iteration, it asynchronously waits
    for 1 second, generates a random float between 0 and 10, and yields it.

    Yields:
        float: A randomly generated float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        random_number = uniform(0, 10)
        yield random_number
