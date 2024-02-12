#!/usr/bin/python3
"""A Square module that inherits from the rectangle """

Rectangle = __import__("rectangle").Rectangle


class Square(Rectangle):
    def __init__(self, size: int, x=0, y=0, id=None):
        """intilizing a square class

        Args:
            size (int): size of the square
            x (int): x_axis of the parent class. Defaults to 0.
            y (int): y_axis of the parent class. Defaults to 0.
            id (int): id of the parent class. Defaults to None.
        """
        super().__init__(id=id, x=x, y=y, width=size, height=size)
        self.size = size

    def __str__(self):
        """overiding the parent method of __str__
        """
        return "[{}] ({}) {}/{} {}".format(
            self.__class__.__name__,  # uses the square class name
            self.id,
            self.x,
            self.y,
            self.size
        )

    @property
    def size(self):
        """Returns the size

        Returns:
            _type_: _description_
        """
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be greater than 0")
        else:
            self._size = value

    def update(self, *args, **kwargs):
        """update the new attributes
        """
        if args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id, self._size = args
            elif len(args) == 3:
                self.id, self.size, self.x = args
            elif len(args) == 4:
                self.id, self.size, self.x, self.y = args
            elif len(args) > 4:
                # handle case when args is more than 5
                pass
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """makes a dictionary

        Returns:
            dict: returns a dictionary containig the various keys
        """
        new_dict = dict()
        new_dict["id"] = self.id
        new_dict['size'] = self.size
        new_dict['x'] = self.x
        new_dict['y'] = self.y
        return new_dict
