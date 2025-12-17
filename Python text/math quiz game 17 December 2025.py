import random
score=0
a=(random.randint(1, 20))
b=(random.randint(1, 20))
answer=(input(f"what is {a}*{b}= "))
if answer == a*b:
    print("correct!")
else:
    print("incorrect")