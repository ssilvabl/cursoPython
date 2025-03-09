# EL CONDICIONAL MATCH PERMITE EVALUAR MÚLTIPLES CASOS

score = 2

match score:
    case 5:
        print(">>> Tu calificación es excelente")
    case 4:
        print(">>> Tu calificación es aceptable")
    case 3:
        print(">>> Tu calificación es regular")
    case 2 | 1 | 0:
        print(">>> No has aprobado la asignatura")
    case _:
        print(">>> El valor ingresado no es válido para una nota")