import json
import os
import sys

Filename="pword_check.json"
if sys.platform == "win32":
    clear = lambda: os.system("cls")
    clear()
else:
    clear = lambda: os.system("clear")

checks=[
     {
        "upper" : "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "lower" : "abcdefghijklmnopqrstuvwxyz",
        "numbers" : "123456789",
        "characters" : "!@#$%^&*()_+",
        "weak" : 4,
        "medium" : 6,
        "strong" : 8
        }
        
]

with open(Filename,"w") as j:
    json.dump(checks,j)

with open(Filename,'r') as j:
    checks=json.load(j)



def check_pword(password):
    clear()
    print("Password Validation".center(100))
    
    if checks:
        for check in checks:
            up = [i for i in password if i in check["upper"]]
            low = [i for i in password if i in check["lower"]]
            num = [i for i in password if i in check["numbers"]]
            char = [i for i in password if i in check["characters"]]
            is_valid = all([up, low, num, char]) 
            
            if is_valid :
                print("Password is valid")
                p=len(password)
                if  p <=check["weak"]:
                    print(f"{password} is weak password")
                    input()
                    clear()
                elif p > check["weak"] and p <=check["medium"]:
                    print(f"{password} is medium password")
                    input()
                    clear()
                elif p > check["medium"] and  p >= check["strong"] :
                    print(f"{password} is strong password")
                    input()
                    clear()
            else:
                print("Password is not valid") 
                input()
                clear()
                
                password=input("enter the password:")    
                return check_pword(password)
          
check_pword(password=input("enter the password:"))

 
