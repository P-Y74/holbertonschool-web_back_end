#!/usr/bin/env python3
"""
Module providing a utility function to safely retrieve the first element
of a sequence without raising an error if the sequence is empty.

This is particularly useful in duck-typed contexts where the type of the
sequence elements is unknown and can vary.
"""


from typing import Sequence, Optional, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Safely retrieve the first element of a sequence.

    Args:
        lst (Sequence[Any]): A sequence (e.g., list, tuple, string)
        of any type of elements.

    Returns:
        Optional[Any]: The first element of the sequence if it exists,
        otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
