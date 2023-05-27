def funcion_nombre(nombre):
    for a in nombre:
        print(a)

mi_nombre = ['A', 'n', 'd', 'r', 'e', 's']

funcion_nombre(mi_nombre)

diccionario1 = {
    1: "azul",
    2: "rojo",
    3: "verde"
}

print(diccionario1[4])

lista = [1,2,3,0,4]

for a in lista:
    if a == 0:
        lista.remove(a)
        lista.insert(x-1, a)