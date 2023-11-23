#while loop
#print the numbers 1 to 10
'''
n=int(input("enter a value"))
i=0
while(i<=n):
	print(i)
	i+=1
print("---------")

#print the even numbers
b=int(input("enter a value"))
print("even numbers are")
i=0
while(i<=b):
    print(i)
    i+=2
   
print("--------")  
b=int(input("enter a value"))
print("odd numbers are:")
i=1
while(i<=b):
    print(i)
    i+=2
    
#continue statement
#odd numbers
i=1
while(i<=20):
    if(i%2==0):
        i+=1
        continue;
    print(i)
    i+=1
 #even numbers
    i=1
while(i<=5):
    if(i%2==1):
        i+=1
        continue;
    print(i)
    i+=1
  
 #break statement
 
i=1
while(i<=20):
    if(i==7):
        break;
    print(i)
    i+=1
'''
    #range in python
    #print even number range(1-5)
print(list(range(5)))
print(list(range(2,5)))
print(list(range(0,21,2)))
print(list(range(1,20,2)))




  

    
    
    