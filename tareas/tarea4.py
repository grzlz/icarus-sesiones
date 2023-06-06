numeros = {i:i**2 for i in range(1,6)}
print(numeros)

def key_existente(dictionary):
    key = input('¿Qué key deseas buscar?: ')
    if key in dictionary:
        print("Sí está esta key")
    else:
        print("No está esta key")

def cuenta_letras(lista):
    dictionario = {i:len(i) for i in lista}

def list_to_dict(lista1, lista2):
    return {i: j for i, j in zip(lista1, lista2)}

print(list_to_dict([1, 5], [2, 6]))
