pokemon_bag=["Charmander","Pikachu","Squirtle","Bulbasaur","Snorlax"]

print("Welcome human!!")
print("You are now holding a bag with pokemon balls")
print(f"inside the pokemon balls there are= {pokemon_bag}")

choose=int(input("\n equip your pokemon by entering 1 number from 0 until 4="))
print(f"you equipped {pokemon_bag[choose]}")

replace=int(input("enter pokemon slot number to be replaced="))
print(f"you replaced {pokemon_bag[replace]}")

replced=(input("enter your new pokemon= "))
pokemon_bag[replace]=replced
print(f"your new pokemon is {pokemon_bag}")