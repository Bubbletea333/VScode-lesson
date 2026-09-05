print('Welcome to online shopping🛒🛍️')
item=str(input("\nplease enter the item you want to buy: "))
much=int(input(f"How much {item} would you want to buy?: "))
each=float(input(f"How much is for one?(in dollars):$ "))
member=(input("are you a member?(true/false): ")).lower()

subtotal=(much*each)
discount=0

if member=='true':
    float(input(f"what is your member ID: "))
    discount=(subtotal*0.2)
elif member=='false':
    member1=str(input(f"would you like to be a member in online shopping?(true/false): ")).lower()
    if member1=='true':
      str(input(f"please enter your phone number: "))
      print("here is your membership and this is your ID")
      print("ID:37678")
      discount=(subtotal*0.2)
    else:
      print("Alright let's proceed your purchase!")

total=(subtotal-discount)
print("---Receipt---")
print(f"item:{item}")
print(f"you bought {much} {item}")
print(f"subtotal: ({much}*{each})=${subtotal}")
print(f"discount: {discount} ")
print(f"total: ${total}")