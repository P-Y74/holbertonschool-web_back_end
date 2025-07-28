#!/usr/bin/env python3
"""
Module that provides a function to calculate the sum of a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floating-point numbers.

    Args:
        input_list (List[float]): A list of float values to be summed.

    Returns:
        float: The total sum of all the float values in the list.
    """
    return sum(input_list)
