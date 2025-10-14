"""Adivina número: L'usuari tindrà tres intents per adivinar un número aleatori del 1 al 10. 
Per cada error es mostrarà per pantalla si el número és major o menor a l'indicat. (2p)"""

import random

numReal=random.randint(1,10)
intents=3

while intents > 0:
    numPosat=int(input("Introdueix un número del 1 al 10: "))
    if numPosat < 1 or numPosat > 10:
        print("Error, NO has introduït un número del 1 al 10.\n")
    else:
        if numPosat == numReal:
            print(f"Correcte!!! El número introduït {numPosat} és el mateix que l'original {numReal}.")
            break
        else:
            intents -= 1
            if intents > 0:
                print(f"Et queden {intents} intents.")
                if numPosat < numReal:
                    print(f"El número original és major al número introduït {numPosat}.\n")
                else:
                    print(f"El número original és menor al número introduït {numPosat}.\n")
            else:
                print(f"No tens més intents, el número original era {numReal}.")