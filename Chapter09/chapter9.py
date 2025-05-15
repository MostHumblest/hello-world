#9-1
class Restaurant():
    """defines a new restaurante"""
    def __init__(self, name, cuisine):
        """creates the restaurant"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0 #from 9-4
    
    def describe(self):
        """prints descrtiption"""
        print(self.name.title() + " is a " + self.cuisine + " restaurant.")
        print(self.name.title() + " has served " + str(self.number_served)+ " customers.")
    
    def open(self):
        """print that restaurant is open"""
        print(self.name.title() + " is now open")

    def set_number_served(self, number): #from 9-4
        """update number served"""
        self.number_served = number

    def increment_number_served(self):
        """increase number served"""
        self.number_served += 1

my_place = Restaurant("taco bell", "mexican")
my_place.describe()
my_place.open()

#9-2
rest_one = Restaurant("wendys", "burger")
rest_two = Restaurant("shore leave", "sushi")
rest_one.describe()
rest_two.describe()

#9-3
class User():
    """creates a user"""
    def __init__(self, first, last, **attributes):
        """create user information"""
        self.first = first
        self.last = last
        self.attempts = 0
        self.deets = {}
        for k, v in attributes.items():
            self.deets[k] = v
    
    def describe(self):
        """prints user info"""
        print("info about " + self.first.title() + " " + self.last.title() + ":")
        for k, v in self.deets.items():
            if k == "privilages":
                print("admin:true")
            else:
                print(k + ":" + v)
    
    def greet(self):
        """prints a greeting"""
        print("Hello " + self.first.title() + ", it's great to see you!")

    def inc_logins(self):
        """increment login attempts by 1"""
        self.attempts += 1
    
    def reset_attempts(self):
        """resets login attempts"""
        self.attempts = 0

steve = User("steve", "smith", height="tall", married="yes")
steve.describe()
steve.greet()

#9-4
dominos = Restaurant('dominos', 'italian')
dominos.describe()
dominos.set_number_served(45)
dominos.describe()
dominos.increment_number_served()
dominos.describe()

#9-5
#add login_attempts to 9-3
larry = User("larry", "alexandrids", species="dog", breed="golden")
larry.greet()
larry.inc_logins()
larry.inc_logins()
larry.inc_logins()
print(larry.first.title() + " has attempted to login in " + str(larry.attempts) + " times.")
larry.reset_attempts()
print(larry.first.title() + " has attempted to login in " + str(larry.attempts) + " times.")

#9-6
class IceCreamStand(Restaurant):
    """class to create ice cream stand as restaurant"""
    def __init__(self, name, cuisine="ice cream"):
        """initiate the icecream stand"""
        super().__init__(name, cuisine)
        self.flavors = []

    def create_flavors(self, *flavors):
        for flavor in flavors:
            self.flavors.append(flavor)
    
    def list_flavors(self):
        """lists the flavors of the ice cream stand"""
        print(self.name + " offers these ice cream flavors:")
        for flavor in self.flavors:
            print("-" + flavor)
DQ = IceCreamStand("DQ")
DQ.create_flavors("chocolate", "vanilla", "strawberry")
DQ.list_flavors()
DQ.describe()

#9-7 and 9-8
class Admin(User):
    """creates admin based on user class"""
    def __init__(self, first, last, **attributes):
        """init the admin"""
        super().__init__(first, last, **attributes)   
        self.priviages = Privilages() 

class Privilages():
    def __init__(self):
        self.privilages_list = ["can add post", "can delete post", "can ban user"]

    def show_privilages(self):
        """list admin privilages """
        print("This user is an admin and has these privilages:")
        for item in self.privilages_list:
            print("-" + item)

steve = Admin("steve", "smith", user="true", married="true", dog="larry")
steve.describe()
steve.priviages.show_privilages()

#9-9 see electric car.py

#9-14
from random import randint
class Die():
    def __init__(self, number):
        """inits a die with input number of sides"""
        self.num_sides = number
    
    def roll_die(self, number):
        """rolls die given number of times"""
        for spot in range(0,number):
            x = randint(1, self.num_sides)
            print("roll " + str(spot+1) + ": " + str(x))

six_sided = Die(6)
ten_sided = Die(10)
twenty_sided = Die(20)

six_sided.roll_die(10)
ten_sided.roll_die(10)
twenty_sided.roll_die(10)