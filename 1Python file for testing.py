# Sample Python file for testing
 
def calculate_total(price, quantity):
    return price * quantity
 
 
product = {
    "id": 1001,
    "name": "Laptop",
    "category": "Electronics"
}
 
total = calculate_total(250, 3)
 
print(f"Product: {product['name']}")
print(f"Total: {total}")
 
users = ["Alice", "Bob", "Charlie"]
 
for user in users:
    print(f"Welcome {user}")