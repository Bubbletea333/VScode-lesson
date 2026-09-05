print('fill this form so we') 
print('can proceed your registration')

print("please write your name")
name=input()
print(name)
#line 4 until 6 is how to collect data from users(beginner)

name1=str(input("please write your name: "))
print(f"Hello {name1}")
#line 6 until 10 is how to collect data from users(pro)

complete_name=str(input("please write your full name:"))
print(f"what a beautiful name {complete_name}")

age=int(input('how old are you?: '))
print(f"your age is {age}")

tall=float(input("how tall are you in meters?: "))
print(f"you are {tall} tall")

corn=bool(input("is corn a fruit?(yes/no)"))
print(f"you have guess {corn}")

print(f"{complete_name} or {name1}, {name1} is {age} years old, {name1} is {tall} tall, {name1} guessed {corn}")