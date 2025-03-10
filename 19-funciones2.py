"""
# FUNCIONES UTILIZANDO POSICIÓN Y NOMBRES
1. Para las funciones con el uso de parámetros por posición, se utiliza el prefijo *
2. Para las funciones con el uso de parámetros por nombres, se utiliza el prefijo **
Posición -> *args (tupla)
Nombres -> **kwargs {diccionario}
"""

def users(*args, **kwargs):
    info = args
    details = kwargs
    # Retornar tupla y diccionario de valores
    return info, details

# Desempaquetar valores retornados
full_info, full_details = users(
    12, 30, 'santiago', False,
    nombre = 'santiago silva',
    email = 's@s.com',
    active = True
)
print(full_info, full_details)

# Las funcuiones más complejas pueden tener la siguiente estructura
# Primero los parámetros obligatorios, después opcionales de n cantidad por posición, los que tienen valores por defecto
# Y por último los opcionales de n cantidad por nombres
def info(name, last_name, *args, age=25, active=True, **kwargs):
    pass