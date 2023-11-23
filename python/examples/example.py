#example for if
""" 
3 marks as input
total
average
result
if pass grade
90-100 A
80-89 B
70-79 C
Else D
"""
m1=int(input("Enter mark-1:"))
m2=int(input("Enter mark-2:"))
m3=int(input("Enter mark-3:"))
tot=m1+m2+m3
avg=tot/3
print("total:",tot)
print("average:",avg)
if(m1>=35 and m2>=35 and m3>=35):
    print("result: pass")
    if(avg>=90 and avg<=100):
        print("Grade is: A")
    elif(avg>=80 and avg<=89):
        print("Grade is: B")
    elif(avg>=70 and avg<=79):
        print("Grade is: C")
    elif(avg>=40 and avg<=69):
        print("Grade is:",D)
    elif(avg>=35 and avg<=39):
        print("Grade is:",E)
else:
	print("result is: Fail")

		
		
	
	


