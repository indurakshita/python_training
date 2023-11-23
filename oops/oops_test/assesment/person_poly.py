'''Question 8: Create a class Person with a method greet(). 
Then, create subclasses Teacher and Student that override the greet() method to provide their own greetings. 
Write a function that greets a list of people.'''

# class Person:
#     def __init__(self,qual):
        
#         self.qual = qual
        
#     def greet1(self):

#         if self.__class__.__name__ == "Teacher":
                
#                 print(f'Hello!,I am {self.name}\n I am {self.qual} teacher')
#         else:
#                 print(f'Hello!,I am {self.name}\n I am {self.qual} student')
            
# class Teacher(Person):
#     def __init__(self,qual,name):
#         super().__init__(qual)
#         self.name = name
           
#     def greet(self):
#         return self.name
    
# class Student(Teacher,Person):

#     def greet(self):
#         return self.name
  
# obj1 = Teacher(name="Indhu",qual="Maths")
# obj2 = Student(name="Rakshita",qual="12th") 
# obj1.greet1()
# obj2.greet1()

        
# def func(l_people):
#     for people in l_people:
#         print(f"      Hello! I am {people.name}\nI am {people.__class__.__name__}")

# l_people = [obj1,obj2]
# func(l_people)
