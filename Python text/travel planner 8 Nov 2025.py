destination=str(input("where do you want to go (beach/mountain): ")).lower()
weather=str(input("what kind of weather do you like(sunny/rainy):  ")).lower()
budget=float(input("what is your budget for the destination (Rp.20000-100000): "))

if budget >= 20000 and budget<= 35000:
    print("try to do something in the main city")
    if destination =="beach":
        if weather =="sunny":
            print("try do to surfing")
        elif weather =="rainy":
            print("try to sit and relax at the nearest cafe")
    if destination =="mountain":
        if weather =="sunny":
            print("try to make s'mores")
        elif weather =="rainy":
            print("try to read a book")
elif budget >35000 and budget >= 50000 and budget<= 100000:
    print("")