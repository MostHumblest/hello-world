alien_0 = {"color": "green", "points":5}
alien_1 = {"color": "yellow", "points":10}
alien_2 = {"color": "red", "points":15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("...")
aliens = []

for alien_number in range(30):
    new_alien = {"color": "green", "points":5, "speed":"slow"}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["points"] = 10
        alien["speed"] = "medium"

for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))

for alien in aliens[0:5]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["points"] = 10
        alien["speed"] = "medium"
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["points"] = 15
        alien["speed"] = "fast"

for alien in aliens[:7]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))

pizza = {
    "crust":"thick",
    "toppings": ["mushrooms", "extra cheese"],
}

print("You ordered a " + pizza["crust"] + "-crust pizza "+
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)
