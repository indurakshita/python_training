'''Question 5: Create a class BankAccount with attributes account_number and balance. 
Then, create a subclass SavingsAccount that inherits from BankAccount 
and has a method calculate_interest to compute the interest earned on the balance.'''

class BankAccount:
    def __init__(self,account_number,balance,interest,year):
        self.account = account_number
        self.balance = balance
        self.interest = interest
        self.year = year

    @property
    def cal_interest(self):
       return (self.interest/100) * self.balance *self.year
        
    def tot_bal(self):
        tot_amount = self.balance + self.cal_interest
        print(f"total amount is:{tot_amount}")

    def offers(self):
        return f"No offers"


class SavingsAccount(BankAccount):
    def __init__(self,account_number,balance,year):
        self.__interest = 3
        super().__init__(account_number,balance,self.__interest,year)

    def offers(self):
        return f"zero balance,debit card"
        
    def __str__(self):
        return f"Total balance is:{self.tot_bal}"
    

class CurrentAccount(BankAccount):
    
    def __init__(self,account_number,balance,year):
        self.__interest = 4
        super().__init__(account_number,balance,self.__interest,year)
        
    def __str__(self):
        return f"Total balance is:{self.tot_bal}"
    
    def offers(self):
        return f"zero balance,credit card"
    
# sa = SavingsAccount(account_number = 1111111,balance = 2000,year = 2)
# sa.tot_bal()
# print(sa.offers())

