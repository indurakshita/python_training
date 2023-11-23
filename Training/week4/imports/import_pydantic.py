from typing import List
from pydantic import BaseModel
from dataclasses import dataclass
from pprint import pprint
import json

# normal method
class User():
    name : str =""
    age : int = 0

    def __repr__(self):
        return f"Username:{self.name}\nage:{self.age}"
    

# user = User()
# user.name = "Indhu"
# user.age = 29

"----------------------------------------------------------------------------------------------------------------"

# pydantic method
class User(BaseModel):
    name : str 
    age : int 
user = User(name ="Indhu",age=27)
print(user)
# user1 = User(name ="Indhu",age=27)
# print(user1)
# user2 = User(name ="Indhu",age="ab")
# print(user2)

# methods in pydantic
# print(user.model_dump())
# print(user.model_dump_json())
'--------------------------------------------------------------------------------------------------------------'
#dataclass method:

# @dataclass
# class User():
#     name : str 
#     age : int 
# user = User(name ="Indhu",age="27")
# print(user)

# user = User(name ="Indhu",age="as")
# print(user)

'----------------------------------------------------------------------------------------------------------------------------------'
class Address(BaseModel):
    area:str
    pincode:int


class Degree(BaseModel):
    name: str
    univ:str
    address :Address

class User(BaseModel):
    name : str 
    age : int 
    degree : Degree
    address :Address

class Users(BaseModel):
    users : List[User]

user1 = User(
    name ="Indhu",
    age="27",
    degree=Degree(
        name="B.E",univ="Anna University",
        address=Address(
            area="Dgl",
            pincode=62411
            )
        ),
    address=Address(
        area="Chennai",
        pincode=624001
        )  
        )
user2 = User(name ="Rani",
            age="30",
            degree=Degree(name="B.E",univ="Anna University",address=Address(area="Dgl",pincode=62411)),
            address=Address(area="Chennai",pincode=624001)
             )

# print(user1.degree.name)
# print(user1.model_dump())

userss= Users(users=[user1,user2])
# pprint(userss)
# print(userss.model_dump_json)
print(json.dumps(userss.model_dump(),indent=4))




