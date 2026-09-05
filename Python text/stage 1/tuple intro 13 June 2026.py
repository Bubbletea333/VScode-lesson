#pets = ("Sparkle", "Cookie", "Fluffy")

#print(pets[-1])

#pets = ("Sparkle", "Cookie", "Fluffy", "Milo")

#print(pets[1:3])

#pets = ("Sparkle", "Cookie", "Fluffy")

#for sleep in pets:
    #print(sleep)

#numbers = (1, 2, 2, 2, 2, 2, 2, 2, 3)

#print(numbers.count(2))#it counts how many twos are there

#🟢 Level 1

#Create a tuple:

pets = ("Sparkle", "Cookie", "Fluffy")
#Print the first pet.
#Print the last pet.
#Print the second pet.
print(pets[0])
print(pets[2])
print(pets[1])
#🟡 Level 2
colors = ("red", "blue", "green", "yellow")
#Print the first 2 colors using slicing.
#Print the last 2 colors using slicing.
print(colors[0:2])
print(colors[2:4])
#🔴 Level 3
scores = (90, 85, 90, 100, 90)
#How many times does 90 appear?
#What is the index of the first 100?
print(scores.count(90))
print(scores.index(100))
#(Hint: use .count() and .index())