class Carro:
    def __init__(self,cilindros):
        self.cilindros = cilindros
    def arrancar(self):
        print("Rum, rum")

mi_carro = Carro(4)
mi_carro.arrancar()
