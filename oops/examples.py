# class MyClass:
#     class_var = 42

#     def __init__(self):
#         self.instance_var = 10

#     def instance_method(self):
#         print("hello")

# print("Namespace of MyClass:")
# print(MyClass.instance_method)
# obj=MyClass()
# obj.instance_method()
'---------------------------------------------------------------------------------------------------------'

# '''Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and 
# emp_department and methods like calculate_emp_salary,and print_employee_details'''

class Employee:
    overtime=0
    w_hours=0
    salary=0
   
    print("Employee Details".center(100))

    def __init__(self,emp_id,emp_name,emp_depart):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_depart = emp_depart
        

    def emp_salary(self):
        

        if self.emp_depart.lower() == "developer":
            self.salary = 15000
            return self.salary
        elif self.emp_depart.lower() == "hr":
            self.salary = 20000
            return self.salary
        elif self.emp_depart.lower() == "manager":
            self.salary = 30000
            return self.salary
        else:
            self.salary = 10000
            return self.salary
       
    
        
    def __str__(self):
        
        return f"Emp_id:{self.emp_id}\nEmp_name:{self.emp_name}\nEmp_depart:{self.emp_depart}\nEmp_salary:{self.salary}\n"
       
        

emp1 = Employee(emp_name="Indhu",emp_id="ONE1001",emp_depart="Developer")
emp2 = Employee(emp_name="Chandru",emp_id="ONE1002",emp_depart="HR")
emp3 = Employee(emp_name="rani",emp_id="ONE1003",emp_depart="admin")
emp1.emp_salary()
print(emp1)

emp2.emp_salary()
print(emp2)
emp3.emp_salary()
print(emp3)
'-------------------------------------------------------------------------------------------------'
# Inheritance:

'''Create a base class Animal with attributes name and sound. Create two subclasses, Dog and Cat, 
that inherit from Animal and add methods for making their respective sounds.'''

# logic 1:

# class Animals:
#     def __init__(self,name,sound):
#         self.name = name
#         self.sound = sound
    
        

# class Dog(Animals):
#     def __str__(self):
#         return f"{self.name} sound is {self.sound}"

# class Cat(Animals):
#     def __str__(self):
#         return f"{self.name} sound is {self.sound}"
    
# dog = Dog("dog","barks")
# print(dog)
# cat = Cat("cat","meow")
# print(cat)
'------------------------------------------------------------------------------'

# logic 2:
# class Animals:
#     def __init__(self,name,sound):
#         self.name = name
#         self.sound = sound
#     def __str__(self):
#         return f"{self.name} sound is {self.sound}"

# class Dog(Animals):
#     def __init__(self,name,sound):
#         # Animals.__init__(self,name,sound)or 
#         super().__init__(name,sound)
    

# class Cat(Animals):
#     def __init__(self,name,sound):
#         # Animals.__init__(self,name,sound)or 
#         super().__init__(name,sound)  
#     def __str__(self):
#         return f"{self.name} sound is {self.sound}"

# d = Dog("dog","barks")
# print(d)

# c = Cat("cat","meow") 
# print(c)
        
        




