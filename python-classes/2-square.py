#!/usr/bin/python3
"""Define a Square class."""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square's side.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the new square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Square are values

        """
        return self.__size**2
