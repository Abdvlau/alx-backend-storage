#!/usr/bin/env python3
"""
This module contains a function that insert
a new document in to a collection base on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    insert a new document
    """
    new_school = mongo_collection.insert_one(kwargs)
    return new_school.inserted_id
