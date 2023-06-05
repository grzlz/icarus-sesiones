def paso1():
    diccionario1 = {}
    for x in range(1,6):
        diccionario1[x] = x ** 2
    print(diccionario1)

diccionario = {"a":1, "b":2, "c":3, "d":4}

#2
def paso2(diccionario,key):
    print(diccionario[key])

#3
def paso3(diccionario,key,value):
    if key not in diccionario:
        diccionario[key] = value
    return(diccionario)

#4
def paso4(diccionario, key):
    del diccionario[key]
    return(diccionario)

#5
def paso5(diccionario, key):
    if key in diccionario:
        print("La llave sí existe en el diccionario.")
    else:
        print("La llave no existe en el diccionario")

#6
def paso6(diccionario):
    for key, value in diccionario.items():
        print(f"{key}:{value}")

#7
def paso7():
    a = [a**2 for a in range(1,11)]
    print(a)
    return(a)

#8
def paso8(lista1,lista2):
    diccionario = {a:b for a,b in zip(lista1,lista2)}
    return(diccionario)

#9
def paso9(diccionario):
    lista = list(diccionario.values())
    print(lista)
    return(lista)

#10
def paso10(diccionario):
    keys_ordenadas = sorted(diccionario.keys())
    for key in keys_ordenadas:
        value = diccionario[key]
        print(value)

def paso11(diccionario):
    values_ordenados = sorted(diccionario.values())
    for value in values_ordenados:
        key = 
