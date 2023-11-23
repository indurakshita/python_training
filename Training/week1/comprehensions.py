from string import ascii_uppercase
# comprehensions (list, dictionary, set) - (tuple -> generator)

numbers = list(range(1, 101))
# for i in numbers:
#     if i%2==0:
#         print(i)
#     if i%2==1:
#         print("odd")
# # Single Condition
# odd = [i for i in numbers if i % 2 == 1]
# even = [i for i in numbers if i % 2 == 0]


# Multiple conditions
# check = [f"{i}=Odd" if i % 2 == 1 else f"{i}=Even" if i % 2 == 0 else "None" for i in numbers]
# print(check)

# # dictionary comprhension
# check = {idx:i for idx, i in enumerate(ascii_uppercase, start=1)}
# print(check)
fruits=["apple","orange","mango"]
f=[i for i in enumerate(fruits,start=1)]
print(f)

# set comprehension
# odd = {i for i in numbers if i % 2 == 1}
# print(odd)


# tup = (i for i in numbers if i % 2 == 0)
# print(next(tup))
# print(next(tup))
# print(next(tup))
# print(next(tup))
# print(next(tup))
# print(next(tup))