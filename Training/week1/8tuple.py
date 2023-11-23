'''Tuple - is a collection which is ordered and unchangeable or immutable. Allows duplicate members.'''

tuple1 = ("Apple", "Orange", "kiwi", "Orange")
tuple2 = (1, 2, 3)


# 1.count()	Returns the number of times a specified value occurs in a tuple
# x= tuple1.count("Orange")
# print(x)

# 2.index()	Searches the tuple for a specified value and returns the position of where it was found
# x= tuple1.index("Orange")
# print(x)


'''Once a tuple is created, you cannot change its values. 
Tuples are unchangeable, or immutable as it also is called.'''
#1.how to add element in tuple value:

# tuple2 = list(tuple1)
# # tuple2.append(2) #using append method
# tuple2[0] = 3 #using index
# print(tuple2)
# print(tuple(tuple2))

# 2.how to add new tuple in old tuple(extend the tuple)
# y = ("strawberry",)
# tuple1 += y
# print(tuple1)
# or change into list and extend the new list into old one

# join the two tuples:
# tuple3 = tuple1 + tuple2
# print(tuple3)
