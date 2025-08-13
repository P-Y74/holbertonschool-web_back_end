#!/usr/bin/env python3
"""update_topics module.

This module provides a function to update the 'topics' field
for all documents in a MongoDB collection matching a given school name.
"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """Update the 'topics' field of all school documents with a given name.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
        collection object.
        name (str): The name of the school to update.
        topics (list of str): The list of topics to assign to the
        'topics' field.

    Returns:
        pymongo.results.UpdateResult: The result of the update operation.
    """
    update_topic = mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
