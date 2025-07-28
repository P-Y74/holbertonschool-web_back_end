#!/usr/bin/env python3
"""
Module providing a function to safely retrieve a value from a mapping
with a specified key, using an optional default return value.
"""


from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieve a value from a dictionary-like mapping using a key.

    If the key exists in the mapping, return the corresponding value.
    Otherwise, return the provided default value.

    Args:
        dct (Mapping): The dictionary or mapping to retrieve the value from.
        key (Any): The key to look for in the mapping.
        default (Union[T, None], optional): The default value to return
            if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key if found,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
