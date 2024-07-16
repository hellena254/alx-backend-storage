#!/usr/bin/env python3
"""
function that inserts a new document in a collection based on kwargs
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection 
    Args:
        mongo_collection: The MongoDB collection object.
        **kwargs: Keyword arguments
    Return: the _id of the newly inserted doc
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

