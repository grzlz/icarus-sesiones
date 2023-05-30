def paso1():
    lista1 = [1,2,3,4,5]

def paso2():
    print(lista1[3])

def paso3():
    print(len(lista1))

def paso4(lista):
    lista[2] = "Saludos cordiales."

def paso5(lista, elemento):
    lista.append(elemento)

def paso6(lista):
    def split_list(lista):
        half = len(lista)//2
        return lista[half:]
    print(split_list(lista))

def paso7():
    lista7 = [1,2,3,4,[1,2,3,4]]
    resultado7 =  lista7[4][2]
    print(resultado7)

def paso8(lista):
    for a in lista:
        print(a)

def paso9():
    lista9 = []
    for a in range(1,11):
        cuadrado = i ** 2
        lista9.append(cuadrado)
    return lista9

def paso10(lista1,lista2):
    lista10 = []
    for a in range(len(lista1)):
        resultado10 = lista1[a] * lista2[a]
        lista10.append(resultado10)
    return lista10

def paso11(lista):
    print(sum(lista))

def paso12(lista):
    acumulador = 1
    for a in lista:
        acumulador *= a 
    print(acumulador)

def paso13(lista):
    print(max(lista))
    print(min(lista))

def paso14(lista):
    lista14 = list(set(lista))
    return lista14

def paso15(lista):
    a = lista
    a.reverse()
    print(a)

