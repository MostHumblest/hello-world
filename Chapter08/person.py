def build_person(first, last, age=''):
    """return a dictionary about a perosn"""
    person = {'first':first, 'last':last}
    if age:
        person['age'] = age
    return person
musician =  build_person('jimi', 'hendrix', age = 27)
print(musician)