print('Welcome to online shopping🛒🛍️')
item=str(input("\nplease enter the item you want to buy: "))
much=int(input(f"How much {item} would you want to buy?: "))
member=(input("are you a member?(true/false): "))
if member=='true':
    float(input(f"what is your member ID: "))
elif member=='false':
    member1=bool(input(f"would you like to be a member in online shopping?(true/false): "))
    if member1=='true':
      str(input(f"please enter your phone number: "))
      print(input("here is your membership and this is your ID(press enter)"))
      print("ID:37678")
    else:
      print("Alright let's proceed your purchase!")

#continue to create discount system
   
   