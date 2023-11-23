import json
import os
import sys

if sys.platform == "win32":
    clear = lambda : os.system("cls")
else:
    clear = lambda : os.system("clear")

filename = "invent_oops.json"
filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)),filename)

class Products:
    
    
    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price


    def product(self):
        return {
            "name" : self.name,
            "quantity" : self.quantity,
            "price" : self.price
        }
        


class Inventory(Products):
    def __init__(self,name,quantity,price):
        super().__init__(name,quantity,price)
        self.invent_products = []
    
    def store_items(self):
        
        if os.path.exists(filepath):
            
            self.invent_products = self.get_data()
            
        
        self.invent_products.append(self.product())
        self.w_data()       
        return main()   
             
    def w_data(self):
        with open(filepath,'w') as f:
            json.dump(self.invent_products,f)
        return main()    
        
    def get_data(self):
        with open(filepath) as f:
            items = json.load(f)
            return items 
        
        
    def update_item(self,p_name,p_quantity):
        items = self.get_data()
        for item in items:
            if item["name"] == p_name:
                item["quantity"] = p_quantity
                print("item updated successfully")
                input()
                clear()
            else:
                print("product not available")
                input()
                clear()
            
    def remove_product(self,p_name):
        items = self.get_data()
        for item in items:
            if item["name"] == p_name: 
                items.remove(item)

                print(items)          
                input()
                clear()

        return main()    
def main():
    clear()
    option = int(input("1.add product\n2.update product_item\n3.remove product\n4.exit()"))
    input()
    clear()
    if option == 1:
        p_name = input("enter the product:")
        p_quantity = int(input("enter the quantity:"))
        p_price = int(input("enter the price:"))
        input()
        clear()
        invent = Inventory(name=p_name,quantity=p_quantity,price = p_price)
        invent.store_items()
        invent.w_data()
    if option == 2:
        p_quantity = int(input("enter the quantity:"))
        p_name = input("enter the product:")
        invent = Inventory(name="", quantity=0, price=0)
        invent.update_item(p_name,p_quantity)
        input()
        clear()
    if option == 3:
        p_name = input("enter the product:")
        invent = Inventory(name="", quantity=0, price=0)
        invent.remove_product(p_name)
        input()
        clear()

    if option == 4:
        exit()
        


main()


      

