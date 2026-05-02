fruits = ["apple", "banana", "orange"]

print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[2])   # orange
#line 3 until 5 is a positive index it always starts from the left with 0
print(fruits[-1])  # orange
print(fruits[-2])  # banana
#line 7 and 8 is a negative index it always starts from the right with -1
fruits[1] = "grape"
print(fruits)
#line 10 is how to change an item inseide a list

#exercise 1
colors = ["red", "blue", "green"]
#👉 Print:first color and last color

print(colors[0])
print(colors[-1])

#exercise 2
#What will this print?
nums = [10, 20, 30]
print(nums[1])
#Answer= 20

#🟡 Level 2 – Medium
#Fix the code:
animals = ["cat", "dog", "bird"]
print(animals[2])
#Answer= change the animals[3] to [2] because the first word is always 0

#Change "banana" to "mango":
fruits = ["apple", "banana", "orange"]
#answer=
fruits[1] = "mango"
print(fruits)
