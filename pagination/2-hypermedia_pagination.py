#!/usr/bin/env python3
"""
Module to provide pagination helper functions and a Server class.

This module contains:

- A helper function `index_range` to calculate start and end indexes
for pagination.
- A `Server` class that loads a dataset from a CSV file of popular baby
names and provides methods to retrieve paginated data:
    - `get_page`: returns a list of rows for a given page and page size.
    - `get_hyper`: returns a dictionary with pagination metadata along with
      the requested page data (hypermedia pagination).

The dataset is cached after initial loading to optimize subsequent access.
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
    Return a dictionary containing pagination info and the page data.

    Args:
        page (int): The page number to retrieve (1-indexed). Must be > 0.
        page_size (int): The number of items per page. Must be > 0.

    Returns:
        dict: A dictionary containing:
            - page_size (int): The length of the returned dataset page.
            - page (int): The current page number.
            - data (List[List]): The dataset page.
            - next_page (int or None): Number of the next page, None if no
            next page.
            - prev_page (int or None): Number of the previous page, None if no
            previous page.
            - total_pages (int): The total number of pages in the dataset.
    """
        data = self.get_page(page, page_size)
        total_page = math.ceil(len(self.dataset()) / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_page else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_page
        }
