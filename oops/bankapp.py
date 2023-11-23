import sys
import os
import random

if sys.platform == "win32":
    clear = lambda : os.system("cls")
else:
    clear = lambda : os.system("clear")



class BankApp:
    clear()
    cus_details={}
    print("Banking System".center(100))
    def __init__(self,name):
        self.name = name
        self.ac_no = 0
        self.withdraw = None
        self.balance = 0

    def create_ac(self):
            self.ac_no =''.join([str(random.randint(0, 9)) for _ in range(10)])
            # self.ac_no=random.randint(1111111,1111120)
            # return self.ac_no
            
   
    def add_deposit(self):
        op = input(f"do you want deposit the amount to customer {self.name} (yes/no):")
        clear()
        if op == "yes":
            amount = float(input("enter the amount:"))
            self.balance+=amount
            print("deposit successfully")
            input()
            clear()
        else:
            print("Thank you")
            input()
            clear()
    def add_withdraw(self):
        op = input("do you want withdraw the amount (yes/no):")
        clear()
        if op == "yes":
            amount = float(input("Enter the amount:"))
            if self.balance:
                self.balance-=amount
                print("withdraw successfully")
                input()
                clear()
            else:
                print("insufficient balance")
                input()
                clear()
        else:
            print("Thank you")
            input()
            clear()
    
            
    def __repr__(self):
        return f"Name:{self.name}\naccount no:{self.ac_no}\nbalance:{self.balance}"
    
    
    

user1 = BankApp(name="Indhu")
user2 = BankApp(name="Chandru")
user1.create_ac()
user1.add_deposit()
user1.add_withdraw()

print(user1)
user2.create_ac()
user2.add_deposit()
user2.add_withdraw()
print(user2)

    





