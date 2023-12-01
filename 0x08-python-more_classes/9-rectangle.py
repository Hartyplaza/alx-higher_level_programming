#!/usr/bin/python3
""" A Rectangle class """


class Rectangle:
    """ defines a rectangle """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    """ width setter """

    @property
    def width(self):
        return self.__width

    """ width getter """

    @width.setter
    def width(self, value):

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ height setter """

    @property
    def height(self):
        return self.__height

    """ height getter """

    @height.setter
    def height(self, value):

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ Area of Rectangle"""

    def area(self):
        return self.__height * self.__width

    """ Perimeter of a Rectangle"""

    def perimeter(self):
        if self.width == 0:
            return 0
        if self.height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    """ String representation"""

    def __str__(self):
        empty_string = ""

        if self.__width == 0 or self.__height == 0:
            return empty_string

        r = (((str(self.print_symbol) * self.width) + "\n") * self.height)[:-1]
        return r

    """ string representation of the rectangle"""

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    """ Deleting an instance """

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    """ Returns the biggest rectangle based on the area """
    def bigger_or_equal(rect_1, rect_2):

        if isinstance(rect_1, Rectangle) is not True:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is not True:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1

        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle instance """
        return cls(size, size)
