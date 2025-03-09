# PALABRAS RESERVADAS CONTINUE Y BREAK AL TRABAJAR CON CICLOS
# Continue -> Salta a la siguiente iteración
# Break -> Rompe la ejecución del ciclo y lo detiene


"""
for number in range(0, 10 + 1):
    # Salta a la siguiente iteración si el número es par
    if number % 2 == 0:
        continue
    # Rompe la iteración cuando llegue al 7
    if number == 7:
        break
    print("El número es:", number)
"""

# La palabra reservada pass o los tres puntos ... sirven para crear bloques los cuales no ejecuten nada
name = None

if name == None:
    pass

if name == None:
    ...