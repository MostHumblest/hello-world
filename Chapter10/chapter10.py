#10-1
filename = r'c:\Users\sasmi\Documents\GitHub\hello-world\Chapter10\learning_python.txt'
print("\nPrint entire contents:")
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.strip())

print("\nPrint by looping over object:")
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

print("\nPrint by storing and working with list:")
with open(filename) as file_object:
    lines = file_object.readlines()

doc_string = ''
for line in lines:
    doc_string += line
print(doc_string)

#10-2
print("\nPrint and replace Python:")
doc_string = doc_string.replace('Python', 'C')
print(doc_string)

#10-3
filename = "guest.txt"

print("\nSingle Entry:")
name = input("What is your name? ")
with open(filename, 'w') as file_object:
    file_object.write(name + '\n')

#10-4
print("\nMulti Entry: (type quit to exit)")
name = ''
with open(filename, 'a') as file_object:
    while name != 'quit':
        name = input("What is your name? ")
        if name == 'quit':
            break
        file_object.write(name + '\n')

#10-5
print("\n10-5 Programming Poll")
filename = "programming.txt"
name = ''
reason = ''
print("enter quit to quit")
with open(filename, 'a') as file_object:
    while name != 'quit':
        name = input("What is your name?")
        if name =="quit":
            break
        reason = input("What do you like about programming? ")
        if reason =="quit":
            break
        file_object.write(name + ' likes programming because ' + reason + '\n')

#10-6 and 10-7
print("\n10-6 Additon")
print("enter two numbers to add together")
print("enter q to quit")
while True:
    first_number = input("Enter the first number: ")
    if first_number == 'q':
        break
    second_number = input("Enter the second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except:
        print("cannot add strings")
    else:
        print('The sum is: ' + str(answer))

#10-8 and 10-9
print("\n10-8 Cat and Dog Names")
filenames = ['dogs.txt', 'cats.txt']
for filename in filenames:
    try:
        with open(filename) as f_obj:
            contents = f_obj.readlines()
    except FileNotFoundError:
        pass
    else:
        for line in contents:
            print(line.title().strip())

#10-10
print("\n10-10 Common Words")
filename = "alice.txt"
with open(filename, 'r', encoding='utf-8') as f_obj:
    contents = f_obj.read()
    count = contents.lower().count('alice')
    print(filename + " contains the word 'alice' " + str(count) + " times.")