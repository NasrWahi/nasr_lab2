# nasr_lab2

# Lab 2 - Classes (Circle & Rectangle)

This lab has Circle and Rectangle classes, working with geometric shapes

# Files
- 'circle.py'
- 'rectangle.py'
- 'testing.py'
- 'manual_tests.ipynb'
- 'uml.png'

# What the classes can do:
- Area and perimeter (read-only)
- Move shapes around with translate()
- Compare shapes ==, <, >, etc
- Check to see if circle is for instance unit circle or rectangle is square
- Error messages if it's wrong

# Examples
from circle import Circle
from rectangle import Rectangle

circle = Circle(0, 0, 1)
rectangle = Rectangle(0, 0, 2, 3)

circle.translate(5, 3)
print(circle.area)
print(circle == rectangle)

---

python testing.py