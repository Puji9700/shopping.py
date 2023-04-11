# Create an empty dictionary to represent the shopping cart
shopping_cart = {}

# Create a function to add items to the shopping cart
def add_item(item_name, item_price):
    if item_name in shopping_cart:
        shopping_cart[item_name] += item_price
    else:
        shopping_cart[item_name] = item_price

# Add some items to the shopping cart
add_item("milk", 5)
add_item("Bread", 2.25)
add_item("eggs", 6.75)

# Print the contents of the shopping cart
print("Shopping Cart:")
for item in shopping_cart:
    print(item + " - $" + str(shopping_cart[item]))

# Calculate the total cost of the shopping cart
total_cost = sum(shopping_cart.values())
print("Total cost: $" + str(total_cost))
