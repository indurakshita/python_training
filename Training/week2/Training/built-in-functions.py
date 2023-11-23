

# abs() give back absolute value
# a = -18
# print(abs(a))

# all()
# some_list = [True, True, False, True] 
# print(all(some_list)) # returns True if all the values inside th list is True else returns False

# any()
# some_list = [False, False, False, True] 
# print(any(some_list)) # returns True if any of the values inside th list is True else returns False

# ascii()
# a = ascii("hello") # just gives you the representation
# print(a)

# bin()
# a = bin(89568) # gives back the binary values for a given integer
# print(a)

# bool()
# a = bool(-5652) # return True if the value is True else returns False
# print(a)

# breakpoint() Set breakpoints for debugging


# bytearray()
# a = bytearray(b"albin") # generate iterables of ascii values from bytes object
# for i in a:
#     print(a)

# bytes()
# a = b"inthu" # explicitly set the object as bytes
# print(bytes(a))

# callable()
# some = lambda: "hello" # check whether the object is fucntion or not
# print(callable(some))

# chr()
# print(chr(97)) # return ascii character when providing ascii number

# compile()
# a = "print('hello world')" # Compile a source code
# code = compile(a, filename="test.py", mode="single")
# print(exec(code))

# complex()
# a = complex(25, 30) #  returns complex numbers
# print(a)

# dir()
# import requests # dir shows all the commands available for a packacge or module
# print(dir(requests))


# divmod()
# a = 11
# b = 3
# out = divmod(a,b) # returns qoutient and reminder form as a tuple
# print(out)

# from datetime import timedelta

# -----------------------------------------------------------
# enumerate() -> [(index, value)]
lst = ["albin", "indhu", "akash", "naga"]
# lst.insert(3, "kannan")


# for i in range(len(lst)):
#     if i < 3:
#         print(lst[i])

# count = 0
# for i in lst:
#     if count < 3:
#         print(i)
#         count += 1

# count = 0
# while count < 3:
#     print(lst[count])
#     count += 1

# count = 0
# while True:
#     if count < 3:
#         print(lst[count])
#         count += 1
#     else:
#         break

# from time import perf_counter

# start = perf_counter()
# for idx, name in enumerate(lst):
#     if idx < 3:
#         print(idx, name)
# print(perf_counter() - start)


# start = perf_counter()
# for i in range(len(lst)):
#     if i < 3:
#         print(i, lst[i])
# print(perf_counter() - start)

# --------------------------------------------------------

# eval()
# from functions import *

# def some(name):
#     return "returning something from the function some"

# add = lambda a,b: a+b
# sub = lambda a,b: a-b
# mul = lambda a,b: a*b
# div = lambda a,b: a/b

# user = input("enter calculation (add, sub, mul, div): ") # add, sub, mul, div
# nums = input("enter nums: ") # comma seperated 2 values
# getting_function = eval(user)

# a, b = nums.split(",")
# print(getting_function(int(a), int(b)))

# apple = "Apple is red"
# orange = "Orange is orange"

# user = input("Enter fruit: ").casefold()
# # normal method
# if user == "apple":
#     print(apple)
# elif user == "orange":
#     print(orange)

# # using eval method
# print(eval(user))

# exec()
# executing code from other files
# with open("scopes.txt") as f:
#     exec(f.read())

# user = input("Enter code: ")
# flag = False
# for i in user.split():
#     if i in ["password", "username", "select"]:
#         flag = True

# if not flag:
#     exec(user)
# else:
#     print("hacking script found... ")

# format()
# method_1 = "My name is {} and I am a {}".format("indhu", "python developer") # method 1
# method_2 = "My name is {1} and I am a {0}".format("indhu", "python developer") # method 2
# method_3 = "My name is {name} and I am a {profession}".format(name="indhu", profession="python developer") # method 3
# method_4 = "My name is %s and I am a %s" % ("indhu", "python developer") # Not used method 4

# frozenset()
# frozen = frozenset(["albin", "akash", "albin"]) # unique and immutable
# print(frozen)

# hash() returns unique identifier
# password = "indhu@123"
# hashed = hash(password) 
# print(hashed)


# help() information about a particuluar function, method or an object which is defined in its documentation.
# def some(name: str) -> str:
#     """Gives you back some message"""
#     return "hello"
# help(some)


# hex() returns hexadecimal value of an integer
# a = 8080
# print(hex(a))