'''Question 4: Create a class Animal with attributes name and species. 
Then, create a subclass Dog that inherits from Animal and has an additional attribute breed. 
Implement a method to display the dog's details.'''

# class Animal:
#     def __init__(self,name,species):
#         self.name = name
#         self.species = species
        
#     def ani_sound(self):
#        return "woof"
        
# class Dog(Animal):
#     def __init__(self,name,species,breed):
#         super().__init__(name,species)
#         self.breed = breed
    
#     def display(self):
#         print(f"name of the dog is.:".ljust(20),f"{self.name}")
#         print(f"Breed of the dog is:".ljust(20),f"{self.breed}")
#         print(f"species of the dog is:".ljust(20),f"{self.species}")
#         print(f"Sound of the dog is:".ljust(20),f"{self.ani_sound()}")


# b= Dog(name="Bella",species="German Shepard",breed = "Bull")
# b.display()