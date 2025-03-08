# STRINGS
# Son una colección de caracteres, por lo tanto, cada caracter tiene un índice


message = 'Primer mensaje' # Se puede establecer con comillas simples
message2 = "Segundo mensaje" # Se puede establecer con comillas dobles

print(message) # Imprimir
print(len(message)) # Contar número caracteres
print(type(message)) # Indicar tipo de dato
print("i" in message) # Validar si existe un caracter en el string
print(message.index("m")) # Validar si existe un caracter en el string y retornar su índice
print(message[-1])

# Generar substrings
message2 = message[2:]
print(message2)