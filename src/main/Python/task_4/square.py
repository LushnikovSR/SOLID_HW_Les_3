from shape import Shape


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def set_side_length(self, side_length):
        self.side_length = side_length

    def area(self, side_length):
        return side_length * side_length
