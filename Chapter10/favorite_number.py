import json

filename = "chapter10/number.json"

def read_number():
    """reads number if it exists"""
    try:
        with open(filename, 'r') as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number

def get_number():
    """ gets a number from user if it doesn't exist"""
    number = input("What is your favorite number? ")
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
    return number

def display_number():
    """prints results"""
    number = read_number()
    if number:
        print("Your number is: " + str(number))
    else:
        number = get_number()
        print("We'll store your number: " + str(number))

display_number()