#set and its fns in python
"""
n={'raja','sara','kavi'}
print(n)
print(type(n))
for n1 in n: #set in loop
	print(n1)
n.add("sri")
print(n)
n2={"kani","suri","mani"}
n.update(n2)
print(n)
n.remove("suri")
print(n)
n.pop()
print(n)
n.clear()
print(n)
del n
print(n)

n={'raja',"raja",'sara','kavi'}
print(n)
#union
a={1,3,5,6,4}
b={"a","b","c"}

c=a.union(b)
print(c)
"""
a={1,3,5,6,4}
b={2,8,10,7,9}

c=a.intersection(b)
print(c)
a.intersection_update(b)
print(a)

c=a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)
c=a.isdisjoint(b)
print(c)

a={5,6,7}
b={5,6,7,8}
c=a.issubset(b)
print(c)
c=b.issubset(a)
print(c)

a={1,3,2,8,4}
b={2,8,10,7,9}
c=a.issubset(b)
print(c)

a={5,6,7}
b={5,6,7,8}
c=a.issuperset(b)
print(c)
a={5,6,7}
b={5,6,7}
c=a.issuperset(b)
print(c)


	