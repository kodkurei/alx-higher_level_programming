#!/usr/bin/python3
"""Save Object to a file """
import json


def save_to_json_file(my_obj, filename):
    """func that writes an object to a file using json
    Args:
        my_obj (any) :a python object
        filename (str): name of the file to write on
    Returns:
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
