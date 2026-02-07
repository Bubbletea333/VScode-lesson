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
    pick=(input("pick 1 , 2 or 3 :"))

    if pick == 1:
        hunger=hunger+2
        print("Sparkle is eating now")

    elif pick == 2:
        energy=energy+2
        happiness=happiness-1
        print ("Sparkle is sleeping, shh be quiet")

    elif pick == 3:
        energy=energy-2
        hunger=hunger-1
        happiness=happiness+2
        print("Sparkle played catch")
    
    else:
        print(input("please write 1 2 or 3: "))

        #display the status