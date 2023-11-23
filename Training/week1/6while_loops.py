# while loops (infinit loops)

# while [condition]:
#     code..


# while True:
#     name = input("Enter you name: ")

#     check = input(f"is your name {name}? ")

#     if check.casefold() in "yes":
#         print(f"hello {name}")
#         break
#     else:
#         print("Try again...")

# print('Outside of while loop')


start = 0
name = 'inthu0'

# print(cond)

# while name != "inthu10":
#     print("the name is ", name)
#     start += 1
#     name = "".join([i for i in name][:5])
#     name = name + str(start)


cond = name == "inthu10"
# print(cond) = False

while not cond:
    start += 1
    name = "".join([i for i in name][:5])
    name = name + str(start)
    
    if name.casefold() == "inthu10":
        break
 
    
# start = 10 
# for i in range(start):
#     print(i)