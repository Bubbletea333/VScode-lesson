print("you suddenly woke up in a closed shop")
print("\nyou saw the exit but is was locked it needs a key")
print("you need to find the correct key to open it")

magical_backpack=[]
in_danger= True

while in_danger==True:
    print(f"\nyour backpack contains: {magical_backpack}")
    print("\nwhat will you do")
    print("1. try to find the 'Correct Key' and put it in your backpack")
    print("2. throw something from your backpack")
    print("3. try to open the door")
    print("4. give up and will be there for 100 years")
    player=(input("what will you pick: "))

    if player =="1":
        pick=(input("what did you find: "))
        magical_backpack.append(pick)
        print(f"you inserted {pick} into your magical backpack")

    elif player =="2":
        throw=(input("what will you throw?= "))
        if throw in magical_backpack:            
            magical_backpack.remove(throw)
            print(f"you threw {throw} from your magical backpack")
        else:
            print(f"\nlooks like there are no {throw}🤔")

    elif player =="3":
        if "Correct Key" in magical_backpack:
            in_danger=False
            print("you heard a click sound")
            print("yay you unlocked the front door")
            break
        else:
            print("the door is still locked")

    elif player =="4":
        print("you stayed there for 100 years")
        break

    else:
        print("please write it correctly😡")

        
