import math

class Rectangle:
    def __init__(self, x=0, y=0, width=1, height=1):
        self._validate_numeric(x, "x")
        self._validate_numeric(y, "y")
        self._validate_numeric(width, "width")
        self._validate_numeric(height, "height")

        if width <= 0:
            raise ValueError("Width must be positive")
        if height <= 0:
            raise ValueError("Height must be positive")
        
        self._x = float(x)
        self._y = float(y)
        self._width = float(width)
        self._height = float(height)

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

    def translate(self, dx, dy):
        self._validate_numeric(dx, "dx")
        self._validate_numeric(dy, "dy")
        self._x += dx
        self._y += dy

    def is_square(self):
        return math.isclose(self._width, self._height)

    def _validate_numeric(self, value, name):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number, got {type(value).__name__}")

    # Operator overloads
    def __eq__(self, other):
        return math.isclose(self.area, other.area)

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __le__(self, other):
        return self.area <= other.area

    def __ge__(self, other):
        return self.area >= other.area

    def __repr__(self):
        return f"Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height})"

    def __str__(self):
        shape_type = "Square" if self.is_square() else "Rectangle"
        return f"{shape_type} at ({self.x}, {self.y}) with area {self.area:.2f}"