# Las condiciones anidadas se realizan dentro del mismo bloque del if inicial

num1 = 50
num2 = 30

if num1 <= num2:
    print(f"El número {num1} es menor o igual a {num2}")
    if num1 >= 8:
        print(f"El número {num1} es mayor o igual a 8")
    else:
        print(f"El número {num1} no es mayor o igual a 8")
else:
    print(f"El número {num1} es mayor a {num2}")