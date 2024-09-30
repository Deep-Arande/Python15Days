# Implement a program that uses a Circle class to calculate 
# the area and circumference of multiple circles


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

# Function to calculate for multiple circles
def process_circles():
    circles = []  # List to store Circle objects

    # Input number of circles
    num_circles = int(input("Enter the number of circles: "))

    # Input radius for each circle and calculate area & circumference
    for i in range(num_circles):
        radius = float(input(f"Enter the radius of circle {i+1}: "))
        circle = Circle(radius)
        circles.append(circle)

    # Display the area and circumference for each circle
    for i, circle in enumerate(circles, start=1):
        area = circle.calculate_area()
        circumference = circle.calculate_circumference()
        print(f"\nCircle {i}:")
        print(f"Radius: {circle.radius}")
        print(f"Area: {area:.2f}")
        print(f"Circumference: {circumference:.2f}")

# Example usage
if __name__ == "__main__":
    process_circles()
