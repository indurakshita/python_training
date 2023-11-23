"""
s="hello"
print(s.upper())  #upper
a="HELLO"
print(a.lower())    #lower
print(a.replace("H","h")) #replace str
a="hai,hello"
b=a.split(",") #split sub str
print(b)

#keyword
import keyword
print(keyword.kwlist)

#input statement
name=input("Enter a Name:")
print(name)
print(type(name))

#input statement 
a=input("Enter a value of A:") #input type always consider as a string type
b=input("Enter a value of B:")
c=a+b
print(c)
print(type(c))
a=int(input("Enter a value of A:"))
b=int(input("Enter a value of B:"))
c=a+b
print(c)
print(type(c))


#multiple inputs in single line
n1,n2,n3=input("Enter 3 Names: ").split()
print("Name1:",n1)
print("Name2:",n2)
print("Name3:",n3)
n1,n2,n3=input("Enter 3 Names: ").split(",")
print("Name1:",n1)
print("Name2:",n2)
print("Name3:",n3)

#multiline string using"""
a="""I am Indhu. I completed B.E. 
Now am working woman."""
print(type(a))
print(a)
a=["1","2","3"]
print(':'.join(a))

a=[]
print("enter a data:")

while True:
    line=input()
    if line:
        a.append(line)
    else:
        break
print(a)
op='\n'.join(a)
print(op)




