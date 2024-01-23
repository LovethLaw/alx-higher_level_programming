#!/usr/bin/python3
import math


class MagicClass:
    """A class with magical properties.

    Attributes:
        __radius (float or int): The radius of the magical circle.
    """

    def __init__(self, radius=0):
        """Initialize the MagicClass instance with a radius.

        Args:
            radius (float or int): D radius of magical circle. Default is 0.
                It must be a number (float or integer).

        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0

        if type(radius) not in (int, float):
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """Calculate and return the area of the magical circle.

        Returns:
            float: The area of the magical circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the magical circle.

        Returns:
            float: The circumference of the magical circle.
        """
        return 2 * math.pi * self.__radius
