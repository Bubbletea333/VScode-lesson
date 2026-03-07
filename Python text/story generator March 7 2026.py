import random
animals=["a mouse","a cat","a dog","a bird","a lobster"]
names=["John","Blohi","Cherry","Patrick","Paradise"]
places=["supermarket","mall","cafe","school","park"]
when=["yesterday","last week","last year","last decade","an hour ago"]
action=["stole burgers","talked to the phone","read a book","played with friends","bought toys"]
residence=["India","America","Antartica","Russia","South Korea"]
print(random.choice(when)+', there was '+ random.choice(animals)+' named '+ random.choice(names)+' that lived in '+ random.choice(residence)+', it went to the '+ random.choice(places)+' and '+random.choice(action)+'.')