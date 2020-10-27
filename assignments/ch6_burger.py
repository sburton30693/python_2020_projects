# Spencer Burton
# Chapter 6 Burger Castle

# Valid Orders Tuples
validOrders = ("burger", "fries", "salad", "soda", "milkshake")
itemDescriptions = ("Half-pound burger", "Large fries", "Side salad", "Diet root beer", "Chocolate shake")

# Customers order
order = []

# Print Introduction
print("Welcome to Burger Castle")
print("Menu:", validOrders)
print("Please enter each item in your order. Press 'Enter' or type 'quit' on an empty line when done.")


# Get user input for items in a do-while loop
while True :
    item = input("Enter Item: ")

    if item == "" or item == "quit" :
        break
    elif item in validOrders :
        order.append(item)
    else :
        print("Sorry, we don't sell", item)    

# Display order to user
print()
print("Order complete; you are having:")

for item in order :
    index = validOrders.index(item)
    description = itemDescriptions[index]
    print(description)

print("Thanks for visiting Burger Castle!")
