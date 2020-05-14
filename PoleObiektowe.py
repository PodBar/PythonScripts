


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def count_surface_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, sideLength):
        super().__init__(sideLength, sideLength)



class Cube():
    def __init__(self, square: Square):
        self.square = square

    def count_surface_area(self):
        return self.square.count_surface_area() * 6

    def count_volume(self):
        return self.square.count_surface_area() * self.square.height


class Cuboid():
    def __init__(self, figure, height):
        self.base = figure
        self.height = height

    def count_volume(self):
        return self.base.count_surface_area() * self.height

    def count_surface_area(self):
        return 2 * self.base.count_surface_area() + 2 * self.base.width * self.height + 2 * self.base.height * self.height


class Cube(Cuboid):
    def __init__(self, figure: Square):
        super().__init__(figure, figure.height)


cube = Cube(Square(4))

print(cube.count_volume())
