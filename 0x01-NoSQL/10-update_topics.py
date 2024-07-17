#!/usr/bin/env python3
"""This module contains a function that changes school topics """


def update_topics(mongo_collection, name, topics):
    """ updates topics"""

    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
