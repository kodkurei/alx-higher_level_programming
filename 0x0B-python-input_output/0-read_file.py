#!/usr/bin/python3
"""Def a text file-reading function """


def read_file(filename=""):
    """Func that reads a txt file and print in stdout
    Args:
        filename(str): name of the file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
