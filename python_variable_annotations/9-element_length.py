#!/usr/bin/env python3
"""
Module defining a function to return a list of tuples pairing each
element from an iterable of sequences with its length.
"""


from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples where each tuple contains an element from
    the input iterable and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences
        (like strings, lists, etc).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples with each sequence
        and its length.
    """
    return [(i, len(i)) for i in lst]
