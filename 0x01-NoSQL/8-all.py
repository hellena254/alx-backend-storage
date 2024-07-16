#!/usr/bin/env python3
"""list all documents in python
"""

def list_all(mongo_collection):
    """
    Lists all documents in the provided MongoDB collection
    Returns:
        list: A list of documents
    """
    return [i for i in mongo_collection.find()]
