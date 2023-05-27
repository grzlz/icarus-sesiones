lista = [1,2,3,0,4]

for a in lista:
    if a == 0:
        lista.remove(a)
        lista[-1] = a

print(lista)