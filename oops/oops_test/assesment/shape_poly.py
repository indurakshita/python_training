# Polymorphism
'''Question 6: Create a class Shape with a method area(). 
Then, create subclasses Rectangle and Circle that override the area() method to calculate their respective areas. 
Write a function that calculates the total area of a list of shapes, regardless of their specific types.'''


# class Shape:
#     def __init__(self):
#         self.__pi = 3.14

#     @property
#     def hide(self):
#         return self.__pi
        
# class Rectangle(Shape):

#     def __init__(self,w,h):
#         super().__init__()
#         self.w = w
#         self.h = h
    
#     def area(self):
#         return  self.w * self.h
        
# class Circle(Shape):
#     def __init__(self,radius):
#         super().__init__()
#         self.radius = radius
        
#     def area(self):
#         return  self.hide * self.radius **2

# rec = Rectangle(w=5,h=2)
# print(f"area of the Rectangle:{rec.area()}")
# print(f"pi value is:{rec.hide}")
# cir = Circle(2)
# print(f"area of the circle:{cir.area()}")

# def total_area(l_shapes):
#     index = 0
#     tot_area = 0
#     while index < len(l_shapes):
#         tot_area+= l_shapes[index].area()
#         index+=1
#     print(f"total area of the shape is:{tot_area:.2f}")

# l_shapes = [rec,cir]
# total_area(l_shapes)


''''Question 9: Create a class Shape with a method description(). 
Then, create subclasses Rectangle and Circle that override the description() method to provide a 
description of the shape. 
Write a function that generates descriptions for a list of shapes.'''

# class Shape:
    
#     def description():
#         return "shape"
    
# class Rectangle(Shape):

#     def __init__(self,height,width):
#         self.height = height
#         self.width = width

#     def description(self):
#         return f"The rectangle height is:{self.height},and Width:{self.width}"

# class Circle(Shape):

#     def __init__(self,radius): 
#         self.radius = radius

#     def description(self):
#         return f"The Circle is radius:{self.radius}"

# def func(l_shapes):
    
#     index =0
#     while index _shapes[index])
#         index+=1
# l_shapes = [Rectangle(2,width = 5).description(),Circle(radius = 3).description()]
# func(l_shapes)
