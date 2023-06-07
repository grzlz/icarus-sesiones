class Carro:
    def __init__(self,cilindros):
        self.cilindros = cilindros
    def arrancar(self):
        print("Rum,Rum")

mi_carro = Carro(4)
print(mi_carro.cilindros)

mi_carro.arrancar()


class Personajes:
    def __init__(self, bando, presistencia,pataque):
        self.bando = bando
        self.presistencia = resistencia
        self.pataque = ataque
    def ataque(self):
        print(f"Ataca con {self.pataque}")
    
mi_zombie = Personajes(zombies,10,5)
mi_zombie.ataque