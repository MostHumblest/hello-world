from car import ElectricCar

my_ford = ElectricCar("ford", "mach e", 2023)

print(my_ford.get_descriptive_name())
my_ford.battery.describe_battery()
my_ford.battery.get_range()