"""
Juan Yael Avalos Mayorga // A01276329
Este  es el código del juego "Blackjack".
"""

import random
from random import shuffle

lista_barajas = (                 # Creamos una lista que simule la baraja de cartas
[1] * 4 +  [2] * 4 +
[3] * 4 + [4] * 4 +
[5] * 4 + [6] * 4 +
[7] * 4 + [8] * 4 +
[9] * 4 + [10] * 4 +
[10] * 4 + [10] * 4 +
[10] * 4 
)

shuffle (lista_barajas)           # Con esta función los elementos de la lista se ordenan al azar.

def print_menu () :               # Se crea una función que imprima el menú del juego y retorne la opción que eligió el jugador.
    print (" ")
    print ("Bienvenido al juego de 21 programado en Python :), le recuerdo que este juego es para 2 personas.")
    print (" ")
    print ("1. Empezar el Juego")
    print (" ")
    print ("2. Salir")
    print (" ")
    menu_choice = int (input ("Por favor eliga una opción: "))
    print (" ")
    return menu_choice


def player_menu () :              # Se crea una función que imprima el menu de opciones del jugador y retorne la opción que eligió el jugador
    print ("1. Tomar una carta")
    print (" ")
    print ("2. Dejar de tomar cartas")
    print (" ")
    player_choice = int (input  ("Eliga una de las siguientes opciones: "))
    print (" ")
    return player_choice


def choose_winner (lista_de_listas) :     # Se crea una función que escoja al ganador del juego dependiendo su puntaje y si este se excede de 21
    
    score_player1 = lista_de_listas [0][-1]
    score_player2 = lista_de_listas [1][-1]
    
    if score_player1 > 21 :
        score_player1 = 0
    
    if score_player2 > 21 :
        score_player2 = 0
    
    if score_player1 > score_player2 :
        print (" ")
        print (" ")
        print ("!!!El ganador del juego es el jugador 1!!!")
        print (" ")
        print (" ")

    if score_player2 > score_player1 :
        print (" ")
        print (" ")
        print ("!!!El ganador del juego es el jugador 2 !!!")
        print (" ")
        print (" ")



options = print_menu()     # Aquí empieza el desarrollo del juego

if options == 1:

    turno = 0
    acum_card1 = 0
    acum_card2 = 0
    player1_list = []
    player2_list = []

    while turno <= 20 :     # Creamos el código del juego dentro de un while con la variable turno para que respete los turnos de los jugadores
       
        if turno % 2 == 0 :   # Si el módulo de turno/2 es par, será el turno del jugador 1
        
            print (" ")
            print ("Es turno del Jugador 1 ----->")
            print (" ")
            player_m1 = player_menu ()
            
            if player_m1 == 1 :     # Si el jugador decide tomar una carta, esta la tomará de la lista y la almacenará en un acumulador y en una lista,
                                    # esto sirve para cuando se escoja a un ganador
                acum_card1 += lista_barajas.pop ()
                print (" ")
                print (f"el valor de sus cartas es  {acum_card1}")
                print (" ")
                player1_list.append (acum_card1)
            
            if acum_card1 > 21 :   # Si el puntaje del acumulador es mayor a 21, este deja de acumular puntos y se concluye el juego ya quje se excedió del puntaje máximo.
                print (" ")
                print ("Jugador 1, usted se ha superado el límite de valor en sus cartas. Este juego ha acabado.")
                print (" ")
                break

            if player_m1 == 2 :   # Si el jugador decide ya no tomar más cartas, el puntaje del acumulador se quedará en el último valor.
                print (" ")
                print (f"el valor final de sus cartas es  {acum_card1}")
                print (" ")
                

        if turno % 2 == 1 :     # Si el módulo de turno/2 es impar, será el turno del jugador 2.
        
            print (" ")
            print (" ")
            print ("Es turno del Jugador 2 ----->")
            print (" ")
            player_m2 = player_menu ()
            
            if player_m2 == 1 :    # Si el jugador decide tomar una carta, esta la tomará de la lista y la almacenará en un acumulador y en una lista.
                acum_card2 += lista_barajas.pop ()
                print (" ")
                print (f"el valor de sus cartas es  {acum_card2}")
                print (" ")
                player2_list.append (acum_card2)
            
            if acum_card2 > 21 :    # Si el puntaje del acumulador es mayor a 21, este deja de acumular puntos y se concluye el juego ya que se excedió del puntaje máximo.
                print (" ")
                print ("Jugador 2, usted se ha superado el límite de valor en sus cartas. Este juego ha acabado.")
                print (" ")
                break

            if player_m2 == 2 :     # Si el jugador decide ya no tomar más cartas, el puntaje de acumulador se quedará en el último valor
                print (" ")
                print (f"el valor final de sus cartas es  {acum_card2}")
                print (" ")
        
            if (player_m1 == 2) and (player_m2 == 2) :  # Si los 2 jugadores deciden ya no tomar más cartas, se concluye el juego y se decide un ganador.
                break


        turno +=1
    
    final_list = [player1_list , player2_list]     # Creamos una lista que almacene el desarrolo de juego de los 2 jugadores

    print (" ")
    print (" ")
    print (f"Jugador 1, el proceso de su juego se ve así:  {player1_list}")
    print (" ")
    print (f"Jugador 2, el proceso de su juego se ve así:  {player2_list}")
    print (" ")

    choose_winner (final_list)      # Usamos la función "choose_winner" para elegir el ganador del juego

elif options == 2 :
    print ("Hasta la próximaa :)")
    print (" ")

else :
    print ("Error")
    print (" ")
