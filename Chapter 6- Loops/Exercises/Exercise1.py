toppings = []

while (topping := input ("Enter a topping (or 'quit' to finish): ")) != 'quit':
    toppings.append (topping)
    print (f"You've added {topping} to your pizza!")

print("\n The following toppings will be added to the pizza: ", * toppings, sep=' \n- ')