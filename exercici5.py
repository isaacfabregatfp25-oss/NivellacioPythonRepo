"""Hundir la flota (3p)"""

import time

def crearTaulell(maxF, maxC):
    m = []
    for _ in range(maxF):
        fila = ['·'] * maxC
        m.append(fila)
    return m

def escull(text, maxVal):
    while(True):
        num = int(input(f"{text} (0-{maxVal-1}): "))
        if 0 <= num < maxVal:
            return num
        else:
            print("Valor fora del rang.")

def posarVaixells(tauler, n):
    print("Col·loca els teus vaixells:")
    contador = 0
    while contador < n:
        fila = escull("Fila", len(tauler))
        col = escull("Columna", len(tauler[0]))
        if tauler[fila][col] == '·':
            tauler[fila][col] = 'B'
            contador += 1
            imprimirTaulell(tauler, True)
        else:
            print("Posició ocupada per un vaixell.")           
    print("Tots els vaixells col·locats.\n")
    time.sleep(2)

def ferTirada(tauler, fila, col):
    if tauler[fila][col] == 'B':
        tauler[fila][col] = 'X'
        print("Tocat")
        return True
    elif tauler[fila][col] in ['X', 'O']:
        print("Ja has disparat aqui")
    else:
        tauler[fila][col] = 'O'
        print("Aigua...")
    return False    

def imprimirTaulell(tauler, mostrar=False):
    print("\n   " + " ".join(str(i) for i in range(len(tauler[0]))))
    for i, fila in enumerate(tauler):
        if mostrar:
            print(f"{i}  " + " ".join(fila))
        else:            
            print(f"{i}  " + " ".join(['·' if c == 'B' else c for c in fila]))
    print("\n")

def comprovaGuanyador(tauler):
    for fila in tauler:
        if 'B' in fila:
            return False        
    return True
        

max = 5
num_vaixells = 4

print("\n\t\tHundir la flota")

tauler1 = crearTaulell(max, max)
tauler2 =crearTaulell(max, max)

print("Jugador 1, prepara't per col·locar els teus vaixells.")
posarVaixells(tauler1, num_vaixells)
print("\n" * 50)

print("Jugador 2, prepara't per col·locar els teus vaixells.")
posarVaixells(tauler2, num_vaixells)
print("\n" * 50)

torn = 1
fi = False

while not fi:
    print(f"\n===== Torn del jugador {torn} =====")
    if torn == 1:
        imprimirTaulell(tauler2, False)
        fila = escull("Fila per disparar", max)
        col = escull("Columna per disparar", max)
        ferTirada(tauler2, fila, col)
        if comprovaGuanyador(tauler2):
            fi = True
            print("Joc acabat, jugador 1 ha guanyat!")
    else:
        imprimirTaulell(tauler1, False)
        fila = escull("Fila per disparar", max)
        col = escull("Columna per disparar", max)
        ferTirada(tauler1, fila, col)
        if comprovaGuanyador(tauler1):
            fi = True
            print("Joc acabat, jugador 2 ha guanyat!")

    torn = 2 if torn == 1 else 1
    time.sleep(2)