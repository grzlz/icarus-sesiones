a = [a+1 for a in range(10) if a % 2 == 0]

def paso9():
    lista9 = [a**2 for a in range(1,11)]
    return lista9    

def paso10(lista1,lista2):
    lista10 = [a * b for a,b in zip(lista1,lista2)]
    print(lista10)
    return lista10

def dic_comprehension(lista1,lista2):
    diccionario = {a:b for a,b in zip(lista1,lista2)}
    return(diccionario)

lista1 = ["a","b","c","d","e"]
lista2 = [1,2,3,4,5]
print(dic_comprehension(lista1,lista2))