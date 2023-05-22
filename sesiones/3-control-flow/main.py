# Loops
my_list = ["azul", "amarillo", "amazul", "verde", "rojo"]

for i in my_list:
    print(i)

# Entrar al iterador usando len de una lista
for i in range(len(my_list)):
    print(i)

# Funciones - cachos de código
def f():
    print("Hola")

# Funciones con return
def funcion_return():
    return 5

# Funciones no puras - con prints, por ejemplo
def funcion_impura():
    print("5")

# Funciones y variables
mi_numero = funcion_return()
print(mi_numero)

# Funcion impura y variable 
def muggles():
    print("5")
    return 6

a = muggles()


# Funciones y loops, loops y funciones
def funcion_loop():
    print("Welcome to the game. You lost.")

keep_going = True
while keep_going:
    funcion_loop()
    user_input = input("Do you want to keep playing?")
    if user_input == "n":
        break

while True:
    funcion_loop()
    if input("Do you want to keep playing?") == "n":
        break
