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

