""" class Carro:
    def __init__(self,cilindros):
        self.cilindros = cilindros
    def arrancar(self):
        print("Rum, rum")

mi_carro = Carro(4)
mi_carro.arrancar() """

class Personaje:
    def __init__(self,bando, presistencia, pataque):
        self.bando = bando
        self.presistencia = presistencia
        self.pataque = pataque
    def ataque(self):
        print(f'Te ataco con {self.pataque}')
    def defensa(self):
        print(f'Defiendo con {self.presistencia}') 

girasol = Personaje("Planta", 1, 0)
girasol.ataque()