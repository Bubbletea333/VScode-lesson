import random

number=(random.randint(1, 100))
guess=int(input("i have a random number between 1 until 100 can you try to guess?"))
while guess >= number:
    print(input("lower than that!"))
else:
    print(input("higher than that!"))

if guess == number:
    print("BINGO")
    print(f"your total guess is {guess}")