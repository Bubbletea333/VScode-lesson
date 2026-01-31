correct_passcode="syronevolcanicexpedocius"
correct_number=8373
access_granted=False

print("you are in the area of the one and only dangerous room")
print("you are in front of agent spoken's room")

while access_granted == False:
    correct_passcode=str(input("what is the passcode: "))
    if correct_passcode == "syronevolcanicexpedocius":
        print("correct")
        correct_number=int(input("What is the correct number: "))
        if correct_number == 8373:
            access_granted == True
            print("you are inside the room")
            break
        else:
            correct_number=int(input("Wrong,try the number again...: "))
    else:
        correct_passcode=str(input("Wrong,try the passcode again...: "))
#1. make this program more friendly
#2. FOCUS FOCUS FOCUS