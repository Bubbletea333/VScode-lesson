import random

guess=0
number=(random.randint(1, 50))
guess=int(input("i have a random number between 1 until 50 can you try to guess?"))

while guess != number:
    if guess > number:
        print(input("lower than that!"))
    elif guess < number:
        print(input("higher than that!"))
