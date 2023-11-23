"""
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   print(digit)
   sum += digit ** 3
   print(sum)
   temp //= 10
   print(temp)

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
   
   
n=int(input("enter a number"))
s=0
d=1
t=n
while t>0:
	d=t%10
	s+=d**3
    
	print(c)
	print(d)
    print(t)
if n=s:
    print("armstrong number is",n)
else:
    print(n,"It's not armstrong number")
    
#Given a list, write a Python program to swap first and last element of the list.


def lst(n):

    s=len(n)
    
    t=n[0]
    n[0]=n[(s-1)]
    n[(s-1)]=t
    return n
x=lst([1,2,3,4,5])
print(x)
"""
#find a factorial number
n=int(input("enter a number"))
f=1
while n<0:
    print("factorial doesnot exist")
else:
    for i in range(n,1,-1):
        f=i*(i-1)
             
    print("factorial is",f)
 
 
"""   
    
    n=int(input("enter a value"))
f=1
i=1
if(n>=1):
    for i in range(i,n):
        f=f*i
        print("factorial of",n,"is",f)
else:
    print("factorial not exist")
"""
	
	