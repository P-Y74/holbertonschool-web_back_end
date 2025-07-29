#!/usr/bin/env python3
"""
Module to run multiple asynchronous tasks using task_wait_random.
"""


import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn multiple asynchronous tasks that wait for a random delay and
    return results
    in the order of completion.

    This function creates `n` asyncio.Tasks using
    `task_wait_random(max_delay)`, which internally wraps the coroutine
    `wait_random`. Each task waits for a random amount of time between 0 and
    `max_delay` seconds. All tasks run concurrently, and their completion
    times are collected in a list ordered by the time they finish.

    Args:
        n (int): Number of concurrent tasks to run.
        max_delay (int): Maximum delay in seconds for each task.

    Returns:
        List[float]: A list of float delays returned by each task,
                     sorted by order of task completion.
    """
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    result = []
    for finished_coroutines in asyncio.as_completed(coroutines):
        delay = await finished_coroutines
        result.append(delay)
    return result
