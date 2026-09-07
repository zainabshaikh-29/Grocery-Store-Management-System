# Grocery Store Management System - Version 1.1
# Features: purchase and return items, price calculation

def purchase_item(item_id, customer_id):
print("Item", item_id, "purchased by customer", customer_id)

def return_item(item_id):
print("Item", item_id, "returned")

def calculate_total(quantity, price=50):
total = quantity * price
print("Total = Rs.", total)

return total
