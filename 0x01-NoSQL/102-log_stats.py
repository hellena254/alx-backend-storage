#!/usr/bin/env python3
"""
Top ten logs
"""

from pymongo import MongoClient

def print_nginx_logs_stats(nginx_collection):
    """
    Prints statistics about Nginx request logs.

    Args:
    - nginx_collection: pymongo collection object for Nginx logs
    """
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("HTTP Methods:")
    for method in methods:
        req_count = nginx_collection.count_documents({"method": method})
        print(f"\t{method}: {req_count}")

    status_checks_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_checks_count} status checks")


def print_top_ip_stats(nginx_collection):
    """
    Prints statistics about the top 10 HTTP IPs in the Nginx logs.

    Args:
    - nginx_collection: pymongo collection object for Nginx logs
    """
    print("Top 10 IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = nginx_collection.aggregate(pipeline)
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


def main():
    """
    Main function to run the script and print Nginx logs statistics.
    """
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx

    print_nginx_logs_stats(nginx_collection)
    print_top_ip_stats(nginx_collection)


if __name__ == "__main__":
    main()
