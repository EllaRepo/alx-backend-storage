#!/usr/bin/env python3
"""This module defines a function that findd by topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """Find by topic
    """
    return mongo_collection.find({"topics": topic})
