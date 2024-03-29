#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    lines_to_write = []

    with open(filename, "r") as file:
        for line in file:
            lines_to_write.append(line)
            if search_string in line:
                lines_to_write.append(new_string)

    with open(filename, "w") as file:
        file.writelines(lines_to_write)
