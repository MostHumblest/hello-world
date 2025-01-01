#5-1
car = "subaru"
print(car =="subaru")
print(car == "audi")

#conditonal tests that I couldn't be bothered to create

#5-3
alienColor = "green"
if alienColor == "green":
    print("you scored 5pts")
alienColor = "red"    
if alienColor != "green":
    print("wrong")

#5-4
if alienColor == "green":
    print("5pts")
else:
    print("10pts")

#5-5
if alienColor =="green":
    print("5pts")
elif alienColor == "red":
    print("10pts")
elif alienColor == "yellow":
    print("15pts")
else:
    print("0pts")

#5-6
#skipped this one
#5-7
#skipped this one too

#5-8
users = ["steve", "katie", "admin", "buzz", "larry"]

for user in users:
    if user == "admin":
        print("hello admin, would you like a status report?")
    else:
        print("hello " + user + ", welcome back")

#5-9
users = []
if users:
    for user in users:
        if user == "admin":
            print("hello admin, would you like a status report?")
        else :
            print("hello " + user + ", welcome back")
else:
    print("no users!")

#5-10
currentUsers = ["steve", "katie", "admin", "buzz", "larry"]
newUsers = ["mark", "nancy", "buzz"]

for user in newUsers:
    if user in currentUsers:
        print(user.title() + ", please use a different name")
    else:
        print("welcome, " + user.title())

#5-11
ordinals = []
for number in range(1,10):
    ordinals.append(number)
print(ordinals)
for spot in ordinals:
    if spot == 1:
        print(str(spot) + "st")
    elif spot == 2:
        print(str(spot)+"nd")
    elif spot == 3:
        print(str(spot) +"rd")
    else:
        print(str(spot) + "th")
    




