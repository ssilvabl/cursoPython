# MÉTODOS SPLIT Y JOIN
# El método splin se utiliza para generar una lista a partir de un string
# El método join se utiliza para generar un string a partir de una lista

# Generar lista a partir de un string
"""
message = 'hola cómo estás en el día de hoy'
list_message = message.split(' ') # Se indica el caracter separador de cada elemento
print(list_message)

# Generar un string a partir de una lista
message = ' '.join(list_message) # Dentro del string se establece el tipo de separador a utilizar
print(message)


# CONCATENAR STRINGS
name = 'Santiago'
last_name = 'Silva'

# Método 1 - concatenar
full_name = name + ' ' + last_name
print(full_name)

# Método 2 - join
full_name = ' '.join([name, last_name])
print(full_name)

# Método 3 - %s
full_name = '%s %s' %(name, last_name)
print(full_name)

# Método 4 - format
# Opicón 1 - Podemos crear un string base
base = 'Mi nombre completo es {} {} y tengo {} años de edad'
# El método format por defecto asigna los valores en orden de posición y de cualquier tipo
print(base.format(name, last_name, 25))

# Opción 2 - Podemos establecer un nombre para las variables del juego de llaves
base = 'Mi nombre completo es {name} {last_name} y tengo {age} años de edad'
# Se pueden asignar en cualquier posición ya que cuentan con un nombre
print(base.format(name = name, last_name = last_name, age = 25))
"""

# Método 5 - f-string
# Permiten la interpolación, es decir, se permite cambiar los valores en tiempo de ejecución
name = 'santiago'
last_name = 'silva'
# Se pueden añadir las variables, valores y operaciones de forma directa en el juego de llaves
message = f'   mi nombre completo es {name} {last_name} y tengo {20 + 5} años de edad'

# La funión print se puede modificar para cambiar su separador
print(name, last_name, sep='***')

# Convertir todos los caracteres de un string en mayúsculas
print(message.upper())
# Convertir todo en minúscula
print(message.lower())
# Buscar caracter o caracteres en string
print('edad' in message)
# Validar cómo comienza un string
print(message.startswith('mi'))
# Validar cómo termina un string
print(message.endswith('edad'))
# Buscar la primer coincidencia y retornar el índice
print(message.find('s'))
# Convertir el primer caracter en mayúscula
print(message.capitalize())
# Validar si un string está tratando de representar un entero
print('100'.isnumeric())
# Borrar los espacios iniciales y finales
print(message.strip())