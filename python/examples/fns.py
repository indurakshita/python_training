#function
#no return type without arguement
"""
def welcome():
    print("welcome Indhu")
welcome()
welcome()
welcome()
#return type without arguement:
def add():
    a=int(input("enter a A value:"))
    b=int(input("enter a B value:"))
    c=a+b
    return c
x=add()
print(x)

#no return type with arguement
def sub(a,b):
    c=a-b
    print(c)
sub(50,25)

#return type with arguement
def div(a,b):
    c=a/b
    return c
x=div(50,2)
print(x)

#arbitary arguement in python

def cls(*stud):
    print(stud)
    for user in stud:
        print(user)
cls("ram","suja","kathir")

# keyword argument in python
def msg(name,age):
    print('name is',name,'age is',age)
msg(age=35,name="suji")

#arbitory keyword arguement in python
def biodata(**data):
    print(data)
   
biodata(name="suji",age="25",gender="female")

#passing list as an arguement
def total(marks):
    return sum(marks)
print("total",total([70,75,85,90,80]))

#factorial in fns
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
c=factorial(5)
print(c)
"""
#lambda function

c=lambda a:a+5
print(c(5))
c=lambda a,b:a*b
print(c(5,5))
    

    





