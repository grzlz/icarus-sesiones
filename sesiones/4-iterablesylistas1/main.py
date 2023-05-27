lista = [1,2,3,0,4]

for a in lista:
    a + 1

print(lista)

def sumar_1(lista):
    lista2 = []    
    for a in lista:
        lista2.append(a+1)
    return(lista2)

sumar_1(lista)
print(sumar_1(lista))   