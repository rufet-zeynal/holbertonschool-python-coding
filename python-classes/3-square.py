#!/usr/bin/python3
"""
Defining Class Square
"""
class Square:
    """
    Creating Square class
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.
        """
        self.size = size
    @property
    def size(self):
        """
        Retrieve the size
        """
        return self.__size
    @size.setter
    def size(self, value):
        """
        Setter to set the size
        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """
        Area of the square
        """
        return self.__size **2
