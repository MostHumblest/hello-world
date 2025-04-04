def describe_pet(type, name):
    """Display info about a pet"""
    print("\nI have a " + type + ".")
    print("My " + type + "'s name is " + name.title() + ".")

describe_pet('golden', 'larry')
describe_pet(name = 'buzz', type = 'labrador')