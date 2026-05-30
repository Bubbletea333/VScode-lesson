import random
weapon_storage=["staff","bow and arrow","dagger","fireball","1000 wolfs","lightning bolt","super power","ultimate bomb","1 dragon"]
enemy_hp=200
enemy_choose=""
player_hp=200

print("you are fighting the final boss")
print(f"final boss hp{enemy_hp}")
print(f"your hp{player_hp}")
choose=(input(str("\n choose your weapons junk, intermediate, advanced= "))).lower()
if choose == "junk":
    player_weapon=weapon_storage[0:3]
    print("\nyou have")
    print(player_weapon)
elif choose=="intermediate":
    player_weapon=weapon_storage[3:7]
    print("\nyou have")
    print(player_weapon)
elif choose=="advanced":
    player_weapon=weapon_storage[7:10]
    print("\nyou have")
    print(player_weapon)
else:
    print("it is not in the selection")
   # while enemy_hp >0 or player_hp >0:

