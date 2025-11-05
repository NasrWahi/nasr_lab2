import math 

class Circle:
    def __init__(self, x=0, y=0, radius=1):
        self._validate_numeric(x, "x")
        self._validate_numeric(y, "y")
        self._validate_numeric(radius, "radius")

        if radius <= 0:
            raise ValueError("Radius must be positive")
        
        self._x = float(x)
        self._y = float(y)
        self._radius = float(radius)

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return math.pi * self._radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self._radius

    def translate(self, dx, dy):
        self._validate_numeric(dx, "dx")
        self._validate_numeric(dy, "dy")
        self._x += dx
        self._y += dy

    def is_unit_circle(self):
        return math.isclose(self._radius, 1) and math.isclose(self._x, 0) and math.isclose(self._y, 0)

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
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"

    def __str__(self):
        unit_status = " (unit circle)" if self.is_unit_circle() else ""
        return f"Circle at ({self.x}, {self.y}) with radius {self.radius}{unit_status}"