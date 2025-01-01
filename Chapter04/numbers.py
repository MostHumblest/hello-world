for value in range(1,5):
    print(value)
#only prints 1-4, because for loop stops at 5

#prints 1-5
for value in range(1,6):
    print(value)

#range direct to list
numbers = list(range(1,6))
print(numbers)

#range and skip numbers
evenNumbers = list(range(2, 11, 2))#adds 2 after starting number
print(evenNumbers)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

#list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)