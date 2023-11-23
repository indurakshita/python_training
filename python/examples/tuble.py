#tuple in python
"""
a=(1,2.5,True,'Ram')
print(a)
print(type(a))
print(a[1])
print(a[-1])
print(a[0:2])
print(a[:-1])
b=list(a)
b.append("sugi")
print(b)
a=tuple(b)
print(a)
print(type(a))
print(len(a))
b=(5,)
print(type(b))
#loop
for i in a:
    print(i)

if "Ram" in a:
    print("Ram is found")
else:
     print("Ram is not found")
print("-----------------")
del a
print(a)
print("-------------------")
"""
x=("indhu",)*5
print(x)
a=(1,3,4,5,6)
print(min(a))
print(max(a))

a=(1,2,3,5,7,6)
b=(5,6,7)
c=a+b
print(c)
print(c.count(7))
print("-------------------")

#nested tuple
a=(1,2,3,5,7,6)
b=(5,6,7)
c=(a,b)
print(c)
print(c[0])
print(c[1][2])








   