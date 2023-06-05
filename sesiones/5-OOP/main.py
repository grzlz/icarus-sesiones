class Carro:
    def __init__(self,cilindros):
        self.cilindros = cilindros
    def arrancar(self):
        print("Rum,Rum")

mi_carro = Carro(4)
print(mi_carro.cilindros)

mi_carro.arrancar()

