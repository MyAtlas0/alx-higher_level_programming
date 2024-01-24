#!/usr/bin/python3

"""Define a MagicClass matching exactly a bytecode provided by Holberton."""

import math

class MagicClass:
    """Represent a circle."""

    def __init__(self, radius: float = 0):
        """Initialize a MagicClass.

        Args:
            radius (float): The radius of the new MagicClass.
        Raises:
            TypeError: If the provided radius is not a number.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    @property
    def radius(self) -> float:
        """Get the radius of the MagicClass."""
        return self.__radius

    def area(self) -> float:
        """Calculate and return the area of the MagicClass."""
        return self.__radius ** 2 * math.pi

    def circumference(self) -> float:
        """Calculate and return the circumference of the MagicClass."""
        return 2 * math.pi * self.__radius
