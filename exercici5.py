"""Hundir la flota (3p)"""

import random
import string

def crear_tauler():
    return [["~" for _ in range(tauler)] for _ in range(tauler)]

def mostrar_tauler(tauler, amagar_vaixells=True):
    print("  " + " ".join(string.ascii_uppercase[:tauler]))
    for i, fila in enumerate(tauler):
        fila_mostrar = []
        for c in fila:
            if amagar_vaixells and c == "O":
                fila_mostrar.append("~")
            else:
                fila_mostrar.append(c)
        print(f"{i+1:2} " + " ".join(fila_mostrar))
    print()

def es_posicio_valida(tauler, fila, col, mida, orientacio):
    if orientacio == "H":
        if col + mida > tauler:
            return False
        return all(tauler[fila][col+i] == "~" for i in range(mida))
    else:
        if fila + mida > tauler:
            return False
        return all(tauler[fila+i][col] == "~" for i in range(mida))

def col·locar_vaixell(tauler, mida):
    while True:
        orientacio = random.choice(["H", "V"])
        fila = random.randint(0, tauler-1)
        col = random.randint(0, tauler-1)
        if es_posicio_valida(tauler, fila, col, mida, orientacio):
            if orientacio == "H":
                for i in range(mida):
                    tauler[fila][col+i] = "O"
            else:
                for i in range(mida):
                    tauler[fila+i][col] = "O"
            break

def preparar_tauler():
    tauler = crear_tauler()
    for mida in tamany_vaixell:
        col·locar_vaixell(tauler, mida)
    return tauler

def disparar(tauler_oponent, fila, col):
    if tauler_oponent[fila][col] == "O":
        tauler_oponent[fila][col] = "X"
        if vaixell_enfonsat(tauler_oponent, fila, col):
            print("💥 Vaixell enfonsat!")
        else:
            print("🔥 Tocat!")
        return True
    elif tauler_oponent[fila][col] in ["~", "*"]:
        tauler_oponent[fila][col] = "*"
        print("💧 Aigua.")
        return False
    else:
        print("Ja has disparat aquí.")
        return False

def vaixell_enfonsat(tauler, fila, col):
    for r in range(max(0, fila-1), min(tauler, fila+2)):
        for c in range(max(0, col-1), min(tauler, col+2)):
            if tauler[r][c] == "O":
                return False
    return True

def tots_els_vaixells_enfonsats(tauler):
    return all(cell != "O" for fila in tauler for cell in fila)

def coordenada_a_index(coord):
    try:
        col = string.ascii_uppercase.index(coord[0].upper())
        fila = int(coord[1:]) - 1
        if 0 <= fila < tauler and 0 <= col < tauler:
            return fila, col
    except:
        pass
    return None, None


tauler = 10
tamany_vaixell = [4, 3, 3, 2, 2]

print("Benvinguts a UNDÍ LA FLOTA!")
tauler1 = preparar_tauler()
tauler2 = preparar_tauler()
torn = 1

while True:
    if torn == 1:
        print("\n--- Torn del Jugador 1 ---")
        mostrar_tauler(tauler2, amagar_vaixells=True)
        coord = input("Introdueix coordenada (ex: A5): ").strip().upper()
        fila, col = coordenada_a_index(coord)
        if fila is None:
            print("Coordenada invàlida.")
            continue
        disparar(tauler2, fila, col)
        if tots_els_vaixells_enfonsats(tauler2):
            print("Jugador 1 ha guanyat!")
            break
        torn = 2
    else:
        print("\n--- Torn del Jugador 2 ---")
        mostrar_tauler(tauler1, amagar_vaixells=True)
        coord = input("Introdueix coordenada (ex: B3): ").strip().upper()
        fila, col = coordenada_a_index(coord)
        if fila is None:
            print("Coordenada invàlida.")
            continue
        disparar(tauler1, fila, col)
        if tots_els_vaixells_enfonsats(tauler1):
            print("Jugador 2 ha guanyat!")
            break
        torn = 1