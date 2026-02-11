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

    print("\nWhat would Sparkle do?")
    print("1.Eat 2.Sleep 3.Play")
    pick=str(input("pick 1 , 2 or 3 :"))#Python consideres the variable value as a string IF we dont type any Data types

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

    elif energy <= 0 or hunger <= 0 or happiness <= 0:
        keep_alive==False
        print("oh no poor Sparkle")
        break

    else:
        print(str(input("please write 1 2 or 3: ")))

if keep_alive == False:
    print("oh nooooooooo...... (っ °Д °;)っSparkle (┬┬﹏┬┬)")
        #do check how to break the loop