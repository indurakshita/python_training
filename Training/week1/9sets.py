"""set - A set is a collection which is unordered, unchangeable*, and unindexed.
Note: Set items are unchangeable, but you can remove items and add new items."""
set1 = {"Orange", "kiwi","mango","pappaya"}
set2 = {"beetroot", "mango","pappaya"}
set3 = {"Orange", "kiwi"}



#1.Duplicates Not Allowed

# print(set1)

#2.add() - Adds an element to the set
# set1.add("strawberry")
# print(set1)

# 3.clear()	Removes all the elements from the set
# set1.clear()
# print(set1)

# 4.copy()	Returns a copy of the set
# set3 = set1.copy()
# print(set3)

# 5.difference() - Returns a set containing the difference between two or more sets

# z=set1.difference(set2) 
# print(z)
# set1.difference_update(set2)
# print(set1)
# 6.The discard() method removes the specified item from the set.

# set1.discard("Orange")
# print(set1)

# 7.The intersection() method returns a set that contains the similarity between two or more sets.
# z=set1.intersection(set2) 
# print(z)
# set1.intersection_update(set2) 
# print(set1)
# 8.isdisjoint() - if Evanan one value same in Ist and 2nd set means True
# z=set1.isdisjoint(set2) 
# print(z)

# 9.issubset()	Returns whether another set contains this set or not
# z=set1.issubset(set3) 
# print(z)

# 10.The issuperset() method returns True if all items in the specified set exists in the original set, 
# otherwise it returns False.
# z=set1.issuperset(set3) 
# print(z)

# 11.The symmetric_difference() method returns a set that contains all items from both set, 
# but not the items that are present in both sets.

# z=set1.symmetric_difference(set2) 
# print(z)

# 12.union() - Return a set that contains all items from both sets, duplicates are excluded:

# z=set1.union(set2) 
# print(z)

# 
# 13.update - Update the set with another set, or any other iterable

# set1.update(set2) 
# print(set1)