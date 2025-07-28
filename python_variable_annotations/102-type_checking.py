#!/usr/bin/env python3
"""
Module providing a function to repeat elements in a tuple
a given number of times, returning the result as a list.
"""


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Duplicate each element in a tuple by a specified factor.

    Args:
        lst (Tuple): The input tuple containing any type of elements.
        factor (int, optional): The number of times each element should be
        repeated. Defaults to 2.

    Returns:
        List: A list with each element of the input tuple repeated
        `factor` times.

    Example:
        >>> zoom_array((1, 2), 3)
        [1, 1, 1, 2, 2, 2]
    """
    zoomed_in = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
