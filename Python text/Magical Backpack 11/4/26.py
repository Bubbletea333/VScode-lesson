print("you suddenly woke up in a closed shop")
print("\nyou saw the exit but is was locked it needs a key")
print("you need to find the correct key to open it")

magical_backpack=[]
in_danger= True

while in_danger==True:
    print(f"\nyour backpack contains: {magical_backpack}")
    print("\nwhat will you do")
    print("1. try to find the correct key and put it in your backpack")
    print("2. throw something from your backpack")
    print("3. try to open the door")
    print("4. give up and will be there for 100 years")
    player=(input("what will you pick: "))

    if player =="1":
        pick=(input("what did you find: "))
        magical_backpack.append(pick)
        print(f"you inserted {pick} into your magical backpack")
