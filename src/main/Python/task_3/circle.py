import math

from i_shape_2D import IShape2D


class Circle(IShape2D):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 2 * math.pi * self.radius
