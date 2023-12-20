#!/usr/bin/env python3
"""This module defines a function that logs stats
"""
from pymongo import MongoClient


def print_nginx_logs():
    """Provides some stats about Nginx logs stored in MongoDB.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Count logs
    print('{} logs'.format(nginx_collection.count_documents({})))

    # Count methods
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        method_count = nginx_collection.count_documents({'method': method})
        print('\tmethod {}: {}'.format(method, method_count))

    # Count status checks
    status_checks_count = nginx_collection.count_documents(
        {'method': 'GET', 'path': '/status'}
    )
    print('{} status check'.format(status_checks_count))

    # List top 10 IPs with the most requests
    print('IPs:')
    sorted_ips = nginx_collection.aggregate([
        {'$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}},
        {'$sort': {'totalRequests': -1}},
        {'$limit': 10},
    ])
    for sorted_ip in sorted_ips:
        ip = sorted_ip['_id']
        ip_count = sorted_ip['totalRequests']
        print('\t{}: {}'.format(ip, ip_count))


if __name__ == '__main__':
    print_nginx_logs()
