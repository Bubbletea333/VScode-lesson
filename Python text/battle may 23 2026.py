import random
weapon_storage=["staff","bow and arrow","dagger","fireball","1000 wolfs","lightning bolt","super power","ultimate bomb","1 dragon"]
enemy_hp=200
enemy_choose=random.choice(weapon_storage)
player_hp=200

print("you are fighting the final boss😱")
print(f"enemy hp={enemy_hp}")
print(f"your hp={player_hp}")
while enemy_hp >0 or player_hp >0:
    choose=(input(str("\n choose your weapons junk, intermediate, advanced= "))).lower()
    if choose == "junk":
        player_weapon=weapon_storage[0:3]
        print("\nyou have")
        print(player_weapon)
        choose2=(input("pick one from your weapons= ")).lower()
        if choose2 =="staff":
            print("you used your staff")
            enemy_hp=enemy_hp-20
            print(f"enemy's hp={enemy_hp}")
        elif choose2 =="bow and arrow":
            print("you used your bow and arrow")
            enemy_hp=enemy_hp-30
            print(f"enemy's hp={enemy_hp}")
        elif choose2 =="dagger":
            print("you used your dagger")
            enemy_hp=enemy_hp-40
            print(f"enemy's hp={enemy_hp}")
        else:
            print("it is not listed there")
            print(f"enemy choose={enemy_choose} and it hits you")
            player_hp=player_hp-45
            print(f"player_hp={player_hp}")
    elif choose=="intermediate":
        player_weapon=weapon_storage[3:6]
        print("\nyou have")
        print(player_weapon)
        choose4=(input("pick one from your weapons= ")).lower()
        if choose4 =="fireball":
            print("you used your fireball")
            enemy_hp=enemy_hp-50
            print(f"enemy's hp={enemy_hp}")
        elif choose4 =="1000 wolfs":
            print("you used your 1000 wolfs")
            enemy_hp=enemy_hp-65
            print(f"enemy's hp={enemy_hp}")
        elif choose4 =="lightning bolt":
            print("you used your lightning bolt power")
            enemy_hp=enemy_hp-40
            print(f"enemy's hp={enemy_hp}")
        else:
            print("it is not listed there")
            print(f"enemy choose={enemy_choose} and it hits you")
            player_hp=player_hp-60
            print(f"player_hp={player_hp}")


        
    elif choose=="advanced":
        player_weapon=weapon_storage[6:10]
        print("\nyou have")
        print(player_weapon)
        choose3=(input("pick one from your weapons= ")).lower()
        if choose3 =="super power":
            print("you used your super power")
            enemy_hp=enemy_hp-35
            print(f"enemy's hp={enemy_hp}")
        elif choose3 =="ultimate bomb":
            print("you used your ultimate bomb")
            enemy_hp=enemy_hp-85
            print(f"enemy's hp={enemy_hp}")
        elif choose3 =="1 dragon":
            print("you used your dragon")
            enemy_hp=enemy_hp-95
            print(f"enemy's hp={enemy_hp}")
        else:
            print("it is not listed there")
            print(f"enemy choose={enemy_choose} and it hits you")
            player_hp=player_hp-90
            print(f"player_hp={player_hp}")
    else:
        print("it is not in the selection")
    if enemy_hp <=0:
        print("Congratulations you have beaten the final boss!!!🥳")
        break

    elif player_hp <=0:
        print("you lost try again later😭")
        break