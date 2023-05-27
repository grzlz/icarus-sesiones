from funciones import ahorcado
from funciones import volado
from funciones import adivinanza


def play_chipiado():
    print("Hola, dime qué juego quieres jugar")
    tipo_juego = input("Escribe 'a' para ahorcado, 'b' para un volado y 'c' para adivinar un número o 'x' para salir: ")
    if tipo_juego.lower() == 'a':
        ahorcado()
        play_chipiado()
    elif tipo_juego.lower() == 'b':
        volado()
        play_chipiado()
    elif tipo_juego.lower() == 'c':
        adivinanza()
        play_chipiado()
    elif tipo_juego.lower() == 'x':
        print("Juego terminado")
        return
    else:
        print("Esta no es una letra válida")
        play_chipiado()

play_chipiado()