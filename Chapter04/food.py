myFood=["pizza", "pasta", "pie"]
yourFood = myFood[:]

print(myFood)
print(yourFood)

myFood.append("pirogi")
yourFood.append("pizza")

print(myFood)
print(yourFood)

#this sets on list to the other list
yourFood = myFood
myFood.append("pizza")

print(yourFood)