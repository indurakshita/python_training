#cohesion(function should be have high cohesion):
''' one function doing only and one task'''
 #Coupling(lower dependency)
# import requests
# import random

# def api_jokes():
#     url = "https://v2.jokeapi.dev/joke/Any"
#     response = requests.get(url).json()
#     return response.get("joke")

# def default_joke():
#     jokes = ["I joke","II joke","III joke","IV joke"]
#     return random.choice(jokes)

# joke = api_jokes() or default_joke()

# def main(joke):
#     print(f"Today's joke:\n{joke}")
# main(joke)

# ---------------------------------------------------------------------------------------------------------   
# import string
# import random

#static method:
'''It's doing function itself doesn't take the class attributes'''

# class User:
#     def __init__(self,name,profession):
#         self.name = name
#         self.profession  = profession
#         self.__password  = None

#     @staticmethod
#     def create_password(count):
#         char = string.ascii_letters + string.digits
#         char = [i for i in char]
#         random.shuffle(char)
#         char = "".join(random.choices(char, k=count))
#         return char


#     @property
#     def password(self):
#         if self.__password is None:
#             self.__password = self.__password or self.create_password(5)
#         return self.__password

# user = User("Indhu","developer")
# print(user.password)
#  ----------------------------------------------------------------------------------------------------
# Class method

'''Its shouldnot accessed initial attribute but allow to access default attributes.
Its multible times call multible object'''
'''Declares a class method.
The first parameter must be cls, which can be used to access class attributes.
The class method can only access the class attributes but not the instance attributes.
The class method can be called using ClassName.MethodName() and also using object.
It can return an object of the class'''

# difference b/w class method and static method:
'''@classmethod	
Declares a class method.	                                                                
It can access class attributes, but not the instance attributes.	
It can be called using the ClassName.MethodName() or object.MethodName().	
It can be used to declare a factory method that returns objects of the class.	
Declares a static method.

@staticmethod:
It cannot access either class attributes or instance attributes.
It can be called using the ClassName.MethodName() or object.MethodName().
It cannot return an object of the class.'''

import json

l_user = [{
    "name": "Indhu",
    "profession": "developer",
    "exp": 2
    },
    {
    "name": "Rakshita",
    "profession": "Doctor",
    "exp": 2
    },
    {
    "name": "Chandru",
    "profession": "HR",
    "exp": 2
    },
]

class User:
    def __init__(self,name,profession):
        self.name = name
        self.profession  = profession


    def __str__(self):
        return f"Name:{self.name}\nProfession:{self.profession}"

    @classmethod
    def create_user_from_list(cls,user_list):
        
        users=[]
        for user in user_list:
            user = cls(user["name"],user["profession"])
            users.append(user)
        return users
        
   
user1 = User("Rani","Admin")
print(user1)
user2 = User.create_user_from_list(l_user)
print(user2)

#     @classmethod
#     def create_from_json(cls,filename):
#         with open(filename) as f:
#             users_list = json.load(f)
#         users=[]
#         for user in t:
#             user = cls(user["name"],user["profession"])
#             users.append(user)
#         return users
# if __name__ == "__main__":
#     # user1 = User.create_from_json("some_json_file.json")
#     # print(user1)