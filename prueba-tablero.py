# Prueba de función de la generación del tablero

from funciones import gen_tablero as generar
from funciones import mostrar_tablero as mostrar

minimo = generar(3)
maximo = generar(10)
inferior = generar(2)
superior = generar(15)

if (type(minimo) == list) and (type(maximo) == list):
    print('Prueba 1 pass')
if (inferior == -1) and (superior == -1):
    print('Prueba 2 pass')