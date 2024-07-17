#!/usr/bin/env python3
"""contain a find by topic function """


def schools_by_topic(mongo_collection, topic):
    """find by topic in school """
    return mongo_collection.find(
       {"topics": topic}
    )
