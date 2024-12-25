#3-4
guestList = ["katie", "steve", "larry"]
print(guestList[0]+ ", you are inivted to dinner!")
print(guestList[1]+ ", you are invited to dinner!")
print(guestList[-1]+", you are invited to dinner!")

#3-5
popList = guestList.pop(1)
print("oh no, "+popList+" can't make it!")
print(guestList)
guestList.append("buzz")
print(guestList)

print(guestList[0].title()+ ", you are inivted to dinner!")
print(guestList[1].title()+ ", you are invited to dinner!")
print(guestList[-1].title()+", you are invited to dinner!")

#3-6
guestList.insert(0, popList)
guestList.insert(2, "otis")
guestList.append("bear")
print(guestList)

#3-7

#3-8
places=["tokyo", "london", "berlin", "nyc", "boston", "chicago"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

#3-9
print(len(guestList))

#3-10
