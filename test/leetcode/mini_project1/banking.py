import json
import pathlib
import os
import sys


if sys.platform == "win32":
    clear = lambda: os.system("cls")
else:
    clear = lambda: os.system("clear")


# print(os.listdir(r"C:\Users\Albia\Desktop\Training"))
FILENAME = "database.json"
FILEPATH = pathlib.Path(__file__).resolve().parent / FILENAME

def write_db(data=None):
    with open(FILEPATH, "w") as f:
        f.write(json.dumps(data))
    return data


def get_db():
    data = None
    if os.path.exists(FILEPATH):
        with open(FILEPATH) as f:
            data = json.load(f)
    return data




def view(): 
    data = get_db()
    if data:
        a_num = int(input("Enter account number: "))
        for user in data:
            if a_num == user["account_number"]:
                clear()
                print("\tUser Details")
                print(f"{'Name': <10}: {user['name']}")
                print(f"{'Age': <10}: {user['age']}")
                print(f"{'Account No': <10}: {user['account_number']}")
                print(f"{'Balance': <10}: {user['balance']}")
                input()
                clear()
                return display()
    else:
        print("No data available")
        input()
        clear()
        return display()


def deposit():
    a_num = int(input("Enter account number: "))
    amount = int(input("Enter amount:"))
    
    data = get_db()
    for user in data:
        if a_num == user["account_number"]:
            user.update({"balance": user["balance"] + amount})
    
    write_db(data)
    input("Amount deposited sccessfully")
    clear()
    return display()
            

def withdraw():
    a_num = int(input("Enter account number: "))
    amount = int(input("Enter amount:"))
    
    data = get_db()
    for user in data:
        if a_num == user["account_number"]:
            if not user["balance"] > amount:
                input("Insufficient balance")
            else:
                user.update({"balance": user["balance"] - amount})
                write_db(data)
                input("Amount Withdrawed sccessfully")
    
    clear()
    return display()
    
    
def balance():
    a_num = int(input("Enter account number: "))
    data = get_db()
    
    for user in data:
        if a_num == user["account_number"]:
            input(f"Hello {user['name']}!! Your balance is {user['balance']}")
    clear()
    return display()

 
def display():
    clear()
    print("\t Banking System".center(100))
    
    option = int(input("1. view\n2. create account\n3. deposit\n4. withdraw\n5. current balance\n6. Exit\n"))
    
    funcs = {
        1: view,
        2: create_account,
        3: deposit,
        4: withdraw,
        5: balance,
        6: exit
    }
    clear()
    return funcs[option]()
    

def create_account():
    if not os.path.exists(FILEPATH):
        write_db()
        create_account()

    else:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        data = get_db()
        default = 111111111
        if data:
            default = max([i.get("account_number", default) for i in data]) + 1
        else:
            data = []
        user = {"name": name, "age": age, "account_number": default, "balance": 100}
        data.append(user)
        write_db(data)

    input("account created successfully\n")
    clear()
    return display()
            
            
def main():
    try:
        display()
    except KeyboardInterrupt:
        
        exit(code="Exiting Bank...")
            

if __name__ == "__main__":
    main()

