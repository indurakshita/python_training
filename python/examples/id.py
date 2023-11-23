#identity operator in python
a=[1,2]
b=[1,2]
c=a
print(a is c) #check the memory
print(a is b)
print(id(a))
print(id(c))
print(a==b) #check the values
print(a is not c)
