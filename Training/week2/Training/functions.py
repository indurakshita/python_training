# Functions

# Functions are used to run a set of tasks or to group tasks
# able to call multiple times whenever needed
# able to pass arguments and keyword arguments as th input

# Two types of arguments
# Positional and Keyword Arguments
# if we set a default value to a positional argument it becomes keyword argument
# Dont forget the order !!!!!!
# (Keyword argument comes after postional argument)
# *args and **kwargs
# *args returns a tuple
# # **kwargs returns dictionary


# Positional Arguments (args)
# def get_args(name, age):
#     return f"my name is {name} and I am {age} years old"

# # Keyword Arguments (kwargs)
def get_args(name=None, age=None):
    return f"my name is {name} and I am {age} years old"


# # When we have uncertainity about the inputs we get we use *args and **kwargs
# # # Arguments (*args)
# def get_args(*args):
#     print(args)

# # # Arguments (**kwargs)
def get_kwargs(**kwargs):
    print(kwargs)


# # # example combination
# def get_combination(name, age=25, *args, **kwargs):
#     print(name,age,args, kwargs)


# args = get_args("albin", "anthony", 25, True, "hello", 3.2)
kwargs = get_kwargs(fname="albin", lname="anthony", age=25, dveveloper=True, messsage="hello", point=3.2)
# comb = get_combination("albin", 29,"Anthony", distance=36)
# # print(comb)


# # addition (normal function)
# def addition(x, y):
#     ...
#     ...
#     ...
#     ...
#     ...
#     ...
#     return x+y

# # add = addition(2, 5)
"-------------------------------------------------------------------------------------------"


# # Anonymous function or lambda function addition
# anon = lambda x, y: x+y

# # print(anon(2, 5))

"---------------------------------------------------------------------------------------------"

# # recursion

# def func(n):
#     if n!=0:
#         return n+func(n-1)
#     return n
# print(func(2))

"-----------------------------------------------------------------"
# scope

# g_var = 8

# def f1():
#     f1_var = 2
#     print(f1_var)
    
   
#     def f2():
#         f2_var = f1_var
#         print(g_var)
        
#         def f3():
#             f3_var =5
#             print(f3_var)
#             print(f2_var)
#             print(f1_var)
#         f3()
    
#     f2()
#     print(g_var)
# f1()
"-----------------------------------------------------------------------------"
# func within function
def first(name):
    return f"hello world {name}"


def second(func):
    res = func("Indhu")
    return res.upper()

def third(func, func2):
    res = func(func2)
    return res + " Third"

out = third(second, first)
print(out)


# print(out)
