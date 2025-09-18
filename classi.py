class Player:
    def __init__(self, name, health=100, shield=5, attack=7):
        self.name = name
        if health <1:
            health = 100
            print("ERRORE! La vita non può essere minore di 1, verrà impostata automaticamente a 100")
        self.hp = health
        self.shield = shield
        self.attack = attack

player1 = Player("Vanessa")
print(player1.name, player1.hp, player1.shield, player1.attack)
player2 = Player("Fabio", -8, 6, 5)
print(player2.name, player2.hp, player2.shield, player2.attack)
player3 = Player("Jason", 50, 5, 5)
print(player3.name, player3.hp, player3.shield, player3.attack)
