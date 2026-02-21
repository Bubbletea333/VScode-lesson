pet_name = "Sparkle"
hunger=5
energy=5
happiness=5
keep_alive=True

print("Welcome to the digital Pet Hub")
print("keep sparkle healthy")

while keep_alive == True:
    print("\nSparkle's status:")
    print(f"hunger:{hunger}/10")
    print(f"energy:{energy}/10")
    print(f"happiness:{happiness}/10")

    

    if energy <= 0 or hunger <= 0 or happiness <= 0:#Checking for game over
        keep_alive=False
        print("oh no poor Sparkle（；´д｀）ゞ")
        print("GAME OVER(┬┬﹏┬┬)")
        break


    else:
        print("\nWhat would Sparkle do?")
        print("1.Eat 2.Sleep 3.Play")
        try:
            pick=input("pick 1 , 2 or 3 :").strip()#Python consideres the variable value as a string IF we dont type any Data types
        except (EOFError, KeyboardInterrupt):
            print("No input detected — continuing the game.")
            continue
        
        if pick == "1":
            hunger=hunger+2
            print("Sparkle is eating now")

        elif pick == "2":
            energy=energy+2
            happiness=happiness-1
            print ("Sparkle is sleeping, shh be quiet")

        elif pick == "3":
            energy=energy-2
            hunger=hunger-1
            happiness=happiness+2
            print("Sparkle played catch")

            if energy > 10:
                energy= 10
            
            if hunger > 10:
                hunger= 10

            if happiness > 10:
                happiness= 10

        else:
            print("INVALID"+ "please write 1 or 2 or 3")

        #do check how to break the loop