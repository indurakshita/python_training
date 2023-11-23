'''Question 3: Create a class Person with attributes name and age. 
Then, create a subclass Student that inherits from Person and has an additional attribute student_id. 
Implement a method to display the student's details.'''

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# class Student(Person):
#     def __init__(self,name,age):
#         super().__init__(name,age)
    
#     @property
#     def stud_id(self):
#         return self.name[:2] + str(self.age)

#     def display(self):
#         return f'Student name is: {self.name}\nage is: {self.age}\nstudent_id: {self.stud_id}'

# stud = Student("Rani",27)
# print(stud.display())
