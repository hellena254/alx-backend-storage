#!/usr/bin/env python3
"""
Script to provide stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

def nginx_logs_stats():
    """
    Provides statistics about Nginx logs stored in MongoDB.

    Output format:
    first line: x logs where x is the number of documents in this collection
    second line: Methods:
        \t<number of GET logs>
        \t<number of POST logs>
        \t<number of PUT logs>
        \t<number of PATCH logs>
        \t<number of DELETE logs>
    third line: <number of GET logs with path=/status>

    Note: Output format exactly matches the example provided.
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    # Count total logs
    total_logs = collection.count_documents({})

    # Count logs for each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}

    # Count GET logs with path="/status"
    get_status_logs = collection.count_documents({"method": "GET", "path": "/status"})

    # Print statistics in the specified format
    print(f"{total_logs} logs where {total_logs} is the number of documents in this collection")
    print("Methods:")
    for method in methods:
        print(f"\t{method}: {method_counts[method]}")
    print(f"{get_status_logs} logs with method=GET and path=/status")

if __name__ == "__main__":
    nginx_logs_stats()

