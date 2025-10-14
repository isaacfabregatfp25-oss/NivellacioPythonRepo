"""Pedra - Paper - Tisores: Guanyador el primer que arriba a 3 punts. (2p)"""

import random

opcions=["pedra", "paper", "tisores"]
puntsUsuari=0
puntsMaquina=0

def opcions_joc(escollir_user, escollir_maquina):
    global puntsUsuari, puntsMaquina

    if escollir_user == escollir_maquina:
        print("Heu emapatat.")
    elif (escollir_user == "pedra" and escollir_maquina == "tisores") or \
        (escollir_user == "tisores" and escollir_maquina == "paper") or \
        (escollir_user == "paper" and escollir_maquina == "pedra"):
        print("Has guanyat aquesta ronda.")
        puntsUsuari += 1
    else:
        print("La màquina ha guanyat aquesta ronda.")            
        puntsMaquina +=1

while puntsUsuari < 3 and puntsMaquina < 3:
    escollir_user=input("Escull entre (pedra, paper i tisores): ")
    if escollir_user not in opcions:
        print("Error, no has escollit correctament.\n")        
    else:
        escollir_maquina = random.choice(opcions)
        print(f"La màquina ha escollit {escollir_maquina}.")

        opcions_joc(escollir_user, escollir_maquina)
        print(f"Total de punts:\n\tL'usuari te {puntsUsuari}\n\tLa màquina te {puntsMaquina}\n")

if puntsUsuari == 3:
    print("Has guanyat la partida!!!")
else:
    print("La màquina ha guanyat la patida.")