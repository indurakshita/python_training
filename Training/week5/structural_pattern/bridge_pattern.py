class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass


class Color:
    def fill_color(self):
        pass


class RedColor(Color):
    def fill_color(self):
        return "Red"


class GreenColor(Color):
    def fill_color(self):
        return "Green"


class Circle(Shape):
    def draw(self):
        return f"Drawing a Circle with {self.color.fill_color()} color"


class Square(Shape):
    def draw(self):
        return f"Drawing a Square with {self.color.fill_color()} color"


red_color = RedColor()
green_color = GreenColor()

circle = Circle(red_color)
square = Square(green_color)

print(circle.draw())
print(square.draw())