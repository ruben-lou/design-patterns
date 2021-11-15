class DrawingAPIOne(object):
    """Implementation-specific abstraction: concrete class one"""

    @staticmethod
    def draw_circle(x, y, radius):
        print("API 1 is drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))


class DrawingAPITwo(object):
    """Implementation-specific abstraction: concrete class two"""

    @staticmethod
    def draw_circle(x, y, radius):
        print("API 2 is drawing a circle at ({}, {} with radius {}!)".format(x, y, radius))

class Circle(object):
    """Implementation-independent abstraction"""

    def __init__(self, x, y, radius, drawing_api):
        """Initialise the necessary attributes"""

        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """Implementation-specific abstraction taken care of"""

        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        """Implementation-independent"""
        self._radius *= percent

# Build the first Circle object using API One
circle1 = Circle(1, 2, 3, DrawingAPIOne())
# Draw circle
circle1.draw()

# Build the second Circle object using API Two
circle2 = Circle(2, 3, 4, DrawingAPITwo())
# Draws circle
circle2.draw()
