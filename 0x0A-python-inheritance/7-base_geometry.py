#!/usr/bin/python3
"""This Module is on Geometry"""

class BaseGeometry:
    """An empty class BaseGeometry"""
    def area(self):
        """Raises and exception when not implemented"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """A function That validates if a value is of type int if not raise an Exception
            Exception:
                TypeError: if values is not an int
                ValueError: if Value is less or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
