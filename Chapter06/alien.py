alien_0={"color":"green", "points":5}
print(alien_0["color"])
print(alien_0["points"])

new_points = alien_0["points"]
print("You just earned " + str(new_points) + " points.")

print(alien_0)
alien_0["x_pos"] = 0
alien_0["y_pos"] = 25
print(alien_0)

alien_0 = {"color": "green"}
print(alien_0["color"])
alien_0["color"] = "yellow"
print(alien_0["color"])

alien_0 = {"x_pos":0, "y_pos": 25, "speed": "slow"}
print("Original x-pos: " + str(alien_0["x_pos"]))
if(alien_0["speed"]) =="slow":
    x_inc = 1
elif(alien_0["speed"]) =="medium":
    x_inc = 2
else:
    x_inc = 3

alien_0["x_pos"] = alien_0["x_pos"] = x_inc
print ("New x-pos: " + str(alien_0["x_pos"]))
print(alien_0)
del alien_0["speed"]
print(alien_0)
