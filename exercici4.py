"""Tres en ratlla (2p)"""

import time

def crearTaulell(maxF, maxC):
    m = []
    for _ in range(maxF):
        fila = ['·'] * maxC
        m.append(fila)
    return m

def escull(a):
    num=0

    while(True):
        num=int(input(f"Escull la {a} (entre 0 i 2): "))
        if 0 <= num <= 2:
            print("\t")
            return num
        else:
            print("\tNo és un número correcte.")
            time.sleep(2)

def ferTirada(q, fitxa):
    fila=0
    col=0

    while(True):
        fila = escull("fila")
        col = escull("columna")
        if q[fila][col] != '·':
            print("Posició ocupada.")
            time.sleep(2)
            print("\n\n")
            imprimirTaulell(q, fitxa)
        else:
            q[fila][col] = fitxa
            break
    return q

def canviFitxa(fitxa):
    if fitxa == 'O':
        return 'X'
    else:
        return 'O'

def imprimirTaulell(quadre, tirada):
    print("\n\t\t3 en ratlla")
    print(f"Torn del jugador {tirada}:\n")
    for i in quadre:
        print(' '.join(i))
    print("\n")

def comprovaGuanyador(quadre):    
    for i in range(3):
        #per fila
        if quadre[i][0] == quadre[i][1] == quadre[i][2] != '·':
            return True
        #per columna
        if quadre[0][i] == quadre[1][i] == quadre[2][i] != '·':
            return True
    
    #diagonals
    if quadre[0][0] == quadre[1][1] == quadre[2][2] != '·':
        return True
    if quadre[0][2] == quadre[1][1] == quadre[2][0] != '·':
        return True


max = 3
quadre = []
fitxa = 'O'
jugades = 0
guanyador = False

quadre = crearTaulell(max, max)

while jugades < max * max and not guanyador:
    fitxa = canviFitxa(fitxa)
    imprimirTaulell(quadre, fitxa)
    quadre = ferTirada(quadre, fitxa)
    jugades += 1
    guanyador = comprovaGuanyador(quadre)

if not guanyador:
    print("\n\Joc acabat, no ha guanyat ningú. Adeu!!!")
else:
    print(f"\n\nJoc acabat, ha guanyat el jugador: {fitxa}!!")

imprimirTaulell(quadre, fitxa)