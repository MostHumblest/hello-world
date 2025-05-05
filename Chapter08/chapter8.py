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

#8-12
def sandwich_order(name, *toppings):
    print("\nMaking a sandwich for " +
          name.title() + "!")
    print("Sandwich with:")
    for topping in toppings:
        print("-" + topping)
sandwich_order("steve", "ham", "cheese", "mayo")
sandwich_order("katie", "bacon", "lettuce", "tomato")
sandwich_order("tomas", "pork", "pickles", "mustard", "swiss")

#8-13
def build_profile(first, last, **user_info):
    profile = {}
    profile['first']= first
    profile['last'] = last
    for k, v in user_info.items():
        profile[k] = v
    return profile
user_profile = build_profile("steve", "smith", height="tall", pet_name="larry", wife="katie")
print(user_profile)

def build_car(make, model, **details):
    this_car = {}
    this_car['make'] = make
    this_car['model'] = model
    for k,v in details.items():
        this_car[k] = v
    return this_car
my_car = build_car('vw', 'tigin', color='green', fwd='true')
print(my_car)