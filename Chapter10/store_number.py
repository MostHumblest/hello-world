import json

filename = "number.json"
number = input("What is your favorite number? ")
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)