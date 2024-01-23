#!/usr/bin/python3
"""Module defines the class Square with some attributes"""


class Square:
    """Defines a square.

    Attributes:
        __size (float or int): The size of the square.
    """

    def __init__(self, size=0):
        """Initialize the Square instance.

        Args:
            size (float or int): The size of the square. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (float or int): The size to set.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Define the equality comparison."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """Define the not equal comparison."""
        result = self.__eq__(other)
        if result is not NotImplemented:
            return not result
        return NotImplemented

    def __lt__(self, other):
        """Define the less than comparison."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """Define the less than or equal comparison."""
        result = self.__lt__(other) or self.__eq__(other)
        if result is not NotImplemented:
            return result
        return NotImplemented

    def __gt__(self, other):
        """Define the greater than comparison."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """Define the greater than or equal comparison."""
        result = self.__gt__(other) or self.__eq__(other)
        if result is not NotImplemented:
            return result
        return NotImplemented
