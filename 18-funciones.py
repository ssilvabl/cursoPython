# FUNCIONES
# Deben seguir la nomenclatura Snake Case
"""
Estructura:
def <nombre_funcion>(<parámetros>):
    instrucciones
    return retornar_valores

# Función sin parámetros
def hello():
    print("Hola, Santiago")
# Llamar función
hello()


# Función con parámetros
def hello(name):
    message = f"Hola, {name}"
    return message

# Cuando le pasamos un valor de entrada a la función se conoce como argumento
# Llamar a la función
print(hello("santiago"))

# Función con dos parámetros
def multiply(num1, num2):
    result = f"El resultado de la multiplicación entre {num1} y {num2} es: {num1 * num2}"
    return result

# Función con 2 argumentos
print(multiply(12, 20))


# Las funciones no pueden retornar múltiples valores
# Se retorna una tupla cuando se envían múltiples valores separados por comas
def test():
    return True, 'hola', 40

# Cuando se reciba una tupla se debe realizar el desempaquetado
status, _, age = test()
print(status, age)


# Las funciones por defecto asignan los argumentos a los parámetros en orden de posiçión
# Sin embargo, se pueden indicar los argumentos directamente con el nombre de los parámtros
# Los parámetros por defecto se deben establecer de derecha a izquierda
def hello(name, age=25):
    return f'hola, {name}, tienes {age} años de edad'

#print(hello(age=25, name='santiago'))

# Cuando las funciones tienen parámetros por default se pueden omitir los argumentos
print(hello('santiago'))

# Las funciones pueden recibir n cantidad de argumentos por posición utilizando el prefijo * en el parámetro
# Y se retorna una tupla con todos los argumentos
def suma(*numbers):
    return sum(numbers)

print(suma(12, 30, 4, 5, 10))

# Se pueden pasar otros parámetros por posición y asignar también otro con el prefijo *
def promedio(name, *notes):
    message = f'Hola, {name}. Tu promedio de notas es: {sum(notes) / len(notes)}'
    return message

print(promedio('santiago', 5, 4, 2, 1, 4, 5))
"""

# Se pueden establecer parámetros con n cantidad de argumentos utilizando los nombres
# Y en este caso no se retorna una tupla sino un diccionario que se agrega al parámetro con doble **
def users(**user):
    return user

# Los argumentos en las funciones con doble ** se pasan como clave - valor
print(users(
    name = 'santiago',
    last_name = 'silva',
    age = 25,
    email = 's@s.com'
))