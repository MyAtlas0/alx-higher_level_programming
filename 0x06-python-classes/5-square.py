#!/usr/bin/python3

"""Define a Class Square"""

class Square:
    """Represents a Square"""

    def __init__(self, size=0):
        """Initalize a New Sqaure.

        Args:
            size (int): The size of the new Sqaure.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the Current size of the Square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the Current area of the Square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the Square with the # Character"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
