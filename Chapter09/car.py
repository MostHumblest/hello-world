"""A set of classes to represent gas and electric cars"""

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """initialize attributes to descrive a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """return neatly formatted name."""
        long_name = str(self.year)+ ' ' + self.make.title() + " " + self.model.title()
        return long_name.title()
    
    def read_odometer(self):
        """show car's milage"""
        print("This car has "+ str(self.odometer_reading) + " miles on it")

    def update_odometer(self, milage):
        """
        set the odometer reading
        reject the reading if rolling back
        """
        if milage > self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back the milage")
    
    def increment_odometer(self, miles):
        """increase odo by amount"""
        self.odometer_reading += miles

class ElectricCar(Car):
    """add electric aspects to car"""
    def __init__(self, make, model, year):
        """initialize attributes of parent class."""
        super().__init__(make, model, year)   
        self.battery = Battery()

    def fill_gas_tank(self):
        """override gas tank for electric car"""
        print("Electric cars don't need gas.")

class Battery():
    """A simple class to model the battery for an electric car"""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        """print a statement to describe battery size"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """print a statement about the range this battery provides"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "this car can go approcimately " + str(range)
        message += " miles on a full charge."
        print(message)

    #9-9
    def upgrade_battery(self):
        """upgrade battery if not already upgraded"""
        if self.battery_size < 85:
            self.battery_size = 85
