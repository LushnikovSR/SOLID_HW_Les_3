from i_shape_2D import IShape2D
from i_shape_3D import IShape3D


class Cube(IShape2D, IShape3D):
    def __init__(self, edge):
        self.edge = edge

    def area(self):
        return 6 * self.edge * self.edge

    def volume(self):
        return self.edge * self.edge * self.edge
