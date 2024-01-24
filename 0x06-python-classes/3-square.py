#!/usr/bin/python3

""" Define a Class Square """

class Square:
    """ Represents a Square """

    def __init__(self, size=0):
        """ Initalize a New Sqaure.

        Args:
            size (int): The size of the new Sqaure.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Return the Current area of the Square """
        return (self.__size * self.__size)
