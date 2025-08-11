#!/usr/bin/env python3
"""
Module to provide pagination helper functions.

This module contains functions and classes to assist in paginating
datasets, including calculating index ranges and serving paginated data
from a CSV file containing popular baby names.
"""

import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize a new Server instance with a cached dataset set to None.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset from the CSV file.

        Reads the CSV file specified by DATA_FILE, caches the dataset
        (excluding the header row), and returns it.

        Returns:
            List[List]: The dataset loaded from the CSV file as a list of rows,
                        where each row is a list of strings.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset.

        Args:
            page (int): The page number to retrieve (1-indexed). Must be > 0.
            page_size (int): The number of items per page. Must be > 0.

        Raises:
            AssertionError: If page or page_size are not integers greater
            than 0.

        Returns:
            List[List]: A list of rows representing the requested page of data.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        page_data = data[start:end]
        return page_data
