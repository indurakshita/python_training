# age = 18

# if age >= 18:
#     print("You can vote") 
# elif age == 15:
#     print("wait for 3 more years to vote")
# elif age == 10:
#     print("school student")
# else:
#     print("Not allowed")



# if (true statement):
#     oper

# if not (age >= 18):
#     print("Not allowed")
# else:
#     print("You can vote")

# False Values (0, None, False, '', [], set(), {}, ())
# True Values (if values, True, "content", [125, "items"], {"test"}, {"key": "value"}, ("someval", ))

# name = [1]

# if name:
#     print("it is a true value")
# else:
#     print("Not true")


# age = 18
# exam = None


# # Logicall error
# if age >= 28:
#     exam = "RCI"
   

# elif age >= 25:
#     exam = "sat"
    
# elif age >= 18:
#     exam = "gsat"

# else:
#     exam =""

# print("Your are eligible for {1} {2}".format(exam))

# Python indentation posiibilities
# if age >= 28: exam = "RCI"; exam = "Some other exam"
# elif age >= 25: exam = "sat" 
# elif age >= 18: exam = "gsat"
# else:exam =""

# print(f"Your are eligible for {exam} exam")


country = "India"
state = "Kerala"
district = "Coimbatore"


# Normal Conditions
# if country.casefold() == "india":
#     if state.casefold() == "tamilnadu":
#         if district.casefold() == "coimbatore":
#             print("Hi nanba")
#         else:
#             print("which district you are from")
#     else:
#         print("which state are you from")
# else:
#     print('what country you are from')
    
    
    

# # Gaurd Clause Conditons
# if not country.casefold() == "india":
#     print('what country you are from')
    
# elif not state.casefold() == "tamilnadu":
#     print("which state are you from")

# elif not district.casefold() == "coimbatore":
#     print("which district you are from")
    
# else:
#     print("Hi nanba")

# examples:

# species = "Animal"
# animal = "cat"


# if species.lower() == "animal":
#     if animal.lower() == "dog":
#         print(f"{animal} is woof.....")
#     else:
#         print("which animal sound would you like?")
# else:
#     print("which animal would you like?")


# if not species.lower() == "animal":
#     print("which animal would you like?")
# elif not animal.lower() == "dog":
#     print("which animal sound would you like?")
# else:
#     print(f"{animal} is woof.....")

    
