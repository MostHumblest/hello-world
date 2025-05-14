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