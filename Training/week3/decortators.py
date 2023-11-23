import time

# decorator
# it is a wrapper function
"---------------------------------------------------------------------------"
def deco(func):
    def inner():
        print("This is the decorator")
        func()
        print("end of the decorator")
    return inner
def f1():
    print("This is the First function")
    
d=deco(f1)
d()
"----------------------------------------------------------------------------------------------"

# @decorator
# def function():
#     ...

# high level functionality of decorator
# def add():
#     return 2 + 3


# def sub():
#     return 2 - 3

# def calc(f):
#     return f() + 10

# c = calc(add)
# print(c)

"-----------------------------------------------------------------------------------------------------"
# decorator for calculating time
from time import perf_counter


# def calc_time(func):
#     def wrapper(*args, **kwargs):
#         start = perf_counter()
#         final = func(*args, **kwargs)
#         total_time = perf_counter() - start
#         return final, total_time
#     return wrapper


# @calc_time
# def add():
#     return 2 + 3

# output, total_time = add()

# print(output, total_time)



# def change_case(func):
#     def wrapper(*args, **kwargs):
#         final: str = func(*args, **kwargs)
#         return final.title()
#     return wrapper

# @calc_time
# def loop_1000000():
#     a = 0
#     for i in range(1000000):
#         a += i
#     return a

# @calc_time
# def loop_2000000():
#     a = 0
#     for i in range(2000000):
#         a += i
#     return a

# @calc_time
# def loop_dynamic(num):
#     a = 0
#     for i in range(num):
#         a += i
#     return a

# @change_case
# def set_username_and_age(name, age=26):
#     return f"your name is {name} and you are {age} years old!!"


# username = set_username_and_age("indhu")
# print(username)

# # def calc_time(func):
# #     start = perf_counter()
# #     final = func()
# #     total_time = perf_counter() - start
# #     print(final, total_time)

# # calc_time(loop_1000000)
# # calc_time(loop_2000000)

# # loop_1000000()


# # loop_20 = loop_2000000()
# # print(loop_20)

# # loop_dyna = loop_dynamic(500)
# # print(loop_dyna)

# # set_user = set_username_and_age("indhu")
# # print(set_user)


# def general(func):
#     def wrapper(*args, **kwargs):
#         final = func(*args, **kwargs)
#         return final
#     return wrapper

# Type Writing effect
# from time import sleep

# def typing(sentence):
#     for i in sentence:
#         print(i, flush=True, end='')
#         sleep(0.1)


# def change_case(func):
#     def wrapper(*args, **kwargs):
#         final: str = func(*args, **kwargs)
#         return final.title()
#     return wrapper

# from functools import wraps

def typing(color='white', speed=5):
    speed = 10 if speed > 10 else 0 if speed < 0 else speed
    speed = (10-speed) * 0.05
    def inner(func):
        # @wraps(func)
        def wrapper(*args, **kwargs):
            "wrapper"
            colors = {
                "black": "\033[0;30m",
                "red": "\033[0;31m",
                "green": "\033[0;32m",
                "yellow": "\033[0;33m",
                "blue": "\033[0;34m",
                "purple": "\033[0;35m",
                "cyan": "\033[0;36m",
                "white": "\033[0;37m",
            }

            final = func(*args, **kwargs)
            final = colors.get(color, "white") + final+'\n' + colors.get("white")
            for i in final:
                print(i, flush=True, end="")
                time.sleep(speed)
                
            return final
        return wrapper
    return inner

@typing("blue", speed=6)
def some_sentence(name):
    "hello"
    sentence = f"Hello all, My name is {name}!!"
    return sentence
# r=some_sentence("Indhumathi")
# print(r)
help(some_sentence)
'------------------------------------------------------------------------------'

# @typing('red')
# def some_other():
#     return "Your task has been completed, and the output is something new"


# @typing()

# def some_blue():
#     return "Output in blue color"


# some_sentence("Indhumathi")
# some_other()
# some_blue()

# def typewrite(data):
#     for i in data:
#         print(i,flush=True,end='')
#         time.sleep(0.5)
# t = typewrite('I am indhu')


    
      
    



# def name(n): 
#     print(n)
#     def age(a):
#         return f"{n}-{a}"
#     return age(25)
# r=name(n="indhu")

# decorator
# def mul(func):
#     def wrapper(*args,**kwargs):
#         r=func(*args,**kwargs)
     
#         final = r*5
#         return final
#     return wrapper
# @mul
# def add(a,b):
#     return a+b
# r=add(4,5)
# print(r)
# "--------------------------------------------------------------------------"
# def deco(func):
#     def wrapper(*args,**kwargs):
#         r=func(*args,**kwargs)
        
#         final = r.upper()
#         return final
#     return wrapper

# @deco   
# def f1(name):
#     return f"this is {name}"  
# r=f1("indhu")   
# print(r) 



