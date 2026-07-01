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

#--------------------------------------
#Dictionary intro part 2
#--------------------------------------
#Loop
#------
#Example
#-----------
#Print all key names in the dictionary, one by one:
#for x in thisdict:
#  print(x)
#--------------------------------------
#Example
#--------------------------------------
#Print all values in the dictionary, one by one:
#for x in thisdict:
#  print(thisdict[x])
#--------------------------------------
#Example
#--------------------------------------
#You can also use the values() method to return values of a dictionary:
#for x in thisdict.values():
#  print(x)


#--------------------------------------
#COPY A DICTIONARY
#Example
#--------------------------------------
#Make a copy of a dictionary with the copy() method:
#thisdict = {
#  "brand": "Ford",
#  "model": "Mustang",
#  "year": 1964
#}
#mydict = thisdict.copy()
#print(mydict)
#Another way to make a copy is to use the built-in function dict().
#--------------------------------------
#Example
#--------------------------------------
#Make a copy of a dictionary with the dict() function:
#thisdict = {
#  "brand": "Ford",
#  "model": "Mustang",
#  "year": 1964
#}
#mydict = dict(thisdict)
#print(mydict)


#--------------------------------------
#NESTED DICTIONARY
#Example
#Create a dictionary that contain three dictionaries:
#--------------------------------------
#myfamily = {
#  "child1" : {
#    "name" : "Emil",
#    "year" : 2004
#  },
#  "child2" : {
#    "name" : "Tobias",
#    "year" : 2007
#  },
#  "child3" : {
#    "name" : "Linus",
#    "year" : 2011
#  }
#}
#--------------------------------------
#Access Items in Nested Dictionaries
#To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
#--------------------------------------
#Example
#Print the name of child 2:
#print(myfamily["child2"]["name"])
#--------------------------------------
#Loop Through Nested Dictionaries
#You can loop through a dictionary by using the items() method like this:
#--------------------------------------
#Example
#Loop through the keys and values of all nested dictionaries:
#--------------------------------------
#for x, obj in myfamily.items(): check your dictionary values one by one then grabs each values to save it in "x" after that it bundles them to "obj"
#  print(x) print the values
#  for y in obj: rename obj into y
#    print(y + ':', obj[y]) it prints the keys then the values

#Dictionary Methods
#Python has a set of built-in methods that you can use on dictionaries.
#Method	Description
#--------------------------------------
#clear():	Removes all the elements from the dictionary
#copy():	Returns a copy of the dictionary
#fromkeys():	Returns a dictionary with the specified keys and value
#get():	Returns the value of the specified key
#items():	Returns a list containing a tuple for each key value pair
#keys():	Returns a list containing the dictionary's keys
#pop():	Removes the element with the specified key
#popitem():	Removes the last inserted key-value pair
#setdefault():	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update():	Updates the dictionary with the specified key-value pairs
#values():	Returns a list of all the values in the dictionary