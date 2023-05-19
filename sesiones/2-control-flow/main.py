import random

def obtener_opcion_jugador():
    opcion = input("Elige una opción: Piedra (r), Papel (p) o Tijera (t): ")
    if opcion.lower() == "r":
        return "piedra"
    elif opcion.lower() == "p":
        return "papel"
    elif opcion.lower() == "t":
        return "tijera"
    else:
        print("Opción inválida. Por favor, elige nuevamente.")
        return obtener_opcion_jugador()

def obtener_opcion_computadora():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "Empate"
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        return "¡Ganaste!"
    else:
        return "¡La computadora ganó!"

def jugar_piedra_papel_tijera():
    print("¡Bienvenido a Piedra, Papel o Tijera!")
    jugador = obtener_opcion_jugador()
    computadora = obtener_opcion_computadora()
    print("Tu elección: " + jugador)
    print("Elección de la computadora: " + computadora)
    print(determinar_ganador(jugador, computadora))

jugar_piedra_papel_tijera()