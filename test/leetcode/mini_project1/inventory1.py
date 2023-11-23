
import json

# Initialize an empty inventory dictionary
inventory = {}

# Function to save the inventory to a JSON file
def save_inventory_to_json(filename):
    with open(filename, 'w') as json_file:
        json.dump(inventory, json_file)

# Function to load the inventory from a JSON file
def load_inventory_from_json(filename):
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        return {}

# Main loop to interact with the inventory system
while True:
    print("\nOptions:")
    print("1. Add product to inventory")
    print("2. Remove product from inventory")
    print("3. Update product quantity")
    print("4. Display inventory")
    print("5. Save inventory to JSON")
    print("6. Load inventory from JSON")
    print("7. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5/6/7): ")
    
    if choice == '1':
        product_name = input("Enter the product name: ")
        quantity = int(input("Enter the quantity to add: "))
        if product_name in inventory:
            inventory[product_name] += quantity
        else:
            inventory[product_name] = quantity
        print(f"{quantity} {product_name}(s) added to the inventory.")
    elif choice == '2':
        product_name = input("Enter the product name: ")
        quantity = int(input("Enter the quantity to remove: "))
        if product_name in inventory:
            if inventory[product_name] >= quantity:
                inventory[product_name] -= quantity
            else:
                print(f"Error: Not enough {product_name} in inventory.")
        else:
            print(f"Error: {product_name} not found in inventory.")
    elif choice == '3':
        product_name = input("Enter the product name: ")
        quantity = int(input("Enter the new quantity: "))
        inventory[product_name] = quantity
    elif choice == '4':
        print("Current Inventory:")
        for product, quantity in inventory.items():
            print(f"{product}: {quantity}")
    elif choice == '5':
        filename = input("Enter the filename to save the inventory (e.g., inventory.json): ")
        save_inventory_to_json(filename)
        print("Inventory saved to JSON file.")
    elif choice == '6':
        filename = input("Enter the filename to load the inventory from (e.g., inventory.json): ")
        inventory = load_inventory_from_json(filename)
        print("Inventory loaded from JSON file.")
    elif choice == '7':
        print("Exiting the inventory management system.")
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4/5/6/7).")




