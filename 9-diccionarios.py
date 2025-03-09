# DICCIONARIOS
# La estructura es con clave : valor. Y tanto la clave como el valor puede ser cualquier tipo de objeto

user = {'name' : 'santiago',
        'last_name' : 'silva',
        'edad' : 25}
print(user) 
"""
# Validar si existe una clave/llave en el diccionario
print('name' in user)
# Obtener el valor de una clave
print(user['edad'])
# Obtener el valor de una clave de forma segura sin generar errores.
# Se puede poner un segundo argumento como valor en caso de no existir la llave
print(user.get('namse', 'No existe'))
# Actualizar o añadir un elemento. Se existe se actualiza, sino, se agrega
user['last_name'] = 'silva'
user['name'] = 'clive'
print(user)
# Obtener solo las llaves/claves de un diccionario
print(tuple(user.keys()))
# Obtener solo los valores de un diccionario
print(user.values())
# Obtener el par llave - valor de un diccionario
print(list(user.items()))
"""
# El método setdefault intenta obtener el valor de clave, y sino existe, la crea
print(user.setdefault('name', 'juan'))
# Actualizar items del diccionario o crearlos sino existen
user.update({
    'name' : 'juan',
    'status' : 'active'
})
print(user)
# Eliminar elemento del diccionario
del user['name']
print(user)
# Eliminar elemento del diccionario pero retornando el valor de la llave
print(user.pop('last_name'))
# Eliminar todos los items del diccionario
user.clear()
print(user)