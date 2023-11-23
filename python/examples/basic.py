#basic datetime
'''
import datetime
now=datetime.datetime.now()
print("date and time")
print(now.strftime("%Y-%M-%D %H:%M:%S"))
'''
#current date and time
import datetime as dt
current_date=dt.date.today()
current_time=dt.datetime.now()
print("current date is",current_date)
print("current time is",current_time)
print("------------")

#give the date 
new=dt.date(2022,7,5)
print(new)
print("year",new.year)
print("month",new.month)
print("day",new.day)
print("-------------------------") 
#seperate date and time
new=dt.datetime(2023,1,5,6,30,30)
print(new)
print(new.date())
print(new.time())
print("---------")
#difference between 2 date
current=dt.datetime.now()
n_year=dt.datetime(2024,1,1)
diff=n_year-current
print(diff)
# different style of date
current=dt.datetime.now()
s=current.strftime("%A %B %d %Y")
print(s)
'''
#calendar
import calendar
y=int(input("enter a year;"))
m=int(input("enter a month;"))
print(calendar.month(y,m))

#calculate the numbers of days b/w two date
from datetime import date
a=date(2023,4,10)
b=date(2023,4,25)
c=b-a
print(c.days)


#given number same multiply with 3 if different add 3 numbers
a=int(input("enter a value"))
b=int(input("enter a value"))
temp=a
a=b
b=temp
print(a)
print(b)

#check leap year
year=int(input("enter a year"))
if year%4==0:
    print("It's leap year")
else:
    print("it's not leap year")
 
#which is largest number
a=int(input("enter a value"))
b=int(input("enter a value"))
c=int(input("enter a value")) 
if a>b and a>c:
    large=a
elif b>a and b>c:
    large=b
else:
    large=c
    print("largest number is:",large)

#if number is prime or not
n=int(input("enter a number:"))
if (n%2==0):
    print("it's not a prime")
elif (n==1):
    print("it's not a prime")
else:
    print("it's prime")
   
#print the prime numbersbas
l=int(input("enter a number:"))
u=int(input("enter a number:"))
print("prime numbers")
for n in range(l,u,1):
    if n>1:
        for i in range(2,n):
            if(n%i)==0:
                break
        else:
            print(n)
        
     
   
# multipllication table
n=int(input("enter a number:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)
 
# fibnaacci series
n=int(input("enter term"))
a=0
b=1
i=1
while i<=n:
    print(a)
    c=a+b
    a=b
    b=c
    i+=1

#armstrong number
n=int(input("enter a value"))

sum=0
t=n
while t>0:
    d=t%10
    sum+=d**3
    t//=10
if n==sum:
    print(n,"armstrong number")
else:
    print(n,"not armstrong number")
  
 #armstrong number in intervals
l=int(input("enter a lowest number"))
u=int(input("enter a highest number"))
for n in range(l,u,1):
    sum=0
    t=n
    while t>0:
        d=t%10
        sum+=d**3
        t//=10
        if n==sum:
            print(n)


#factorial numbers

i = 1	1 * 1 = 1
i = 2	1 * 2 = 2
i = 3	2 * 3 = 6
i = 4	6 * 4 = 24

n=int(input("enter a value"))
f=1
i=1
if(n>=1):
    for i in range(i,n):
        f=f*i
        print("factorial of",n,"is",f)
else:
    print("factorial not exist")
    
#factorial in fns
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
c=factorial(5)
print(c)
    



    # Sum of natural numbers up to num

n=int(input("enter a number"))

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)
 
#calcute the power of 2
n=int(input("enter a number"))
for i in range(0,n):
    s=0
    i=2**i
  print("power of 2 is",i)

#if the number divisable by another number
l=int(input("enter a lowest number"))
u=int(input("enter a highest number"))
n=int(input("enter a number"))
for i in range (l,u,+1):
    if(i%n==0):
        print(i)
    else:
        continue
        i+1

# add the 2 matrix.
x=[[1,2,3],
   [4,5,6],
   [7,8,9]]
y=[[1,2,3],
   [4,5,6],
   [7,8,9]]
res=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        res[i][j]=[x[i][j]+y[i][j]]
for r in res:
    print(r)
'''
    