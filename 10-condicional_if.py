# CONDICIONAL IF
# Para definir si un bloque de código le pertenece a otro en Python siempre debe estar identado
"""
Ejemplo:
-Valor booleano
if <bool>:
    print("Este mensaje se muestra porque el valor es booleano")
"""

if True:
    print("El valor es True")

if not False:
    print('El valor no se muestra porque es False')

name = 'Santiago'
# Se ejecuta ya que tiene un valor, y esto lo hace True
if not name:
    print('En la variable hay un valor')
# El bloque else se ejecuta solo si la condición no se cumple, es decir, si es False
else:
    print('El valor de name es falso')