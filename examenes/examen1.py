from funciones_examen1 import simple_cuatro

nombre = "Francisco"
edad = 22
type(nombre)
type(edad)

def separacion(string):
    lista = string.split()
    print(lista)

numbers = [*range(1,11,1)]
print(numbers)

semestre = {"Macro" : 9, "Micro" : 8, "Desarrollo" : 7, "Series": 8.5}

def impar(n):
    if n.isnumeric() == True:
        if n % 2 == 0:
            print("Este es un número par.")
        else:
            print("Este es un número impar.")
    else:
        print("Este no es un número entero.")

def cuenta_impares(numeros):
    numero_impares = 0
    impares = []
    for n in numeros:
        if n % 2 == 1:
            impares.append[n]
            numero_impares += 1
    print(f"Hay {numero_impares} impares \ Son {impares}")

def hola():
    nombre = input("¿Cómo te llamas?: ")
    if isinstance(nombre) == True:
        print(f"Hola, {nombre}")
    else:
        print("Esto no es un nombre")

cuadrados = [1**2, 2**2, 3**2, 4**2, 5**2, 6**2, 7**2, 8**2, 9**2, 10**2]

def division_segura(x,y):
    if y != 0:
        return x/y
    else:
        print("ERROR")
        return None
    
print(simple_cuatro())

    


