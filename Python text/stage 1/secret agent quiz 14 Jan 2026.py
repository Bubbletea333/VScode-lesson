correct_name="Agent Amber"
correct_code="Expedocious endorphins"

print("you are in the area of the secret rooms")
print("you are in front of agent Amber's room")

correct_name=(input("what is your name? "))
while correct_name != "Agent Amber":
    print("wrong Agent")
    print("probably your room is beside me")
    correct_name=(input("what is your name? "))
else:
    print("hello Agent Amber")
    correct_code=(input("What is the secret password: "))
while correct_code!="Expedocious endorphins":
    print("wrong answer")
    correct_code=(input("What is the secret password: "))
else:
    print("ACCESS GRANTED")