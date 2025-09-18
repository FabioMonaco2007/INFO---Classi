#Esercizio 1:
print("Classi | Esercizio 1")

import random
   
class Rettangolo:
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza
        self.area = self.base * self.altezza

base1 = random.randint(1, 20)
altezza1 = random.randint(1, 20)
R1 = Rettangolo(base1, altezza1)
print(R1.base, R1.altezza, R1.area)

base2 = random.randint(1, 20)
altezza2 = random.randint(1, 20)
R2 = Rettangolo(base2, altezza2)
print(R2.base, R2.altezza, R2.area)