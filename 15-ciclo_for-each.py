# CICLO FOR-EACH
# Nos permite iiterar cada uno de los elementos de una colección, obteniendo su valor

"""
Estructura:
for <variable_de_cada_elemento_recorrido> in <colección>:
    ... Intrucciones a ejecutar en cada ciclo
"""

numbers = [1, 2, 3, 4, 5]
user = {
    'name' : 'santiago',
    'last_name' : 'silva',
    'age' : 25
}

"""

for number in numbers:
    print(f"El número es: {number}")

# En el caso de las tuplas se puede aplicar el desempaquetado
for key, value in user.items():
    print(f"La clave {key} tiene el valor {value}")
"""

# FUNCIÓN RANGE
# Permite generar un rango de número enteros, es decir, una colección

# El método range con un solo argumento genera el número de enteros que se pasen
for number in range(10):
    print(number)

# El método range con dos parámetros genera un rango de números entre dos valores y se excluye el final
for number in range(5, 10 + 1):
    print(number)