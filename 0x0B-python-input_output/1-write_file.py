#!/usr/bin/python3
"""Defines function that writes a string to a text file. """


def write_file(filename="", text=""):
    """func that writes a string to a text file and
    return the number of char written
    Args:
        filename (string): file name to write
        text (string): string of charcters to write in the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        num_chars = f.write(text)
    return (num_chars)
