#!/usr/bin/env python3
"""
Module to list all documents in a MongoDB collection using PyMongo.

This module contains a function that retrieves all documents from
a given MongoDB collection and returns them as a list.
"""


def list_all(mongo_collection):
    """
    Retrieve all documents from a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection):
            The PyMongo collection object from which to retrieve documents.

    Returns:
        list: A list of documents (dict) in the collection.
              Returns an empty list if the collection has no documents.
    """
    new_collection = list(mongo_collection.find())
    return new_collection
