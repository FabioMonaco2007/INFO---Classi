import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def calcola_distanza_origine(self):
        distanza = math.sqrt(self.x**2 + self.y**2) # "**" --> elevamento a potenza
        return distanza
    
    def calcola_distanza_punto(self, altro_punto: "Punto"):
        differenza = math.sqrt(abs(self.y - altro_punto.y)**2 + (abs(self.x - altro_punto.x)**2)) # "abs" --> valore assoluto
        return differenza
    
    def visualizza(self):
        print(f"({self.x}, {self.y})")
        
class Rettangolo:
    def __init__(self, punto1: Punto, punto2: Punto):
        self.punto1 = punto1
        self.punto2 = punto2
        
    def get_base(self):
        base = abs(self.punto1.x - self.punto2.x)
        return base 
    
    def get_altezza(self):
        altezza = abs(self.punto1.y - self.punto2.y)
        return altezza
    
    def get_area(self):
        area = self.get_base() * self.get_altezza()
        return area

punto1 = Punto(3, 4)
punto2 = Punto(6, 8)

punto1.visualizza()
punto2.visualizza()

calcola_distanza = punto1.calcola_distanza_punto(punto2) # funzione che calcola la distanza tra i due punti
print(f"La distanza tra i due punti è: {calcola_distanza}")

r1 = Rettangolo(punto1, punto2)
print(r1.get_base())
print(r1.get_altezza())
