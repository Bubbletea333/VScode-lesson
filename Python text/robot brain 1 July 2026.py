print("welcome")
print("you are standing near a robot")

robotbrain={
    "hello" : "hi",
    "joke"  : "Why did the banana go to the doctor? Because it wasn't peeling well!",
    "name"  : "my name is LYRA",
    "moon"  : "Because the Moon has no wind or weather, the footprints left by Apollo astronauts will stay there for millions of years.",
    "bye"   : "bye have a great day",
    "who are you" : "I'm ROj979879, you can call me LYRA, an AI assistant created by OpenAI. I'm here to help with a wide range of tasks"
}
#while robotbrain != "bye":#if we did not leave
#   robotquestion=(input("try to say something: ")).lower()# we need to say something to the robot
# solution
while True:

    robotquestion = input("Try to say something: ").lower().strip()

    if robotquestion == "bye":
        print(robotbrain["bye"])
        break

    elif robotquestion=="hello":
        print(robotbrain["hello"])
    elif robotquestion=="joke":
        print(robotbrain["joke"])
    elif robotquestion=="name":
        print(robotbrain["name"])
    elif robotquestion=="moon":
        print(robotbrain["moon"])
    elif robotquestion=="who are you":
        print(robotbrain["who are you"])
    else:
        print("I'm not programed for this")

#if robotquestion == "bye":
#    print(robotbrain["bye"]) cannot add break