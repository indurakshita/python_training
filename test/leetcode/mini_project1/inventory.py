import json
import os
import sys

filename ="invent_item_details.json"


if sys.platform == "win32":
    clear = lambda: os.system("cls")
else:
    clear = lambda: os.system("clear")

def w_data(data=None):
    with open(filename,"w") as f:
        json.dump(data,f)
    return data
 

def get_data(data=None):
    with open(filename) as f:
        data = json.load(f)
    return data


def add_item():  
    if not os.path.exists(filename):
        w_data() 
        add_item()
    else:   
        name = input("enter the name of the item:")
        quantity = int(input("enter the quantity of the item:"))
        price = int(input("enter the price of the item:"))  
        data=get_data()
        if data:
            for item in data:
                if item["name"]==name:
                    print("items already exists")
                    input()
                    clear()
                    return display()  
            item_data={"name":name,"quantity":quantity,"price":price}
            data.append(item_data)
            w_data(data)
            return display() 
        else:
            data=[] 
            item_data={"name":name,"quantity":quantity,"price":price}
            data.append(item_data)
            w_data(data)
            return display() 

def view():
    data=get_data()
    if data:
        i_name=input("enter the item name:")
        for item in data:
            if item["name"]==i_name:
                clear()
                print("Item Details:\n")
                print(f"Item:".ljust(20),f"{item['name']}")
                print(f"Quantity:".ljust(20),f"{item['quantity']}")
                print(f"Price:".ljust(20),f"{item['price']}")
                input()
                return display()
    else:
        print("no data available") 
        input() 
        clear() 
        return display()
        
        
def update_item():
    data=get_data()
    if data:
        i_name=input("enter the item name:")
        for item in data:
            if item["name"]!=i_name:
                print("no data available") 
                input() 
                clear() 
                return display()
            else:
                item["price"]=int(input("enter the price"))
                
                w_data(data)   
                print("value of item has been changed")
                input()
                clear()
                return display()

def remove_product():
    data=get_data()
    if data:
        i_name=input("enter the item name:")
        for item in data:
            if item["name"]==i_name:
                del data[item]
                w_data(data)
                print(f"product {i_name} removed")
                input()
                clear()
                return display()

def current_inventory():
    data=get_data()
    if data:
        print("Display current inventory\n")
        for item in data:
            print(f"product name is: {item['name']}\n")
            print(f"Item:".ljust(20),f"{item['name']}")
            print(f"Quantity:".ljust(20),f"{item['quantity']}")
            print(f"Price:".ljust(20),f"{item['price']}\n")
                
        w_data(data)
        input()
        clear()
        return display()


def display(): 
    options=int(input("1. View\n2. add item\n3.Update item\n4.Remove item\n5.Curent Inventory items\n6.Exit\n"))
    func={
        1:view,
        2:add_item,
        3:update_item,
        4:remove_product,
        5:current_inventory,
        6:exit    
    }
    clear()
    return func[options]() 

def exit():
    print("Exiting Inventory Store...")
    input()

    
def main():
    try:
        display()
    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    main() 


