"""
Open and clase principle (OCP)
A class should be closed to change but open to modification
"""

"""Wrong implementation"""

"""
class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape = shape_type
        self.values = kwargs

    def calculates_area(self):
        if self.shape == 'rectangle':
            return self.values['width'] * self.values['height']
        elif self.shape == 'square':
            return self.values['width'] ** 2
        else:
            print("No shape passed")

"""
"""Correct implementation"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    def __init__(self, side):
        self.side = side

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, side, height):
        super().__init__(side)
        self.height = height

    def calculate_area(self):
        return self.side * self.height


class Square(Shape):

    def calculate_area(self):
        return self.side ** 2


class Circle(Shape):

    def calculate_area(self):
        return pi * self.side ** 2


x = Rectangle(side=6, height=5)
print(x.calculate_area())
