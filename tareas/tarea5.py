class Persona:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def cumple(self):
        self.edad += 1

mi_persona = Persona("Paco", 22)

class Estudiante(Persona):
    def __init__(self,nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    def cumple(self):
        super().cumple()
        return f'Felicidades {self.nombre}, tienes {self.edad} años'

mi_estudiante = Estudiante("Paco", 22, 8)

print(mi_estudiante.cumple())

class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    def ladrar(self):
        return 'Woof, woof'

mi_perro = Perro('Ubbe', 'chingona')

print(mi_perro.ladrar())

class Retriever(Perro):
    def __init__(self, nombre, raza, color):
        super().__init__(nombre, raza)
        self.color = color
    
balto = Retriever("Balto", "Retriever", "Café")

print(balto.color)