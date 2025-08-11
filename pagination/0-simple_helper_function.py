#!/usr/bin/env python3
"""
Module to provide pagination helper functions.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive)
                         and the end index (exclusive) corresponding to the
                         range of items to display on the given page.

    Examples:
        >>> index_range(1, 10)
        (0, 10)
        >>> index_range(3, 5)
        (10, 15)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
