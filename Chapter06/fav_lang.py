fav_langs = {
    "jen" : "python",
    "sarah" : "c",
    "edward":"ruby",
    "phil":"python",
}

print("Jen's favorite language is " +
      fav_langs["jen"].title() + 
      ".")

for k, v in fav_langs.items():
    print(k.title() + "'s favorite language is " +
          v.title() + ".")
    
for name in fav_langs.keys():
    print(name.title())

for name in fav_langs:
    print(name)

for value in fav_langs.values():
    print(value)

friends = ["phil", "sarah"]
for name in fav_langs:
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              fav_langs[name].title() + "!")
if "erin" not in fav_langs:
    print("Erin, please take our poll!")

for name in sorted(fav_langs):
    print(name.title() + ", thank you for taking the poll")

print("the following languages have been mentioned:")
for lang in fav_langs.values():
    print(lang.title())

print("the following unique languages have been mentioned:")
for lang in set(fav_langs.values()):
    print(lang.title())

print('.......')
favorite_language = {
    "jen":["python", "ruby"],
    "sarah":["c"],
    "edward":["ruby", "go"],
    "phil":["python", "haskell"],
}

for name, languages in favorite_language.items():
    print("\n" + name.title()+"'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())