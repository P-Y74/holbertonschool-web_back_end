#!/usr/bin/env python3
"""
Module to display statistics about Nginx logs stored in MongoDB.

Connects to the 'logs' database and the 'nginx' collection, and prints:
  - total number of log documents
  - number of requests per HTTP method (GET, POST, PUT, PATCH, DELETE)
  - number of GET requests to the /status endpoint
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')

    db = client['logs']
    collection = db['nginx']

    total_collection = collection.count_documents({})
    get_count = collection.count_documents({"method": "GET"})
    post_count = collection.count_documents({"method": "POST"})
    put_count = collection.count_documents({"method": "PUT"})
    patch_count = collection.count_documents({"method": "PATCH"})
    delete_count = collection.count_documents({"method": "DELETE"})
    status_count = collection.count_documents({"method": "GET",
                                               "path": "/status"})

    print(
        f"{total_collection} logs\n"
        "Methods:\n"
        f"\tmethod GET: {get_count}\n"
        f"\tmethod POST: {post_count}\n"
        f"\tmethod PUT: {put_count}\n"
        f"\tmethod PATCH: {patch_count}\n"
        f"\tmethod DELETE: {delete_count}\n"
        f"{status_count} status check"
        )
