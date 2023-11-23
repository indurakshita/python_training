#for loop
#even no
'''
for i in range(0,21,2):
	print(i)
print("__________1")
for i in range(1,20,2):
	print(i)

# print 
*
**
***
****
*****
'''
for i in range(5):
    for j in range (i):
        print("*",end="")
    print("")
print("---------")
''' 
# print
*****
****
***
**
*
'''
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print("")
#print
'''
ABCDE   
ABCDE 
ABCDE  
ABCDE 
ABCDE 
'''
for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end="")
    print("")
    
    
    
    
    