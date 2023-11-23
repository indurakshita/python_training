# Map -> to map all the elements in an iterable and process the output
from time import perf_counter
from functools import reduce
fruits = ["apple", "orange", "raspberry"]
vegs=["carrot","potato","tomato"]

def map_fruits(fruit,veg):
    return fruit,veg
    

# recomended method
# start = perf_counter()
# mapped = list(map(map_fruits, fruits,vegs))
# print(mapped)
# print(perf_counter()-start)

# filtered = list(filter(map_fruits, fruits,vegs))
# print(filtered)


# Python logic
# start = perf_counter()
# mapped2 = [map_fruits(i) for i in fruits]
# print(mapped2)
# print(perf_counter()-start)


# Check length of items in a list
# mapped = list(map(lambda fruit:{fruit:fruit[0]},fruits))
# print(mapped)

"---------------------------------------------------------------------------------------------------------"
#filter with map and map with filter

def f1(n):
    return n*2
def f2(a):
    return a>3
#filter inside map
# r=  map(f1,filter(f2,[1,2,3,4,5,6,7,8]))
# print(list(r))

# r=map(lambda x : x*2,filter(lambda y:y>3,[1,2,3,4,5,6,7,8]))
# print("Using lambda",list(r))


# # map inside filter
# r=filter(f2,map(f1,[1,2,3,4,5,6,7,8]))
# print(list(r))
r= filter(lambda x:x*2,1,2,3,4,5,6)
print("Using lambda",list(r))


# reduce method

def add(a,b):
    return a+b

r= reduce(add,[1,2,3,4,5,6,7])
print(r)


# r = reduce(add,filter(lambda y: y > 3, map(lambda x: x * 2, [1,2,3,4,5,6,7,8])))
# print("Using reduce with lambda",r)