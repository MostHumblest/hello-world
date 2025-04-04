def greet_users(names):
    """Print simple message to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

users = ['steve', 'larry', 'katie']
greet_users(users)