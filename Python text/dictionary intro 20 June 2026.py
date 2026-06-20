#How to Create a Dictionary

#Use curly braces {}.

#pet = {
#    "name": "Sparkle",
#    "species": "Dog",
#    "age": 3
#}

#Accessing Values

#Use the key inside square brackets.

#print(pet["name"])

#Output:

#Sparkle

#Changing Values
#pet["age"] = 4

#Now:

#print(pet)

#Output:

#{'name': 'Sparkle', 'species': 'Dog', 'age': 4}

#Adding New Information
#pet["favorite_food"] = "Chicken"

#Output:

#{
    #'species': 'Dog',
    #'age': 4,
    #'favorite_food': 'Chicken'
#}

#Removing Information

#del pet["species"]

#The "species" entry disappears.

#Exercises
#🟢 Level 1: Easy

#Create this dictionary:

book = {
    "title": "Harry Potter",
    "author": "J.K. Rowling",
    "pages": 300
}
#Print the title.
#Print the author.

print(book["title"])
print(book["author"])

#🟡 Level 2: Medium

#Create:

pet = {
    "name": "Sparkle",
    "hunger": 5,
    "energy": 5
}
#Change hunger to 8.
#a d d a new key called "happiness" with value 7.
#Print the whole dictionary.

pet["hunger"] = 8
pet["happiness"] = 7
print(pet)
#🔴 Level 3: Challenge

#Create a dictionary for a game character:

#Include:

#name
#health
#attack
#level

#Then:

#Increase health by 20.
#Increase level by 1.
#Print all keys.
#Print all values.

character={
    "name": "Bob",
    "health": 100,
    "attack": 90,
    "level": 999
}

character["health"]=120
character["level"]=1000
print(character.keys())
print(character.values())