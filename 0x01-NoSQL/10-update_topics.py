#!/usr/bin/env python3
"""This module defines a function that changes school topic
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """ update many rows
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
