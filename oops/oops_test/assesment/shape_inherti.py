'''Question 2: Create a base class Shape with a method area() and then create two subclasses, 
Rectangle and Circle, that inherit from Shape. 
Implement the area method in each subclass to calculate their respective areas.'''

# class Shape:
       
#     def area(self):
#         raise ValueError("should give area")
    

# class Rectangle(Shape):

#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
        
#     def area(self):
#         self.rec_area = self.width * self.height
#         return f"Area of the rectangle:{self.rec_area}"


# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#         self.pi =22/7

#     def area(self):
#         self.cir_area = self.pi * self.radius **2
#         return f"Area of the circle:{self.cir_area}"

# cir = Circle(3)
# print(cir.area())

# rec = Rectangle(5,2)
# print(rec.area())




# logic 2:

class Shape:
    def __init__(self,*args,**kwargs):  
        self.args = args #tuple
        self.kwargs = kwargs #dict
    
    def area(self):
        # keys = tuple(self.kwargs.keys())
        # if "width" in keys and "height" in keys:
        #     return self.kwargs.get(keys[0]) * self.kwargs.get(keys[1])
        # elif "radius" in keys:
        #     return 3.14 * (self.kwargs.get(keys[0]) ** 2)

        # if self.kwargs.grt("shape") == "rectangle":
        #     return self.kwargs.get("width") * self.kwargs.get("height")
        # elif self.kwargs.grt("shape") == "circle":
        #     return 3.14 * (self.kwargs.get("radius") ** 2)

        mapping = {
            self.kwargs.get("shape") == "rectangle":  self.kwargs.get("width",0) * self.kwargs.get("height",0),
            self.kwargs.get("shape") == "circle": 3.14 * (self.kwargs.get("radius",0) ** 2)
        }

        return mapping[True]

    

class Rectangle(Shape):
    def __init__(self,width, height):
        super().__init__(width=width, height=height,shape="rectangle")

    
class Circle(Shape):
    def __init__(self,radius):
        super().__init__(radius=radius, shape="circle")



# shape = Rectangle(5,2)
# shape = Circle(3)
# area = shape.area()
# print(area)
'------------------------------------------------------------------------------------------------'
'''child will then use this attribute sides in theri classes'''
class Shape:
    sides = 0

class Circle(Shape):
    c_sides  = 2
    def __init__(self,name):
        self.sides = self.c_sides
        self.name = name

class Square(Shape):
    s_sides = 4
    def __init__(self,name):
        self.sides = self.s_sides
        self.name = name


if __name__ == "__main__":
    shape = Shape()

    circle = Circle("circle1")
    square = Square("square 1")

    print(shape.sides)
    print(circle.sides)
    print(square.sides)

