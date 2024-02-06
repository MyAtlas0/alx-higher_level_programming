#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """An inherited list class with a method for printing sorted elements."""

    def print_sorted(self):
        """Print the list in sorted ascending order.

        Raises:
            TypeError: If the list contains mixed data types.
        """
        try:
            print(sorted(self))
        except TypeError:
            raise TypeError("Unable to sort the list due to mixed data types")
