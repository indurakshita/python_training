#list
"""
a=[1,2,3,4,5]
print(a)
print(type(a))
print("slicing")
print(a[0])
print(a[1:4])
print(a[:4])
print(a[3:])
print(a[-1])
print(a[:-2])
print("--------")
a=[2,True,'indhu',5.5,[1,2,3,4]]
print(a)
print(type(a))
print(a[1],"type is",type(a[1]))
print(a[0],"type is",type(a[0]))
print(a[2],"type is",type(a[2]))
print(a[3],"type is",type(a[3]))
print(a[4],"type is",type(a[4]))
print((a[4][2]))
print("-----------")

a=[10,20,30,40]
print(a)
b=a.copy()
print(b)
c=[10,25,35,45,25,4,25]
print(c)
print(max(c))
print(min(c))
print(len(c))
print(c.count(25))
print(c.index(45))
c.clear()
c=[10,25,35,45,25,4,25]
print(c)
c.pop(1) #remove element using index
print(c)
d=[5,10,15,10,20,10]
d.remove(10) #remove element using value based
print(d)
print("----------------")
"""
names=["Ram"]
print(names)
names.append("sam")
names.append("balu")
names.append("raju")
print(names)
name2=["sara","radha"]
names.extend(name2)
print(names)
names.insert(1,"raja")
print(names)
print("-----------------")
print(list(range(5)))
print(list("Indumathi"))
a=[10,20,80,40,60,50]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=["Orange","Apple","Mango"]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a=["Orange","apple","mango"]
print(a)
a.sort(key=len)
print(a)



