def stars(X):
    for i in range(X):
        print("*")
        
stars(5)

#--------------------

def EnoughPizza(people, slices):
    if people*3<slices:
        print("That's enough pizza.")
        return "That's enough pizza"
    else:
        print("NOT ENOUGH PIZZA!")
        return "NOT ENOUGH PIZZA!"
    
EnoughPizza(1, 20)

#--------------------

import random #needed for randrange
def CoinFlip():
    num = random.randrange(0, 100)
    if num <50:
        return "heads!"
    else:
        return "tails!"
    
print(CoinFlip())
