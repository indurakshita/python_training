import json
import sys
import os
import random

if sys.platform == "win32":
    clear = lambda : os.system("cls")
else:
    clear = lambda : os.system("clear")

class Customer:

    def __init__(self,name,b_day,balance=0):
        self.name=name
        self.b_day=b_day
        self.balance=balance
    @property
    def ac_no(self):
        return self.name.upper()[:4]+self.b_day[-4:]
    def __repr__(self):

        return f"name:{self.name}\naccount no:{self.ac_no}\nbalance:{self.balance}\n"
        
    

      
class BankApp:
    data=None
    filename="bank_oops.json"
    customers=[]

    def __init__(self):
        clear()
        print("Banking Application".center(100)) 
        
        self.total_balance=0
        
        self.customers=self.load_customers()

    def add_customer(self,new_customer):
        
        self.customers.append(new_customer)
        self.store_customer()

    def store_customer(self):
        customer=[{"name":i.name,"b_date":i.b_day,"ac_no":i.ac_no,"balance":i.balance} for i in self.customers]
        
        with open(self.filename,"w") as f:
            json.dump(customer,f)
            
    
    def load_customers(self):
        
        try:
            with open(self.filename) as f:
                customers=json.load(f) 
                for customer in customers:
                    self.customers.append(
                        Customer(
                            name=customer["name"],
                            b_day=customer["b_date"],
                            balance=customer["balance"]
                            )
                    ) 
        except FileNotFoundError:
            return []


    def get_customer(self,account):
        for customer in self.customers:
            if customer.ac_no == account:
                return customer


    def deposit(self,account,amount):
        
        customer = self.get_customer(account)
        print(customer)
        customer.balance+=amount
        self.store_customer()
        
       
    
    def withdraw(self,account,amount):
        customer = self.get_customer(account)
        if customer.balance >= amount:
            customer.balance-=amount
            self.store_customer()
            
        else:
            print("insufficient balance")

    def display(self,account):
        customer = self.get_customer(account)
        print(customer)


 
def main():
        option=int(input("1.create_ac\n2.deposit\n3.withdraw\n4.display\n\5.exit\n"))
        bank = BankApp()
        if option == 1:
            name = input("enter the name: ")
            b_date = input("enter the birth data: ")
            user = Customer(name=name,b_day=b_date)
            bank.add_customer(user)

        if option == 2:
            ac_no=input("enter the account number:")
            amo=int(input("enter the amount"))
            bank.deposit(account=ac_no,amount=amo)
            
        if option == 3:
            ac_no=input("enter the account number:")
            amo=int(input("enter the amount"))
            bank.withdraw(account=ac_no,amount=amo)

        if option == 4:
            ac_no=input("enter the account number:")
            bank.display(account=ac_no)

        if option == 5:
            exit()

main()

