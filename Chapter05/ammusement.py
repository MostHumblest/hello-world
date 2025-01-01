age = 12
if age<4:
    print("your admission cost is $0.")
elif age<18:
    print("your admission cost is $5")
else:
    print("your admission cost is $10")

age = 12
if age<4:
    price = 0
elif age<18:
    price = 5
else:
    price = 10

print ("Because your age is " + str(age) + ", your admission cost is: $" + str(price) +".")

age = 33
if age<4:
    price = 0
elif age<18:
    price = 5
elif age>65:
    price = 5
else:
    price = 10

print ("Because your age is " + str(age) + ", your admission cost is: $" + str(price) +".")
