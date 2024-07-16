#!/usr/bin/env python3
"""
Python function that returns the list of school having a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    Function that returns the list of school having a specific topic
    """
    query = {"topics": topic}
    schools = list(mongo_collection.find(query))
    return schools
