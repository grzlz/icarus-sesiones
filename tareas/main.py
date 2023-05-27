import random

def ahorcado():
    color = ["azul", "amarillo", "blanco", "cafe", "morado", "naranja", "negro", "verde", "rojo"]
    r_color = random.choice(color)
    letras_adivinadas = ["_" for _ in r_color]
    vidas = 5
    letras_intentadas = []

    print("¡Bienvenido al juego de ahorcado!")
    print("Tienes 5 vidas. Adivina el color.")

    while vidas > 0:
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
            print("¡Felicidades! Has adivinado la palabra:", r_color)
            break

    if vidas == 0:
        print("¡Perdiste! La palabra era:", r_color)

ahorcado()
