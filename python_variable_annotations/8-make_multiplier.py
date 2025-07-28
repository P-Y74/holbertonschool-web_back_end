#!/usr/bin/env python3
"""
Module defining a higher-order function that returns a multiplier function.

The returned function multiplies any given float by a preset multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier factor.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product of that float and the multiplier.
    """
    def inner(x: float) -> float:
        """Multiply input x by the multiplier."""
        return x * multiplier
    return inner
