"""El Siete y Medio es un juego de cartas donde el objetivo es acercarse lo máximo posible a 7.5 puntos sin pasarse.
    Se juega con una baraja española (sin ochos ni nueves).
    Las cartas del 1 al 7 valen su valor numérico.
    Las figuras (Sota, Caballo y Rey), representadas como J, Q y K, valen 0.5 puntos.
    Al comenzar la partida, se reparte una carta a cada jugador y a la banca, y se muestran todas esas cartas.
    El jugador, conociendo su carta y la carta visible de la banca, decide:
        Robar otra carta para intentar acercarse a 7.5.
        Plantarse y quedarse con su puntuación actual.
    Si el jugador supera 7.5 puntos, pierde automáticamente.
    Después juega la banca, que roba cartas hasta alcanzar al menos 5.5 puntos o decide plantarse.
Obligatorio uso de funciones y listas/diccionarios"""

import random

def crear_baraja():
    """Crea una baraja sin ochos ni nueves"""
    cartas = [1,2,3,4,5,6,7,'J','Q','K']
    return cartas * 4  # 4 palos

def valor_carta(carta):
    """Devuelve el valor de la carta"""
    return carta if type(carta) == int else 0.5

def jugar():
    # Preparar juego
    baraja = crear_baraja()
    random.shuffle(baraja)
    
    # Repartir
    jugador = [baraja.pop()]
    banca = [baraja.pop()]
    
    print(f"\nTu carta: {jugador[0]} - Puntos: {valor_carta(jugador[0])}")
    print(f"Carta banca: {banca[0]}")
        
    while True:
        total_jugador = sum(valor_carta(c) for c in jugador)
        print(f"\nTus puntos: {total_jugador}")
        
        if total_jugador > 7.5:
            print("¡Te pasaste! Pierdes.")
            return
        
        opcion = input("¿Robar? (s/n): ").lower()
        if opcion == 's':
            jugador.append(baraja.pop())
            print(f"Robaste: {jugador[-1]}")
        else:
            break
        
    print("\n--- Turno banca ---")
    while True:
        total_banca = sum(valor_carta(c) for c in banca)
        print(f"Banca tiene: {total_banca} puntos")
        
        if total_banca > 7.5:
            print("¡Banca se pasó! Ganas.")
            return
        elif total_banca >= 5.5:
            print("Banca se planta")
            break
        else:
            banca.append(baraja.pop())
            print(f"Banca roba: {banca[-1]}")
        
    total_jugador = sum(valor_carta(c) for c in jugador)
    total_banca = sum(valor_carta(c) for c in banca)
    
    print(f"\n--- Resultado ---")
    print(f"Tus puntos: {total_jugador}")
    print(f"Banca puntos: {total_banca}")
    
    if total_jugador > total_banca:
        print("¡Ganaste!")
    elif total_banca > total_jugador:
        print("Perdiste")
    else:
        print("Empate")

while True:
    jugar()
    if input("\n¿Jugar otra? (s/n): ").lower() != 's':
        break