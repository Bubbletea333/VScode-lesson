import random

guess=0
number=(random.randrange(1, 100))
guess=int(input("i have a random number between 1 until 100 can you try to guess?"))
while guess != number:    
    if guess > number:
        print("lower than that!")
        guess=int(input("try again: "))
    elif guess < number:
        print("higher than that!")
        guess=int(input("try again: "))
    else:
        break
print("BINGO")