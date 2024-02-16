#!/usr/bin/python3
"""A rectangle module that prints out a rectangle"""
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
        super().__init__(id)
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

    # Width property
    @property
    def width(self):
        """Returns the value of width

        Returns:
            int : Value to be returned
        """
        return self.__width

    # width setter
    @width.setter
    def width(self, width):
        """Sets and Validates the Value of width and check it instance

        Args:
            height (int): The new value of width

        Raises:
            TypeError: return if width is not of type int
            ValueError: returns if width is lesser than 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    # height getter
    @property
    def height(self):
        """Height value

        Returns:
            int : Returns the value of height
        """
        return self.__height

    # height Setter
    @height.setter
    def height(self, height):
        """Sets and Validates the Value of height and check it instance

        Args:
            height (int): The new value of height

        Raises:
            TypeError: return if height is not of type int
            ValueError: if height is lesser than 0
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    # x getter
    @property
    def x(self):
        """Returns the value of x

        Returns:
            int : returns an integer
        """
        return self.__x

    # x Setter
    @x.setter
    def x(self, x):
        """Validates the setting of the x_axis

        Args:
            x (int): x value to be assigned

        Raises:
            TypeError: return if x is not of txpe int
            ValueError: if x is lesser than 0
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x <= 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    # y getter
    @property
    def y(self):
        """Returns the value of y

        Returns:
            int : returns an integer
        """
        return self.__y

    # y Setter
    @y.setter
    def y(self, y):
        """Validates the setting of the y_axis

        Args:
            y (int): Y value to be assigned

        Raises:
            TypeError: return if Y is not of type int
            ValueError: if y is lesser than 0
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y <= 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    # Get the area of a triangle
    def area(self):
        """Gets the area of the rectangle

        Returns:
            the calculated area of a Rectangle
        """
        return self.__width * self.__height

    # prints rectangle in instance of '#'
    def display(self):
        """prints # in range of height
        """
        nill = ('\n' * self.__y)
        for _ in range(self.__height):
            nill += ' ' * self.__x + "#" * self.__width + '\n'
        print(nill, end="")

    def __str__(self):
        """Rectangle Representation

        Returns:
            str : returns the string reperesentation
            of the rectangle class
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__,
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height,
        )

    # Assings each argument of each variable
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
            elif len(args) > 5:
                # handle case when args is more than 5
                pass
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """conversts a json string to a python dictionary
        retuns a new dict
        """
        new_dict = dict()
        for key, value in self.__dict__.items():
            if key.startswith("_Rectangle__"):
                key = key[len("_Rectangle__"):]
                new_dict[key] = value
        return new_dict
