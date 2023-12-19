#!/usr/bin/env python3
"""This module defines a function that returns all
   students sorted by average score
"""


def top_students(mongo_collection):
    """returns all    students sorted by average score
    Args:
        mongo_collection: the pymongo collection object
    """
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
