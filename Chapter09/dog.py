class Dog():
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """initialize name and age atributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting"""
        print(self.name.title() + " is sitting")
    
    def roll_over(self):
        """simulate rolling over"""
        print(self.name.title() + " rolled over!")

my_dog = Dog('larry', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " +str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('buzz', 8)
print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
