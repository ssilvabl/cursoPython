# MÉTODOS SPLIT Y JOIN
# El método splin se utiliza para generar una lista a partir de un string
# El método join se utiliza para generar un string a partir de una lista

# Generar lista a partir de un string
message = 'hola cómo estás en el día de hoy'
list_message = message.split(' ') # Se indica el caracter separador de cada elemento
print(list_message)

# Generar un string a partir de una lista
message = ' '.join(list_message) # Dentro del string se establece el tipo de separador a utilizar
print(message)