#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


def log_stats():
    """Prints statistics about Nginx logs."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Total logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Aggregating the count for each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count for the specific path
    status_check_count = collection.count_documents({"path": "/status"})
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
