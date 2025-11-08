# \n=== for cleaner look, recommended by Copilot, pseudo-code also changed

# Import our shape classes
from circle import Circle
from rectangle import Rectangle

print("=== TEST 1: Basic Shape Creation ===")
# Create a unit circle at center (0,0) with radius 1
circle1 = Circle(x=0, y=0, radius=1)

# Create another circle at center (1,1) with radius 1
circle2 = Circle(x=1, y=1, radius=1)

# Create a square at center (0,0) with width 1 and height 1
rectangle = Rectangle(x=0, y=0, width=1, height=1)

print("Circle 1 position: (", circle1.x, ",", circle1.y, ") with radius", circle1.radius)
print("Circle 2 position: (", circle2.x, ",", circle2.y, ") with radius", circle2.radius)
print("Rectangle position: (", rectangle.x, ",", rectangle.y, ") size", rectangle.width, "x", rectangle.height)


print("\n=== TEST 2: Equality Comparisons ===")
# Test if two circles have same area (both have radius 1, so both have same area)
print("circle1 == circle2?", circle1 == circle2)  # Should be True

# Test if circle and rectangle have same area (circle area ≈ 3.14, rectangle area = 1)
print("circle2 == rectangle?", circle2 == rectangle)  # Should be False


print("\n=== TEST 3: Translation (Moving Shapes) ===")
# Show circle1 position before moving
print("Before moving - Circle 1 at: (", circle1.x, ",", circle1.y, ")")

# Move circle1 by 5 units in x-direction and 3 units in y-direction
circle1.translate(5, 3)

# Show circle1 position after moving
print("After moving - Circle 1 at: (", circle1.x, ",", circle1.y, ")")
print(f"Movement: (0,0) → (5,3) = moved right 5, up 3")


print("\n=== TEST 4: Error Handling ===")
# Try to move with text instead of numbers - this should cause an error
print("Trying to move with text instead of numbers...")
try:
    circle1.translate("THREE", 5)  # This will fail because "THREE" is text
except TypeError as error:
    print("Caught error:", error)  # Show the error message


print("\n=== TEST 5: Size Comparisons ===")
# Create a larger circle with radius 3 at center (0,0)
circle3 = Circle(radius=3)

print("Circle 3 position: (", circle3.x, ",", circle3.y, ") with radius", circle3.radius)
print("Circle 1 position: (", circle1.x, ",", circle1.y, ") with radius", circle1.radius)

# Check if circle3 is bigger than or equal to circle1 (radius 3 vs radius 1)
print("circle3 >= circle1?", circle3 >= circle1)  # Should be True


print("\n=== TEST 6: Creation Error Handling ===")
# Try to create rectangle with text instead of numbers for height
print("Trying to create rectangle with text height...")
try:
    rectangle2 = Rectangle(width=3, height="5")  # This will fail because "5" is text
except TypeError as error:
    print("Caught error:", error)  # Show the error message


print("\n=== TEST 7: Special Shape Detection ===")
# Check if a circle is a unit circle (radius 1 at origin)
unit_circle = Circle(0, 0, 1)
print("Is circle at (0,0) with radius 1 a unit circle?", unit_circle.is_unit_circle())

# Check if a rectangle is a square (equal width and height)
square = Rectangle(0, 0, 2, 2)
print("Is rectangle 2x2 a square?", square.is_square())
print("Is rectangle 1x1 a square?", rectangle.is_square())


print("\n=== TEST 8: Movement Tracking ===")
# Create a test circle and show how it moves
test_circle = Circle(0, 0, 2)
print("Starting position: (", test_circle.x, ",", test_circle.y, ")")

# Move the circle
test_circle.translate(3, 4)
print("After moving right 3, up 4: (", test_circle.x, ",", test_circle.y, ")")
print(f"Movement: (0,0) → (3,4) = total move of 3 right, 4 up")


print("\n=== TEST 9: String Representations ===")
# Show how the shapes look when printed
print("Circle description:", str(circle1))
print("Circle technical details:", repr(circle1))
print("Rectangle description:", str(rectangle))
print("Rectangle technical details:", repr(rectangle))


print("\n=== TEST 10: Area and Perimeter Calculations ===")
# Show area and perimeter calculations
print("Circle area:", round(circle1.area, 2))
print("Circle perimeter:", round(circle1.perimeter, 2))
print("Rectangle area:", rectangle.area)
print("Rectangle perimeter:", rectangle.perimeter)


print("\n=== TEST 11: Multiple Movements ===")
# Test moving a shape multiple times
test_rect = Rectangle(10, 10, 2, 3)
print("Rectangle starts at: (", test_rect.x, ",", test_rect.y, ")")

test_rect.translate(2, -1)  # Move right 2, down 1
print("After first move: (", test_rect.x, ",", test_rect.y, ")")

test_rect.translate(-5, 3)  # Move left 5, up 3
print("After second move: (", test_rect.x, ",", test_rect.y, ")")