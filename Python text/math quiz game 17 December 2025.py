import random
score=0
for i in range(10):#I need to put the for loop here so the a and b can change the numbers every time it loops
    a=(random.randint(1, 10))
    b=(random.randint(1, 10))
    answer=int(input(f"what is {a}*{b}= "))#I need to put the int data type so it doesn't
#count numbers as string
    if answer == a*b:
        print("correct!")
        score=score+1
        print(f"score:{score}")
    else:
        print("incorrect!")
        print(f"score:{score}")