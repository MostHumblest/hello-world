#6-1
person = {"firstName":"Steve",
          "lastName":"Smith",
          "age": 33,
          "city": "Boston"}

print(person["firstName"].title() + " " + 
      person["lastName"].title() + " is " + 
      str(person["age"]) + " years old and lives in " + 
      person["city"].title())

#6-2
numbers = {"steve": 73,
           "katie": 3,
           "larry": 42,
           "buzz": 8}

print("Buzz's number is: " + str(numbers["buzz"]))

#6-3
glossary = {"list":"items stored in individual indecies",
            "dictionary":"like a list but with key:value pairs",
            "for loops":"for x in y: \n\t\tdo the thing"}
print(glossary["for loops"])
for each, definition in glossary.items():
    print(each + ":")
    print("\t" + definition)

#6-4
#see above

#6-5
rivers = {
    "nile":"egypt",
    "amazon":"brazil",
    "elbe":"germany",
}

for k, v in rivers.items():
    print("The " + k.title() + " runs through " + v.title())

for k in rivers:
    print(k)
for v in rivers.values():
    print(v)

#6-6
pollees = ["katie", "steve", "larry", "buzz"]
fav_lang = {"katie":"english",
            "steve":"english",}
for name in pollees:
    if name in fav_lang.keys():
        print(name.title() + ", thank you for taking hte survey!")
    else:
        print("Good boy, " + name.title() + ", woof woof")

#6-7

person_0 = {"firstName":"Steve",
          "lastName":"Smith",
          "age": 33,
          "city": "Boston"}

person_1 = {"firstName":"Katie",
          "lastName":"Alexandridis",
          "age": 34,
          "city": "Boston"}

person_2 = {"firstName":"Russell",
          "lastName":"Brown",
          "age": 32,
          "city": "East Greenbush",
          }
people = [person_0, person_1, person_2]

for p  in people:
    print(p)

numbers = {"steve": [73, 9],
           "katie": [3, 11],
           "larry": [42],
           "buzz": [8, 14],
           }

for name, nums in numbers.items():
    print("\n"+ name.title() +"'s favorite numbers are: ")
    for num in nums:
        print(str(num))

people = {
    "ssmith": {
        'first': 'steve',
        'last': 'smith',
        'age': 33,
        'location': 'Boston',
    },
    "kalexa":{
        'first': 'katie',
        'last': 'alexandridis',
        'age':34,
        'location':'Boston',
    },
    "rbrown": {
        'first': 'russell',
        'last': 'brown',
        'age': 32,
        'location': 'east greenbush',
    }
}

for person, info in people.items():
    name = info['first'] + " " + info['last']
    age = str(info['age'])
    loc = info['location']
    print("\n" + name.title() + " is " + age + " years old and lives in " + loc.title())
