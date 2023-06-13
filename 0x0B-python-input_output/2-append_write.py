#!/usr/bin/python3
"""Def func that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """ func that append strings at the end of a file
    Args:
        filename (string): file name
        text (string): string to append
    Returns:
        returns the number of characters
    """
    with open(filename, 'a', encoding='utf-8') as f:
        num_chars = f.write(text)
    return num_chars
