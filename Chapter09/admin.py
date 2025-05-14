from users import User

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