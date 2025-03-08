# TUPLAS

# Definición: Las tuplas son lista inmutables, están optimizadas y se pueden declarar con o sin paréntesis
# Uso: nueva_tupla = ("hola", 12, 12.0)
"""""
nueva_tupla = ("hola", 1, 1, 12.0, 22, 33, 90)
print(nueva_tupla)


# Acceder a índice
print(nueva_tupla[2])

# Convertir tupla en lista
nueva_lista = list(nueva_tupla)
print(type(nueva_lista))

# Convertir lista en tupla
nueva_tupla1 = tuple(nueva_lista)
print(type(nueva_tupla1))

# Validar si existe elemento en la tupla
print("hola" in nueva_tupla1)

# Contar mismo elemento en una tupla
print(nueva_tupla1.count(1))

# Contar elementos dentro de una tupla
print(len(nueva_tupla1))

#Tupla unitaria
tupla_unitaria = ("hola")

# Desempaquetado de tupla
saludo, num1, num2, num3 = nueva_tupla1
print(saludo, num2, num3, num1)
# Desempaquetado de tupla sin conocer el número de elmentos
# Se le indica a la última variable un * para indicar que todos los demás elementos deben ir ahí en una lista
uno, *dos = nueva_tupla
print(uno, dos)
# Para omitir todos los demás elementos se debe poner un *_, y para omitir sólo uno
# se debe poner el _ en la posición del elemento
uno, *_ = nueva_tupla
print(uno)

# Para omitir elementos en un rango determinado se debe indicar con *_, var1, var2(número de variables a asignar)
uno, *_, dos, tres = nueva_tupla
print(uno, dos, tres)

# Crear una subtupla a partir de un rango de índices
sub_tupla = nueva_tupla[0:2]
#print(sub_tupla)

# Comprimir elementos para generar una nueva tupla
# Se utiliza la función zip()

# Datos a comprimir
# Los datos se organizan en la nueva tupla en forma de pares
# Cuando los datos no tienen la misma longitud, los elementos restantes se omiten
lista1 = "nombre", "apellido", "barrio", "estrato"
tupla1 = 1, 2, 3, 4

# Comprimir datos
resultado = zip(tupla1, lista1)
# Generar tupla
tupla2 = tuple(resultado)

print(tupla2)"""

# FUNCIONES DE TUPLAS

numbers = (2 ,4, 1, 8, 9, 33, 20, 0, 1, 1)
print(len(numbers)) # Contar el número de elementos que tiene la tupla

print(sorted(numbers)) # Recibe como arg una lista o una tupla. Y retorna una lista ordenada/ascendente(default)
print(sorted(numbers, reverse=True)) # Retorna una lista descendente
print(numbers.count(3)) # Retorna el número de veces que está el caracter que se ingresó como arg
print(2 in numbers) # Comprobar si un caracter existe o no en una tupla
print(numbers.index(2)) # Comprobar en qué índice se encuentra un valor