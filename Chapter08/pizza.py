def make_pizza(*toppings):
    """Print the list of toppings that have been requested """
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green_peppers', 'extra cheese')

def make_pizza(size, *toppings):
    """summarize the pizza which about to be made"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)

make_pizza(16, 'pepperoini')
make_pizza(12, "mushrooms", "green peppers", "extra cheese")