import moduleintro2_Sept_12_2026 as mi2

a = mi2.person1["age"]
print(a)
#we can make the modue name shorter by using "as" then type the name of your new module it can be anything number,letters, and the combination of numbers and letters.

import random
x = dir(random)
print(x)
#dir is a function to display all the tools inside the module.

from moduleintro2_Sept_12_2026 import person1
print (person1["age"])