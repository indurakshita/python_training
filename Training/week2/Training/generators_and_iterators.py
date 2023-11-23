from sys import getsizeof
from time import perf_counter
# from variables_naming import UPPERCASE


# ZIP
name = ("albi", 'naga', "indhu")
age = (25, 24, 26)
mark = (80,85, 70)

for i in zip(name,age,mark):
    print(i)

'---------------------------------------------------------------------------------------'
# iterators
# datatypes which we can iterarte over is known as iterators
# example: list, set, dictionary, strings
# iter() and next()

# from sys import getsizeof
# from time import perf_counter

# start = perf_counter()
# tup = ["albi", 'naga', "indhu"]
# tup = iter(tup)
# print(type(tup))
# total_time =perf_counter()-start
# print(next(tup))
# print(next(tup))
# print(next(tup))
# print(total_time)

# for i in tup:
#     print(i)
# print(total_time)

'-------------------------------------------------------------------------------------'
# # generators
# start = perf_counter()
# gen = (i for i in range(100000000))
# total_time = perf_counter() - start
# print(f"{'Generator Size': <20}: {getsizeof(gen)}\n{'Time Took': <20}: {total_time:.2f}\n")


# start = perf_counter()
# lst = list(i for i in range(100000000))
# total_time = perf_counter() - start
# print(f"{'List Size': <20}: {getsizeof(lst)}\n{'Time Took': <20}: {total_time:.2f}")


# def get_item_gen(items):
#     for item in items:
#         yield item

# tup = ("albi", 'naga', "indhu")

# gen = get_item_gen(tup)
# print(next(gen))

# generator
# tup = ("albi", 'naga', "indhu", "akash", "varun")
# gen=(i for i in tup)
# print(type(gen)) 

# print(next(gen))
# print(next(gen))
# print(next(gen))
# '--------------------------------------------------------------------------------------------------'
# def func(n):
#     for i in range(n):
#         yield i**2

# a=func(3)
# print(list(a))
# for i in a:
#     print(i)

# n=["1","3","Indhu"]
# for i in n:

#     y= iter(i)

# print(type(y))
   