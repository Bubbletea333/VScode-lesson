height=int(input("what is your height in centimeters= "))
weight=int(input("what is your weight in kilograms= "))

height=(height/100)
bmi=(weight/(height*height))

if bmi <= 16:
    print("you are severely underweight")
elif bmi <= 18.5:
    print("you are underweight")
elif bmi <= 25:
    print("you are healthy")
elif bmi >= 30:
    print("severely overweight")
else :
    print("fill the height and weight properly")