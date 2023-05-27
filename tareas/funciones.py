import random

def ahorcado():
    color = ["azul", "amarillo", "blanco", "cafe", "morado", "naranja", "negro", "verde", "rojo"]
    r_color = random.choice(color)
    letras_adivinadas = ["_" for _ in r_color]
    vidas = 5
    letras_intentadas = []
    print("¡Bienvenido al juego de ahorcado!")
    print("Adivina el color.")
    while vidas > 0:
        print(f"Tienes {vidas} vidas")
        print("Palabra: " + " ".join(letras_adivinadas))
        print("Letras intentadas: " + ", ".join(letras_intentadas))
        letra = input("Ingresa una letra: ").lower()
        if len(letra) != 1 or not letra.isalpha():
            print("Ingresa una única letra válida.")
            continue
        if letra in letras_intentadas:
            print("Ya has intentado esa letra.")
            continue
        letras_intentadas.append(letra)
        if letra in r_color:
            for i in range(len(r_color)):
                if r_color[i] == letra:
                    letras_adivinadas[i] = letra
        else:
            vidas -= 1
        if "_" not in letras_adivinadas:
            print("¡Felicidades! Has adivinado el color:", r_color)
            break
    if vidas == 0:
        print("¡Perdiste! El color era:", r_color)

def volado():
    opciones = {1:'águila', 2:'sol'}
    eleccion = input('¿Qué crees que salga? "1" para águila, "2" para sol')
    resultado = random.randint(1,2)
    if eleccion.isnumeric() == True:
        eleccion = int(eleccion)
        if eleccion < 2:
            print(f'Ha salido {opciones[resultado]}')
            print(f'Tú escogiste {opciones[eleccion]}')
            if resultado == eleccion:
                print("Adivinaste")
            else:
                print("No adivinaste")
        else:
            print("Este no es un número válido")
    else:
        print("Esto no es un número")
