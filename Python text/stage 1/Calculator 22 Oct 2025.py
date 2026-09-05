first_number=int(input("enter your first number: "))
second_number=int(input("enter your second number: "))
simbols=(input("choose operations +,-,%,*,/,**,//: "))

if simbols == "+":
    print(first_number+second_number)
elif simbols == "-":
    print(first_number-second_number)
elif simbols == "%":
    print(first_number%second_number)
elif simbols == "*":
    print(first_number*second_number)
elif simbols == "/":
    print(first_number/second_number)
elif simbols == "**":
    print(first_number**second_number)
elif simbols == "//":
    print(first_number//second_number)
else:
    print("enter correct simbol")