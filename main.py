# Grocery Shopping Cart


# Predefined Grocery Items and Prices

grocery_items = {
    "bread": 30,
    "eggs": 6,
    "rice": 60,
    "milk": 40,
    "orange": 15,
    "apple": 20,
    "cheese": 30,  
}

cart = []

print("!!Welcome to the Grocery Shopping Cart!!")

print("Available Grocery Items: ", ", ".join(grocery_items.keys()))

while True:
    action = input("\nWhat would you like to do? (add/remove/view/checkout): ").strip().lower()
    
    if action == 'add':
        item = input("Enter the item you want to add to the cart: ").strip().lower()
        if item in grocery_items:
            cart.append(item)
            print(f"{item.capitalize()} has been added to your cart.")
        else:
            print(f"Sorry, {item} is not available in the store.")
    elif action == 'remove':
        item = input("Enter the item you want to remove from the cart: ").strip().lower()
        if item in cart:
            cart.remove(item)
            print(f"{item.capitalize()} has been removed from your cart.")
        else:
            print(f"{item.capitalize()} is not in your cart.")
    elif action == 'view':
        if not cart:
            print("Your cart is empty, continue shopping...")
        else:
            print("Items in your cart displayed below:")
            total = 0
            for item in cart:
                price = grocery_items.get(item, 0)
                total += price
                print(f"{item.capitalize()}: ${price}")
            print(f"Total cost: ${total}")
    elif action == 'checkout':
        print("Checking out. Thank you for shopping with us!")
        break
    else:
        print("Invalid action. Please choose from add, remove, view, or checkout.")
