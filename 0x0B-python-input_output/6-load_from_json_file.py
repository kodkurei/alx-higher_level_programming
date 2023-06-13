#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """func that creates an object from a JSONfile
    Args:
        filename (str): name of the file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
