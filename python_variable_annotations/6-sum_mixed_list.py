#!/usr/bin/env python3
"""
Module that provides a function to sum a list containing integers and floats,
returning the result as a float.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing both integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of numbers
        (integers and/or floats).

    Returns:
        float: The total sum of the numbers in the list as a float.
    """
    return sum(mxd_lst)
