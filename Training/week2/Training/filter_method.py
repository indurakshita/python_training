from functools import reduce

# Filter Method


fruits = ["apple", "orange", "raspberry", "pineapple", "mango", "banana", "pomegreanate", "grapes"]

ages = [
    {
        "name": "albin",
        "age": 15
    },
    {
        "name": "akash",
        "age": 17
    },
    {
        "name": "naga",
        "age": 20
    },
    {
        "name": "inthu",
        "age": 25
    },
    {
        "name": "varun",
        "age": 30
    },
    {
        "name": "hussein",
        "age": 28
    },
]

# for a in ages:
#     if a["age"] >=18:
#         print(a["name"],"your eligible")
#     else:
#         print(a["name"],"your not eligible")
        
# get_voters = [(a["name"],"your eligible") if a["age"]>=18 else (a["name"],"Your not eligible") for a in ages]
# print(get_voters)
# for n,e in get_voters:
#     print(n,e)
        




# def filter_fruits1(fruit):
#     return fruit[0].casefold() == "p"


# def filter_fruits(fruit):
#     return len(fruit)>=6

# # # Recomended method
# f = filter(filter_fruits, fruits)
# print(list(f))


# # Not recomended logic
# filtered1 = [ i for i in fruits if i[0].casefold() == "p" ]

# # print(filtered)

# filtered = [ i if i[0].casefold() == "p" else "Not p" for i in fruits ]
# print(filtered)

# for i in fruits:
#     if i[0].casefold() == "p":
#         print(i)
    
#     else:
#         print("Not p")

# "----------------------------------------------------------------------------------------"
# # odd or even
def od_en(n):
    if n%2==0:
       return f"even-{n}"
    else:
        return f"odd-{n}" 
    
r=map(od_en,[1,2,3,4,5,6,7,8,9,10])
print(list(r))

"----------------------------------------------------"
# def func(n):
    
#     if n>=5:
#         return n
    
# r=filter(func,(1,2,3,4,5,6,7,8))
# print(list(r))
    

def f1(a,b):
    return a+b

r=reduce(f1,[1,2,3,4,5])
print(r)