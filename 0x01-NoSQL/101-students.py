#!/usr/bin/env python3
"""improved 12-log_stats.py by adding the top 10 of the most
present IPs in the collection nginx of the database logs
"""


def top_students(mongo_collection):
    """ filter by score"""
    return mongo_collection.aggregate([
        {"$project":{"name": "$name","averageScore": {"$avg": "$topics.score"}}},
        {"$sort":{"averageScore": -1}}])
