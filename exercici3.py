"""El 'Penjat' - 'Ahorcado': (2p)
El programa partirà d'una llista de 30 paraules d'entre 3 i 7 lletres obtingudes d'un fitxer extern.
Aleatòriament es seleccionarà una de les 30 paraules.
L'usuari disposarà de número de lletres de la paraula * 2 intents per adivinar-la.
S'anirà mostrant abans de cada intent el tauler típic: R _ _ _ _
"""

import random

def lecturaArchivo(nombreArchivo):
    listaPalabras = []
    with open(nombreArchivo, "r", encoding="utf-8") as fichero:
        for linea in fichero:
            palabra = linea.strip().lower()
            listaPalabras.append(palabra)
        return listaPalabras                

def getPalabra(lista):
    palabra = random.choice(lista)
    return palabra

def transformaPalabra(palabra):
    estado = []
    for letra in palabra:
        estado.append('_')
    return estado

def remplazarLetra(palabraSecreta, estado, letra):
    for n in range(0, len(palabraSecreta)):
        if letra == palabraSecreta[n]:
            estado[n] = letra
    return estado            

def compruebaLetra(letra, palabraSecreta, estado, numIntentos):
    if letra in palabraSecreta:
        print("Has elegido una letra correcta.")
        estado = remplazarLetra(palabraSecreta, estado, letra)
    else:
        print("La letra no está en la palabra.")
        numIntentos -= 1
    return estado, numIntentos

def compruebaEstado(estado):
    if '_' not in estado:
        return True
    
def compruebaIntentos(numIntentos):
    if numIntentos != 0:
        print(f"Te quedan {numIntentos} intentos.")
    else:
        print("Game Over! No te quedan intentos.")        


listaPalabras=lecturaArchivo("archivo.txt")
aciertoFinal=False
numIntentos=6

palabraSecreta = getPalabra(listaPalabras)
estado = transformaPalabra(palabraSecreta)

while aciertoFinal == False and numIntentos > 0:
    print(" ".join(estado))
    letra=input("Introduzca una letra: ")
    estado, numIntentos = compruebaLetra(letra, palabraSecreta, estado, numIntentos)

    if compruebaEstado(estado):
        print(f"Has adivinado la palabra: {palabraSecreta}")
        aciertoFinal = True
    else:
        compruebaIntentos(numIntentos)        