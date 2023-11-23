from sys import getsizeof

# list comprehension

# for i in range(11):
#     if i==5:
#         print(i)

# a= [i if i==5 else i for i in range(10) ]
# print(a)
"-------------------------------------------------------------------------------------"

# for i in range(11):
#     if i%2 ==0:
#         print(f"Even numbers are {i}")
#     else:
#         print(f"odde number {i}")

# print(list(f"Even numbers are {i}" if i%2==0 else f"odde number {i}" for i in range(11)) )

"----------------------------------------------------------------------------------------------------------"
# filered method
# # syntax
# filter(func,iterable)

# fruits =["apple","orange","mango","pineapple"]
# def f1(n):
#     for i in n:
#         if i>=3:
#             return i

# f=f1([1,2,3,4,5,6,7])
# print(f)

# ages =[5,15,18,6,21,23]
# # def func1(age):
# #     return age<18
# # a=list(filter(func1,ages))
# # print(a)


# a= list(filter(lambda x: x,ages))
# b=sorted(a,reverse=True)
# print(b)

"-----------------------------------------------------------------------------------"
# generator

# def func(n):
#     for i in n:
#         print(f"{i}-{getsizeof(i)}")
# r=func([2,3,4,5,6,8])
# print(f"{list(r)}-{getsizeof(r)}")

"-----------------------------------------------------------------"
# iter
n=[1,2,3,4,5,6,7,8]    
r=iter(n)
print(next(r))
print(next(r))

"-----------------------------------------------------------------------------------"
# reduce
from functools import reduce
def f1(a,b):
    return a+b

r=reduce(f1,[1,2,3,4,5])
print(r)