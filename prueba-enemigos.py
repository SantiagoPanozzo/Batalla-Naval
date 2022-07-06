from funciones import gen_tablero as generar
from funciones import gen_enemigos as enemigos
from funciones import probar

x = generar(5)
enemigos_ok = [
    'A1',
    'A2',
    'E3',
    'D4',
    'C2',
]
disparos_ok = [
    'A1',
    'A2',
    'E3',
    'D4',
    'C2',
]
enemigos_mal = [
    'A1',
    'A2',
    'G3',
    'D4',
    'C9',
]
disparos_mal = [ 
    'A1',
    'A2',
    'G3',
    'D4',
    'C9',
]

prueba1 = probar(5,enemigos_ok,disparos_ok)[0]
if ('GANASTE' in prueba1) and ('errores' not in prueba1):
    print('----------- Prueba 1 pass')

prueba2 = probar(6,enemigos_ok,disparos_mal)[0]
print(prueba2)
if ('PERDISTE' and 'errores') in prueba2:
    print('----------- Prueba 2 pass')

prueba3 = probar(6,enemigos_mal,disparos_ok)[0]
if ('PERDISTE' and 'errores') in prueba3:
    print('----------- Prueba 3 pass')

prueba4 = probar(6,enemigos_mal,disparos_mal)[0]
if 'errores' in prueba4:
    print('----------- Prueba 4 pass')

print()
x = generar(11)
enemigos_ok1 = [
    'C1',
    'C3',
    'A2',
    'B4',
    'D2',
]
disparos_ok1 = [
    'C1',
    'C3',
    'A2',
    'B4',
    'D2',
]
enemigos_mal1 = [
    'A1',
    'A2',
    'G3',
    'D4',
    'C9',
]
disparos_mal1 = [ 
    'A1',
    'A2',
    'G3',
    'D4',
    'C9',
]

prueba5 = probar(11,enemigos_ok1,disparos_ok1)[0]
if "errores" in prueba5:
      print('----------- Prueba 5 pass')

prueba6 = probar(2,enemigos_ok1,disparos_ok1)[0]
if "errores" in prueba6:
      print('----------- Prueba 6 pass')