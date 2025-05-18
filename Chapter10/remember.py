import json

#load the username, if it has been stored previously.
#Otherwise, prompt the username and store it.

def get_stored_username():
    """get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def verify_user(username):
    response = input("Are you " + username + "? (y/n) ")
    if response == 'y':
        return True
    else:
        return False
    
def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    last_user = verify_user(username)
    if last_user:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("we'll remember you when you come back, " + username + "!")

greet_user()