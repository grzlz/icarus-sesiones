from funciones import ahorcado
from funciones import volado


def play_chipiado():
    print("Hola, dime qué juego quieres jugar")
    tipo_juego = input("Escribe 'a' para ahorcado, 'b' para un volado y 'c' para adivinar un número: ")
    if tipo_juego.lower() == 'a':
        ahorcado()
    elif tipo_juego.lower()=='b':
        volado()

play_chipiado()