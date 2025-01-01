#4-1
pizzas = ["cheese", "pepperoni", "veggie", "meatlovers"]    
for pie in pizzas:
    #print(pie)
    print("I like " + pie + " pizza")

print("I really love pizza")

#4-2
animals =["whale", "dolphin", "squid"]
for fish in animals:
    #print(fish)
    print("A " + fish + " would be a terrible pet")
print("these animals would love pizza")

#4-3
for numbers in range(1,21):
    print(numbers)

#4-4
#for numbers in range(1, 1000001):
#    print(numbers)

#4-5
numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#4-6
for numbers in range(1, 20, 2):
    print(numbers)

#4-7
for numbers in range(3, 30, 3):
    print(numbers)

#4-8
for cube in range(1, 11):
    cubes = cube**3
    print(cubes)

#4-9
cubes = [value**3 for value in range(1,11)]
print(cubes)

#4-10
print("the first three items in the list are: ")
print(cubes[0:3])
print("the middle items are:")
print(cubes[3:7])
print("the last three items are:")
print(cubes[-3:])

#4-12
myPizzas = pizzas
yourPizzas = pizzas[:]
myPizzas.append("squash")
yourPizzas.append("mushroom")
print(myPizzas)
print(yourPizzas)

for pizza in myPizzas:
    print(pizza)
for pizza in yourPizzas:
    print(pizza)

#4-13
buffet = ("lobaster", "steak", "chicken", "potatoes", "salad")
print(buffet)
buffet = ("crab", "steak", "duck", "potatoes", "salad")
print(buffet)