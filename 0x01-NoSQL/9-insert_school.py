#!/usr/bin/python3
"""
function that inserts a new document in a collection based on kwargs
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection 
    Args:
        mongo_collection: The MongoDB collection object.
        **kwargs: Keyword arguments
    """
    new = mongo_collection.insert_one(kwargs)
    return new.inserted_id

