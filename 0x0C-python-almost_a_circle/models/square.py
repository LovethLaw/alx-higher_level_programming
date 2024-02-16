#!/usr/bin/python3
"""A class that inherits from the Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class a grandchild to base and a child to rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square class constructor"""
        super().__init__(id=id, width=size, height=size, x=x, y=y)
        self.size = size

    def __str__(self):
        """String representation"""
        return "[{}] ({}) {}/{} - {}".format(
            'Square',
            self.id,
            self.x,
            self.y,
            self.size
        )

    @property
    def size(self):
        """returns the size"""
        return self.__width

    @size.setter
    def size(self, width_value):
        """_summary_

        Args:
            width_value (int): interger value of size

        Raises:
            TypeError:  if an int isnt entred
            ValueError:if size value is lesser than 0
        """
        if not isinstance(width_value, int):
            raise TypeError("width must be an integer")
        elif width_value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width_value

    def update(self, *args, **kwargs):
        """updates the instances attributes
        """
        if args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id, self.size = args
            elif len(args) == 3:
                self.id, self.size, self.x = args
            elif len(args) == 4:
                self.id, self.size, self.x, self.y = args
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """_summary_

        Returns:
            dict_: a dict of all instnces attribuues
        """
        diction = dict()
        diction['id'] = self.id
        diction['size'] = self.size
        diction['x'] = self.x
        diction['y'] = self.y
        return diction
