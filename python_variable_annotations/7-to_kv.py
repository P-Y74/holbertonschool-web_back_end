#!/usr/bin/env python3
"""
Module providing a function to create a tuple with a string key and
the square of a numeric value (int or float) returned as a float.
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of a number (as a float).

    Args:
        k (str): A string key.
        v (Union[int, float]): A value to be squared, either an integer
        or a float.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string `k`,
        and the second element is the square of `v` as a float.
    """
    return (k, (v ** 2))
