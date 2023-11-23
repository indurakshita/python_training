class ShapeFactory:
    def create_circle(self):
        pass
    
    def create_rectangle(self):
        pass


class RoundedShapeFactory(ShapeFactory):
    def create_circle(self):
        return RoundedCircle()
    
    def create_rectangle(self):
        return RoundedRectangle()


class RegularShapeFactory(ShapeFactory):
    def create_circle(self):
        return RegularCircle()
    
    def create_rectangle(self):
        return RegularRectangle()


class Circle:
    def draw(self):
        pass


class RoundedCircle(Circle):
    def draw(self):
        return "Drawing a rounded circle"


class RegularCircle(Circle):
    def draw(self):
        return "Drawing a regular circle"


class Rectangle:
    def draw(self):
        pass


class RoundedRectangle(Rectangle):
    def draw(self):
        return "Drawing a rounded rectangle"


class RegularRectangle(Rectangle):
    def draw(self):
        return "Drawing a regular rectangle"


def draw_shapes(factory):
    circle = factory.create_circle()
    rectangle = factory.create_rectangle()
    print(circle.draw())
    print(rectangle.draw())

rounded_factory = RoundedShapeFactory()
regular_factory = RegularShapeFactory()

print("Drawing shapes with RoundedShapeFactory:")
draw_shapes(rounded_factory)

print("\nDrawing shapes with RegularShapeFactory:")
draw_shapes(regular_factory)