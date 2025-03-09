# CON EL CONDICIONAL ELIF SE PUEDEN VALIDAR MÚLTIPLES CONDICIONES
# Y CUANDO UNA DE LAS CONDICIONES SEA VERDADERA, LAS DEMÁS SE OMITEN

color = 'azul'

if color == 'verde':
    print("Puede pasar")
elif color == 'amarillo':
    print("Alto parcial")
elif color == 'rojo':
    print("Debe tenerse")
else:
    print(">>> El color ingresado no es válido")