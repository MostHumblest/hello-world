
print("\n********")
#7-1
rental = input("What kind of car would you like? ")
print("Let me see if I can find you a " + rental)
print("\n********")

#7-2
count = input("How many people are in your party? ")
count = int(count)
if count < 8:
    print("\nYour table is ready")
else:
    print("\nYour table will be ready shortly")
print("\n********")

#7-3
number = input("Please enter a number: ")
number = int(number)

if number % 10 == 0:
    print(str(number) + " is a multiple of 10!")
else:
    print(str(number) + " is not a multiple of 10...")
print("\n********")

#7-4
prompt = "\nWhat would you like on your pizza? "
prompt += "\nEnter 'quit' when done. "
topping = ""
while topping != 'quit':
    topping = input(prompt)
    if topping == 'quit':
        break
    print("\nAdding " + topping + " to your pizza.")

print("\n********")
#7-5
prompt = "\nEnter your age to get pricing:"
prompt += "\nEnter 'quit' when done. "
active = True
while active:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age <= 3:
        print("\nYour ticket is free.")
    elif age <= 12:
        print("\nYour ticket is $10")
    else:
        print("\nYour ticket is $15")

#7-6
#see above

#7-7
#inifinte loop

print("\n********")
#7-8
orders = ['tuna', 'italian', 'blt', 'club']
finished = []
while orders:
    sandwich = orders.pop()
    finished.append(sandwich)
print("\nMade these sandwiches:")
for s in finished:
    print(s)

print("\n********")
#7-9
orders = ['tuna', 'pastrami', 'italian', 'pastrami', 'blt', 'club', 'pastrami']
finished = []
while 'pastrami' in orders:
    print("Sorry, we're out of Pastrami")
    orders.remove('pastrami')
while orders:
    sandwich = orders.pop()
    finished.append(sandwich)
print("\nMade these sandwiches:")
for s in finished:
    print(s)

print("\n********")
#7-9
places = {}
active = True
while active:
    name = input("\nWhat's your name? ")
    loc = input("Where do you want to travel? ")
    places[name] = loc
    cont = input("Continue? (y/n) ")
    if cont == 'n':
        break
for people, locs in places.items():
    print("\nWhere do people want to go?")
    print(people.title() + " wants to go to " + locs.title() + ".")