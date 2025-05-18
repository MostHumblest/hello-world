import json

filename = "number.json"
with open(filename, 'r') as f_obj:
    number = json.load(f_obj)
print(str(number))