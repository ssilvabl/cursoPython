# CICLO WHILE
# Se ejecutan las instrucciones solo si la condición se cumple
# Es apropiado para casos en los que no se conoce el rango o número de elementos

counter = 11

while counter <= 10:
    print(f"El contador es: {counter}")
    #counter = counter + 1
    counter += 1
# También se puede implementar el bloque else cuando la condición del ciclo deje de cumplirse
else:
    print("El ciclo a finalizado")

# Para generar un número aleatorio podemos utilizar la función randint del módulo random
from random import randint

number = None
# Generar número aleatorio en un rango de a hasta b
random_number = randint(0, 10)

while number != random_number:
    number = int(
        input('Ingresa un número entre el 0 y el 10:')
    )
    if number < random_number:
        print("El número aleatorio es mayor")
    else:
        print("El número aleatorio es menor")
else:
    print("¡Enhorabuena! Has encontrado el número aleatorio, el cual es", random_number)