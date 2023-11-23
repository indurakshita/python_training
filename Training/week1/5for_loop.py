# what is loop?
# for (for loops) there is a finite end
# whereas for (while loops) its infinite

# Strings
# name = "Inthu"
# for i in name:
#     print(i)

# number as strings not integer
# name = "78956"
# for i in name:
#     print(i)

# for loops using range
# finite = 101
# for number in range(1, finite):
#     print(number)

# # Sets
# st = {"apple", "mango", "orange"}
# for fruits in st:
#     print(fruits)

# # List
# lst = ["apple", "mango", "orange"]
# for fruits in lst:
#     print(fruits)

# # tuple
# tup = ("apple", "mango", "orange")
# for fruits in tup:
#     print(fruits)
    
dct = {"a": "apple", "m": "mango", "o":"orange"}

for key, fruits in dct.items():
    print(key, fruits)

# Dict keys
for key in dct.keys():
    print(key)

# for fruits in dct:
#     print(fruits)

# # dict values
# for fruits in dct.values():
#     print(fruits)


# For loop scope and If else scope
# for number in range(1, 101):
#     if number % 2 == 0:
#         print("Even number")
#     else:
#         print("Odd number")

# lst = ["albin", "inthu", "nagarjun", "Varun", "ram", 'raja', "kannan"]


# Break
# identified = None
# for name in lst:
#     print(name)
#     if name.casefold().startswith("ra"):
#         identified = name
#         print()
#         print("i have identified the name")
#         print()
#         break
   
# print()       
# print(identified)

# lst = ["albin", "nagarjun", "inthu", "Varun", "ram", 'raja', "kannan"]

# # Continue
# for name in lst:
#     if name.casefold() == "inthu":
#         continue
    
#     if name.casefold() == "ram":
#         continue
    
#     print(name)
   
# print("Outside of for loop")

   