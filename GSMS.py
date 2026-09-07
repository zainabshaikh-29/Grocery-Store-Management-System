Grocery Store Management System - Version 2.0
Features: purchase/return items, total calculation, online catalogue search
catalogue = ["Rice", "Milk", "Bread", "Sugar", "Cooking Oil"]

def purchase_item(item_id, customer_id):
print("Item", item_id, "purchased by customer", customer_id)

def return_item(item_id):
print("Item", item_id, "returned")

def calculate_total(quantity, price=50):
total = quantity * price
print("Total = Rs.", total)
return total

def search_item(item_name):
if item_name in catalogue:
print(item_name, "is available")
else:
print(item_name, "not found")
