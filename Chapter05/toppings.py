request = "mushrooms"
if request !="anchovies":
    print("Hold the anchovies!")

toppings = ["mushrooms", "pepperoni", "cheese"]
print("mushrooms" in toppings)
print("onions" in toppings)

if "mushrooms" in toppings:
    print("adding mushroom")
if "pepperoni" in toppings:
    print("adding pepperoni")
if "onions" in toppings:
    print("adding onions")

print("Finished making your pizza")

for topping in toppings:
    print("adding " + topping)

for topping in toppings:
    if topping == "mushrooms":
        print("sorry, we are out of mushrooms")
    else:
        print("Adding " + topping)

toppings = []
if toppings:
    for topping in toppings:
        print("Adding " + topping)
else:
    print("making plain pizza")

availableToppings =["mushrooms", "olives", "green peppers", 
                    "pepperoni", "pineapple", "cheese"]
toppings = ["mushrooms", "bacon", "cheese"]

for topping in toppings:
    if topping in availableToppings:
        print("Adding " + topping)
    else:
        print("Sorry, we don't have " + topping)