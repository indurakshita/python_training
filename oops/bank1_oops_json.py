import sys
import os
import random
import json

if sys.platform == "win32":
    clear = lambda : os.system("cls")
else:
    clear = lambda : os.system("clear")

filename = "bank1_oops.json"
filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)),filename)

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
    filename=filepath
    customers=[]
    
    print("Banking System".center(100))
    def __init__(self):
        def_tot_amount = 0

     
    def w_data(self,customers):
        
        try:
            with open(self.filename,"w") as f:
                
               json.dump(customers, f, default=lambda o: o.__dict__, indent=4)
               
                    
        except FileNotFoundError:

            print("filenot found")
            return []
            

    def get_data(self):
        with open(self.filename) as f:
            customers=json.load(f)
        
        return customers

    
        
    def add_customers(self,new_customer):
            self.customers.append(new_customer)
            
            self.w_data(self.customers)
            
    def deposit(self):
        customers = self.get_data()
        
        if customers:
            account=input("enter the account number:")
            amount = float(input("enter the amount:"))
            for customer in customers:
                
                if customer["account_no"] == account:
                    customer["balance"]+=amount
                    print(customer)
                
                    print("deposit successfully")
                    input()
                    clear()
                
    def withdraw(self):
        customers = self.get_data()
        if customers:
            account=input("enter the account number:")
            amount = float(input("enter the amount:"))
            for customer in customers:
                
                if customer["account_no"] == account:
                    if customer["balance"]>amount:
                        customer["balance"]-=amount
                        print(customer)
                else:
                    print("insufficient balance")
                    input()
                    clear()
    def display(self):
        customers = self.get_data()
        if customers:
            account=input("enter the account number:")
            for customer in customers:
                if customer["account_no"] == account:
                    print(customer)
                    input()
                    clear()
       


def main():
    option = int(input("1.create customer\n2.deposit\n3.withdraw\n4.balance\n5.exit\n"))
    bank = BankApp()
    if option == 1:
        name = input("enter the name: ")
        b_date = input("enter the birth data: ")
        user = Customer(name=name,b_day=b_date)
        bank.add_customers(user)
    if option == 2:
        bank.deposit()
    if option == 3:
        bank.withdraw()
    if option == 4:
        bank.display()
    if option == 5:
        exit()
main()
   

# import json

# class BankAccount:
#     def __init__(self, account_number, account_holder, balance=0.0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             return f"Deposited ${amount}. New balance: ${self.balance}"
#         else:
#             return "Invalid deposit amount."

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             return f"Withdrew ${amount}. New balance: ${self.balance}"
#         else:
#             return "Insufficient funds or invalid withdrawal amount."

#     def get_balance(self):
#         return self.balance

# Helper function to save account data to a JSON file
# def save_accounts_to_json(accounts, filename):
#     with open(filename, 'w') as file:
#         json.dump(accounts, file, default=lambda o: o.__dict__, indent=4)

# # Helper function to load account data from a JSON file
# def load_accounts_from_json(filename):
#     try:
#         with open(filename, 'r') as file:
#             data = json.load(file)
#             accounts = [BankAccount(**account_data) for account_data in data]
#         return accounts
#     except FileNotFoundError:
#         return []

# # Example usage
# if __name__ == "__main__":
#     # Load existing accounts or create an empty list
#     accounts = load_accounts_from_json("accounts.json")

#     while True:
#         print("\nBank Application Menu:")
#         print("1. Create New Account")
#         print("2. Deposit Money")
#         print("3. Withdraw Money")
#         print("4. View Balance")
#         print("5. Exit")

#         choice = input("Enter your choice (1/2/3/4/5): ")

#         if choice == "1":
#             account_number = input("Enter account number: ")
#             account_holder = input("Enter account holder's name: ")
#             new_account = BankAccount(account_number, account_holder)
#             accounts.append(new_account)
#             save_accounts_to_json(accounts, "accounts.json")
#             print("Account created successfully!")

#         elif choice == "2":
#             account_number = input("Enter account number: ")
#             amount = float(input("Enter deposit amount: "))
#             for account in accounts:
#                 if account.account_number == account_number:
#                     result = account.deposit(amount)
#                     print(result)
#                     save_accounts_to_json(accounts, "accounts.json")
#                     break
#             else:
#                 print("Account not found.")

#         elif choice == "3":
#             account_number = input("Enter account number: ")
#             amount = float(input("Enter withdrawal amount: "))
#             for account in accounts:
#                 if account.account_number == account_number:
#                     result = account.withdraw(amount)
#                     print(result)
#                     save_accounts_to_json(accounts, "accounts.json")
#                     break
#             else:
#                 print("Account not found or insufficient funds.")

#         elif choice == "4":
#             account_number = input("Enter account number: ")
#             for account in accounts:
#                 if account.account_number == account_number:
#                     print(f"Account balance: ${account.get_balance()}")
#                     break
#             else:
#                 print("Account not found.")

#         elif choice == "5":
#             break

#         else:
#             print("Invalid choice. Please enter a valid option.")




