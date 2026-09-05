budget=("your budget is Rp.500.000.00")
choose=str(input("which one will you buy a game console (Rp. 350.000.00), " 
"A school bag (Rp.50.000.00), food (Rp.50.000.00)," 
" Drink (Rp.50.000.00)")).lower()

if choose == "game console":
    print("you will buy the game console")
    print("you will have Rp.150.000.00 left")
elif choose == "school bag":
    print("you will buy the school bag")
    print("you will have Rp.450.000.00 left")
elif choose == "drink":
    print("you will buy the drink")
    print("you will have Rp.450.000.00 left")
elif choose == "food":
    print("you will buy the food")
    print("you will have Rp.450.000.00 left")
else:
    print("please check your spelling")