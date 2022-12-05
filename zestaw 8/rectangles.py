from points import Point


def from_points(points):
    if not (isinstance(points, list) or isinstance(points, tuple)):
        raise TypeError("Nie podano listy lub kroki")
    if len(points) != 2:
        raise ValueError("zła ilość podanych punktów")
    return Rectangle(points[0].x, points[0].y, points[1].x, points[1].y)


class Rectangle:

    @property
    def top(self):
        return self.pt2.y

    @top.setter
    def top(self, value):
        raise PermissionError("nie można zmienić tego pola manualnie")

    @property
    def bottom(self):
        return self.pt1.y

    @bottom.setter
    def bottom(self, value):
        raise PermissionError("nie można zmienić tego pola manualnie")

    @property
    def left(self):
        return self.pt1.x

    @left.setter
    def left(self, value):
        raise PermissionError("nie można zmienić tego pola manualnie")

    @property
    def right(self):
        return self.pt2.x

    @right.setter
    def right(self, value):
        raise PermissionError("nie można zmienić tego pola manualnie")

    @property
    def width(self):
        return abs(self.pt1.x - self.pt2.x)

    @width.setter
    def width(self, value):
        raise PermissionError("nie można zmienić tego pola manualnie")

    @property
    def height(self):
        return abs(self.pt1.y - self.pt2.y)

    @height.setter
    def height(self, value):
        raise PermissionError("nie można zmienić tego pola manualnie")

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):  # "[(x1, y1), (x2, y2)]"
        return "[" + str(self.pt1) + ", " + str(self.pt2) + "]"

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(self.pt2.y) + ")"

    def __eq__(self, other):  # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):  # obsługa rect1 != rect2
        return not self == other

    def center(self):  # zwraca środek prostokąta
        x = (self.pt1.x + self.pt2.x) / 2
        y = (self.pt1.y + self.pt2.y) / 2
        return Point(x, y)

    def area(self):  # pole powierzchni
        x = abs(self.pt1.x - self.pt2.x)
        y = abs(self.pt1.y - self.pt2.y)
        return x * y

    def move(self, x, y):  # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt2.x += x
        self.pt1.y += y
        self.pt2.y += y
        return self

    @property
    def topleft(self):
        return Point(self.pt1.x, self.pt2.y)

    @topleft.setter
    def topleft(self, value):
        raise PermissionError("nie można zmienić tego pola manualnie")

    @property
    def bottomleft(self):
        return self.pt1

    @bottomleft.setter
    def bottomleft(self, value):
        raise PermissionError("nie można zmienić tego pola manualnie")

    @property
    def topright(self):
        return self.pt2

    @topright.setter
    def topright(self, value):
        raise PermissionError("nie można zmienić tego pola manualnie")

    @property
    def bottomright(self):
        return Point(self.pt2.x, self.pt1.y)

    @bottomright.setter
    def bottomright(self, value):
        raise PermissionError("nie można zmienić tego pola manualnie")
