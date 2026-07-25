print("welcome")

pokedex={
    "pikachu" : {
        "Total":430,
        "HP":45,
        "Attack":80,
        "Defense":50,
        "Sp.Atk":75,
        "Sp.def":60,
        "Speed":120
    },
    "muk" : {
        "Total":500,
        "HP":105,
        "Attack":105,
        "Defense":75,
        "Sp.Atk":65,
        "Sp.def":100,
        "Speed":50
    },
    "golem" : {
        "Total":495,
        "HP":80,
        "Attack":120,
        "Defense":130,
        "Sp.Atk":55,
        "Sp.def":65,
        "Speed":45
    },
    "zapdos" : {
        "Total":580,
        "HP":90,
        "Attack":90,
        "Defense":85,
        "Sp.Atk":125,
        "Sp.def":90,
        "Speed":100
    },
    "gengar" : {
        "Total":500,
        "HP":60,
        "Attack":65,
        "Defense":60,
        "Sp.Atk":130,
        "Sp.def":75,
        "Speed":110
    },
    "relicanth" : {
        "Total":485,
        "HP":100,
        "Attack":90,
        "Defense":130,
        "Sp.Atk":45,
        "Sp.def":65,
        "Speed":55
    },
    "dunsparce" : {
        "Total":415,
        "HP":100,
        "Attack":70,
        "Defense":70,
        "Sp.Atk":65,
        "Sp.def":65,
        "Speed":45
    },
    "ludicolo" : {
        "Total":480,
        "HP":80,
        "Attack":70,
        "Defense":70,
        "Sp.Atk":90,
        "Sp.def":100,
        "Speed":70
    }
}
while True:
    enter=(input("type a pokemon: ")).lower()

    if enter =="pikachu":
        print("----data of pikachu----")
        print(pokedex["pikachu"])

    elif enter =="gengar":
        print("----data of gengar----")
        print(pokedex["gengar"])

    elif enter =="golem":
        print("----data of golem----")
        print(pokedex["golem"])

    elif enter =="muk":
        print("----data of muk----")
        print(pokedex["muk"])

    elif enter =="dunsparce":
        print("----data of dunsparce----")
        print(pokedex["dunsparce"])

    elif enter =="relicanth":
        print("----data of relicanth----")
        print(pokedex["relicanth"])

    elif enter =="zapdos":
        print("----data of zapdos----")
        print(pokedex["zapdos"])

    elif enter =="ludicolo":
        print("----data of ludicolo----")
        print(pokedex["ludicolo"])

    else:
        print("pokemon is not detected❌")
#https://pokemondb.net/pokedex/allS