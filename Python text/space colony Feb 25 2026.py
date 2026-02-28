coins = 50
air = 10
food = 10
days = 0
mission_active = True

print("Welcome to Space Colony Simulator!👾")
print("Your mission is to survive 50 days and thrive in space!")

while mission_active:
    days = days+1
    print(f"--day {days}--")
    print(f"Coins={coins}🪙")
    print(f"Air={air}")
    print(f"food={food}🍔🍟🍱🥢")
    
    if air <= 0 or food <= 0:#Checking for game over        
        print("oh no your colony is in danger!😵😨")
        mission_active=False

    elif days == 50:        
        print("yay your colony survived")
        mission_active=False

    else:
        print("what would you do with your coins?")
        print("1. buy air(-5 coins) 2. buy food(-5 coins) 3.Do nothing(+5 coins)")
        pick=(input("pick 1,2 or 3: "))

        if pick == "1":
            air=air+2
            food=food-2
            print("you colony got air")

        elif pick == "2":
            food=food-2
            air=air-2
            print ("your colony ate food")

        elif pick == "3":
            coins=coins+5
            food=food-2
            air=air-2
            print("you get 5 coins")

        else:
            print("please pick 1 , 2 or 3")

print("GAME OVER")