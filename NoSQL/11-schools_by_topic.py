#!/usr/bin/env python3
"""
Module for querying a MongoDB collection of schools.
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Return all schools in the collection that teach a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo
        collection object containing school documents.
        topic (str): The topic to filter schools by.

    Returns:
        pymongo.cursor.Cursor: A cursor to the documents of schools that
        include the specified topic.
    """
    schools = mongo_collection.find({'topics': topic})
    return schools
