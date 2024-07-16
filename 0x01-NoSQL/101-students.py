#!/usr/bin/env python3
"""
Python function that returns all students sorted by average score
"""

def top_students(mongo_collection):
    """
    Python function that returns all students sorted by average score
    """
    pipeline = [
        {
            '$unwind': '$topics'  # Unwind the topics array to work with individual scores
        },
        {
            '$group': {
                '_id': '$_id',  # Group by student ID
                'name': {'$first': '$name'},  # Keep the name of the student
                'averageScore': {'$avg': '$topics.score'}  # Calculate the average score of topics
            }
        },
        {
            '$sort': {'averageScore': -1}  # Sort by averageScore in descending order
        }
    ]

    students = mongo_collection.aggregate(pipeline)
    return students
