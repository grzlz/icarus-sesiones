class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def cumple(self):
        self.edad += 1 

mi_persona = Persona("Andrés", 21)

class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre, edad)
        self.grado = grado
    def cumple(self):
        print(f"Felicidades {self.nombre}.")
    def cumple_Persona(self):
        print(f"Antes tenía {self.edad}.")
        super().cumple()
        print(f"Ahora tiene {self.edad}.")

        
mi_estudiante = Estudiante("Andrés", 21, "Licenciatura")
mi_estudiante.cumple_Persona()

class Perro:
    def __init__(self,nombre,raza):
            self.nombre = nombre
            self.raza = raza
    def ladrar(self):
        print("Woof")

mi_perro = Perro("Firulais", "Akita")

class Retriever(Perro):
        def __init__(self,nombre,edad,color):
        super().__init__(nombre, raza)
        self.color = color

mi_perro2 = Retriever("Firulais2","Retriever", "Balto")


