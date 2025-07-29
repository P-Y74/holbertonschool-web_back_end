#!/usr/bin/env python3
"""
async_comprehension module

This module defines a coroutine that collects 10 random floating-point numbers
from an asynchronous generator using an async comprehension.
"""


from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Asynchronously collect 10 random float numbers.

    This coroutine uses an async comprehension to iterate over the
    async_generator coroutine, which yields 10 random float values.
    The collected numbers are returned as a list.

    Returns:
        List[float]: A list containing 10 randomly generated float numbers
        between 0 and 10.
    """
    result = [numbers async for numbers in async_generator()]
    return result
