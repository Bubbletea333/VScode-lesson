height=int(input("what is your height in centimeters= "))
weight=int(input("what is your weight in kilograms= "))

height=(height/100)
bmi=(weight/(height*height))
print(bmi)

if bmi <= 16 and bmi<18:
    print("you are severely underweight")
elif bmi <= 18.5 and bmi<24:
    print("you are underweight")
elif bmi <= 25 and bmi<29:
    print("you are healthy")
elif bmi >= 30 and bmi<50:
    print("severely overweight")
else :
    print("fill the height and weight properly")