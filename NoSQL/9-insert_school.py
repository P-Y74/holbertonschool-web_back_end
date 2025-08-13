#!/usr/bin/env python3
"""Module to insert a new document into a MongoDB collection.

This module provides a function to insert a new document into a
MongoDB collection using keyword arguments (**kwargs). It returns
the `_id` of the newly inserted document.
"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """Insert a new document into a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection):
            The MongoDB collection object where the document will be inserted.
        **kwargs:
            Arbitrary keyword arguments representing the document's fields
            and values.

    Returns:
        ObjectId: The `_id` of the inserted document.
    """
    inserted = mongo_collection.insert_one(kwargs)
    return inserted.inserted_id
