'function should be same names'

class Human:
    
    def walk(self):
        return "walk with two legs"
    
class Tiger:

    def walk(self):
        return "walk with 4 legs"
    
class Parrot:

    def walk(self):
        return "walk with 2 legs"
    
# animals = [Human,Tiger,Parrot]

# for animal in animals:
#     # walk = animal().walk()
#     walk = animal.walk(animal)

#     print(animal.__name__, '=',walk)

#method2

animals = [Human(),Tiger(),Parrot()]

for animal in animals:
    print(f"{animal.__class__.__name__} = {animal.walk()}")


   

