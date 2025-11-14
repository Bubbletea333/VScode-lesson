destination=str(input("where do you want to go (beach/mountain): ")).lower()
weather=str(input("what kind of weather do you like(sunny/rainy):  ")).lower()
budget=float(input("what is your budget for the destination (Rp.20000-80000): "))

if budget >= 20000 and budget<= 35000:
    if destination =="beach":
        if weather =="sunny":
            print("try to do surfing")
        elif weather =="rainy":
            print("try to sit and relax at the nearest cafe")
        else:
            print("try to check your spelling for weather")
    elif destination =="mountain":
        if weather =="sunny":
            print("try to make s'mores")
        elif weather =="rainy":
            print("try to read a book")
        else:
            print("try to check your spelling for weather")
    else:
        print("please write the destination correctly")
elif budget > 35000 and budget<= 50000:
    if destination =="beach":
        if weather =="sunny":
            print("try to make a castle")
        elif weather =="rainy":
            print("go to a restaurant that sells crab")
        else:
            print("try to check your spelling for weather")
    elif destination =="mountain":
        if weather =="sunny":
            print("try to hike")
        elif weather =="rainy":
            print("try to eat s'mores")
        else:
            print("try to check your spelling for weather")
    else:
        print("please write the destination correctly")
elif budget > 50000 and budget<= 65000:
    if destination =="beach":
        if weather =="sunny":
            print("try to make a picnic")
        elif weather =="rainy":
            print("try to sit and relax")
        else:
            print("try to check your spelling for weather")
    elif destination =="mountain":
        if weather =="sunny":
            print("try to make a picnic")
        elif weather =="rainy":
            print("try to stay in the hotel and chill")
        else:
            print("try to check your spelling for weather")
    else:
        print("please write the destination correctly")
elif budget > 65000 and budget<= 80000:
    if destination =="beach":
        if weather =="sunny":
            print("try to take a picture")
        elif weather =="rainy":
            print("try to play in the rain")
        else:
            print("try to check your spelling for weather")
    elif destination =="mountain":
        if weather =="sunny":
            print("try to explore")
        elif weather =="rainy":
            print("try to eat sandwiches")
        else:
            print("try to check your spelling for weather")
    else:
        print("please write the destination correctly")
else:
    print("try to check your budget")