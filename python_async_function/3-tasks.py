#!/usr/bin/env python3
"""
This module provides a function to create asyncio Tasks from the
wait_random coroutine.

The main purpose of this module is to allow concurrent execution of
asynchronous delays by wrapping the coroutine returned by wait_random
in an asyncio.Task.

Functions:
    task_wait_random(max_delay): Returns an asyncio.Task wrapping
    wait_random(max_delay).
"""


import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task from the wait_random coroutine with the given delay.

    This function wraps the wait_random coroutine inside an asyncio
    Task to allow it to run concurrently when awaited inside an asyncio
    event loop.

    Args:
        max_delay (int): The maximum delay in seconds to wait.

    Returns:
        asyncio.Task: The created asyncio Task wrapping the coroutine.
    """
    coroutine = wait_random(max_delay)
    task = asyncio.create_task(coroutine)
    return task
