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

print("\nMulti Entry: (type quit to exit)")
name = ''
with open(filename, 'a') as file_object:
    while name != 'quit':
        name = input("What is your name? ")
        if name == 'quit':
            break
        file_object.write(name + '\n')
    