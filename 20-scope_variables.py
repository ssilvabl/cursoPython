"""
# EL SCOPE O ALCANCE
- Existen dos tipos de alcances en la variables, los globales y los locales
- Los globales son aquellas variables que se generan fuera de cualquier bloque de código,
- mientras que las variables locales se crean dentro de algún bloque de código.
- Las globales pueden consultarse desde cualquier parte del programa, pero solo se pueden
- modificar desde fuera de los bloques, no desde alguna función.
- Las locales solo se pueden consultar y modificar en su contexto
"""

# Variable global
name = 'Santiago'

def hello():
    # Variable local
    last_name = 'Silva'