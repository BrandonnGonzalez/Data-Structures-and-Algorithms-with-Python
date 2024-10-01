# Problem 5: Restock Inventory
# Write a function restock_inventory() that updates an inventory dictionary based on a restock list. It accepts two parameters:

# current_inventory: a dictionary where each key-value pair represents an item and its current stock in the inventory
# restock_list: a dictionary where each key-value pair represents an item and the quantity to be added to the inventory
# If an item in restock_list is not present in the current_inventory, it should be added. The function should return the updated dictionary current_inventory.

# PLANNING
# 1) Loop through each entry in the restock dictionary
#   a) If the item (key) is already in the inventory, add the new quantity
#   b) If this is a new item, add it to the inventory and set the new quantity
# 2) Return the inventory once all changes have been made 

def restock_inventory(current_inventory, restock_list):
    for items, quantity in restock_list.items():
        if items in current_inventory:
            current_inventory[items] += quantity
        else:
            current_inventory[items] = quantity
    return current_inventory



# Example input

current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}

print(restock_inventory(current_inventory, restock_list))
# Example Output:


# current_inventory = {
#     "apples": 40,
#     "bananas": 15,
#     "oranges": 30,
#     "pears": 5
# }