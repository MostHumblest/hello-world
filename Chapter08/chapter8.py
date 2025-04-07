#8-1
def display_message():
    """prints a sentence"""
    print("we're learning about functions in chapter 8")

display_message()

#8-2
def favorite_book(title):
    """prints the name of a favorite book"""
    print("One of my favorite books is " + title.title() + ".")

favorite_book("dune")

#8-3
def make_shirt(size, message):
    """make tshirt of size with message"""
    print("\nMaking a " + size + " shirt with the message '" + message + "'.")

make_shirt('large', 'testing...')
make_shirt(size='medium', message='this is a t-shirt')

#8-4
def make_shirt(size='large', message='I love Python'):
    """make tshirt of size with message"""
    print("\nMaking a " + size + " shirt with the message '" + message + "'.")
make_shirt()
make_shirt(size='medium', message='this is a t-shirt')
make_shirt(message='this is a t-shirt')

#8-6
def city_country(city, country):
    pair = city.title() + ", " + country.title()
    return(pair)
print(city_country('boston', 'usa'))
print(city_country('paris', 'france'))
print(city_country('london', 'uk'))

#8-7
def make_album(artist, title):
    album = {'artist': artist, 'title': title}
    return album
vinyl = make_album('steve', 'white golden pup')
print(vinyl)

#8-8
while True:
    print("\nPlease enter album info:")
    print("enter 'q' to quit.")
    
    artist = input("Please enter artist: ")
    if artist == 'q':
        break
    title = input("Please enter title: ")
    if title == 'q':
        break

    print(make_album(artist, title))

#8-9
magicians = ["steve", "katie", "larry"]
def print_names(names):    
    print("\nHere is the list:")
    for n in names:
        print(n.title())
print_names(magicians)

#8-10/8-11
def make_great(names):
    great_names = []
    for n in names:
        great_names.append("The Great " + n.title())
    return great_names
great_magicians = make_great(magicians[:])
print_names(great_magicians)
print_names(magicians)

