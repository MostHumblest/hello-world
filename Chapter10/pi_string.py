file_path = r'c:\Users\sasmi\Documents\GitHub\hello-world\Chapter10\pi_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

filename = r'c:\Users\sasmi\Documents\GitHub\hello-world\Chapter10\pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
    print(pi_string[:52] + "...")
    print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("your birthday appears in the listed digits of pi!")
else:
    print("your birthday was not found.")