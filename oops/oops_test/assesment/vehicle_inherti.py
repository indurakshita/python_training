'''Question 1: Create a class Vehicle with attributes make and model. 
# Then, create a subclass Car that inherits from Vehicle and has an additional attribute year. 
# Implement a method display_info to print the car's details.'''

class RTO:
    def __init__(self,make,model):
        self.make = make
        self.model = model 

    @property
    def registration(self):
        return self.make[:3] + self.model[-3:]
    
class Car(RTO):
    def __init__(self,make,model,year):
        super().__init__(make,model)
        self.year = year

    def display(self):
        return f"Car model is: {self.make}\nCar make is:  {self.model}\nYear is:  {self.year}\nRegistration is:{self.registration}"
    
car = Car(make="Toyota",model="Camry",year = 2023)
print(car.display())