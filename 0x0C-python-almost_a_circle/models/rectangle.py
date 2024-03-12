#!/usr/bin/python3
"""A class that inherits from the base class"""
from models.base import Base


class Rectangle(Base):
    """A rectangle class

    Args:
        Base (ParentClass): instantize an id
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """an attribute instance
            Args:
            width (int): size width
            height (int): size height_
            x (int): x_axis value . Defaults to 0.
            y (int): y_axis value . Defaults to 0.
            id (int): parent id. Defaults to None.

        Raises:
            TypeError: when either of the attribues are not of type int
            ValueError: if value is lesser than 0
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @ property
    def width(self):
        """ Returns the width

        Returns:
            (private attribute): the private width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width of the rectangle

        Args:
            width (int):
        Raises:
            ValueError: width must be > 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @ property
    def height(self):
        """ Returns the height

        Returns:
            int : height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """ Height Setter

        Args:
            height (int): the value of height you want to assign/change

        Raises:
            ValueError: height must be > 0
        """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """Returns the Value of x

        Returns:
            (private attribute): the private variable x
        """
        return self.__x

    @x.setter
    def x(self, x_value):
        """Sets the value of x

        Args:
            x_value (int): values to assign to x

        Raises:
            ValueError: x must be >= 0
        """

        if not isinstance(x_value, int):
            raise TypeError("x must be an integer")
        elif x_value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x_value

    @property
    def y(self):
        """used to get the value ox y

        Returns:
            (private attribute): returns the value of y
        """
        return self.__y

    @y.setter
    def y(self, y_value):
        """_summary_

        Args:
            y_value (int): value to set y

        Raises:
            TypeError: y  must be an integer"
            ValueError: y must be >= 0
        """
        if not isinstance(y_value, int):
            raise TypeError("y must be an integer")
        elif y_value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y_value

    def area(self):
        """_summary_

        Returns:
            int: return the area of a rectangle
        """
        return self.__width * self.__height

    def display(self):
        """prints # in range of height
        """
        out = ('\n' * self.__y)

        for i in range(self.__height):
            out += ' ' * self.__x + '#' * self.__width + '\n'

        print(out, end='')

    # returns the string representation

    def __str__(self):
        """Rectangle Representation

        Returns:
            str : returns the string reperesentation
            of the rectangle class
        """
        return "[{}] ({}) {}/{} - {}/{}". format(
            "Rectangle", self.id, self.__x, self.__y,
            self.__width, self.__height
        )

    # updating the rectangles
    def update(self, *args, **kwargs):
        """ Update Each attributes with new values
            with *args pr **kwargs
        """

        if args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id, self.__width = args
            elif len(args) == 3:
                self.id, self.__width, self.__height = args
            elif len(args) == 4:
                self.id, self.__width, self.__height, self.__x = args
            elif len(args) == 5:
                self.id, self.__width, self.__height, self.__x, self.__y = args
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """Creates a dictionary"""
        diction = dict()
        diction['x'] = self.__x
        diction['y'] = self.__y
        diction['id'] = self.id
        diction['height'] = self.__height
        diction['width'] = self.__width
        return diction
