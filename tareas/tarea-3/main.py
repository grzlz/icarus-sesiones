def paso1():
    lista1 = [1,2,3,4,5]
    return(lista1)

def paso2():
    print(lista1[2])

def paso3(lista1):
    print(len(lista1))

def paso4(lista):
    lista[2] = "Saludos cordiales."
    return(lista)

def paso5(lista, elemento):
    lista.append(elemento)
    return(lista)

def paso6(lista):
    def split_list(lista):
        half = len(lista)//2
        return lista[half:]
    print(split_list(lista))

def paso7():
    lista7 = [1,2,3,4,[1,2,3,4]]
    resultado7 =  lista7[4][2]
    return(lista7)
    print(resultado7)

def paso8(lista):
    for a in lista:
        print(a)

def paso9():
    lista9 = [a**2 for a in range(1,11)]
    return lista9    

def paso10(lista1,lista2):
    lista10 = [a * b for a,b in zip(lista1,lista2)]
    print(lista10)
    return lista10

lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5]
paso10(lista1,lista2)

def paso11(lista):
    return(sum(lista))
    print(sum(lista))

def paso12(lista):
    acumulador = 1
    for a in lista:
        acumulador *= a 
    return(acumulador)
    print(acumulador)

def paso13(lista):
    print(max(lista))
    print(min(lista))

def paso14(lista):
    lista14 = []
    for a in lista:
        if a not in lista14:
            lista14.append(a)
    return(lista14)

def paso15(lista):
    a = lista
    a.reverse()
    return(a)