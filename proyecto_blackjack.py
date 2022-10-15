"""
Juan Yael Avalos Mayorga // A01276329
Este  es el código del juego 21, agregando listas anidadas
"""

import random

def print_menu () :
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


def player_menu () :
    print ("1. Tomar una carta")
    print (" ")
    print ("2. Dejar de tomar cartas")
    print (" ")
    player_choice = int (input  ("Eliga una de las siguientes opciones: "))
    print (" ")
    return player_choice


def choose_winner (lista_de_listas) :
    
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



options = print_menu()

if options == 1:

    turno = 0
    acum_cart1 = 0
    acum_cart2 = 0
    player1_list = []
    player2_list = []

    while turno <= 20 :
       
        if turno % 2 == 0 :
        
            print (" ")
            print ("Es turno del Jugador 1 ----->")
            print (" ")
            player_m = player_menu ()
            
            if player_m == 1 :
                acum_cart1 += random.randint (1 , 10)
                print (" ")
                print (f"el valor de sus cartas es  {acum_cart1}")
                print (" ")
                player1_list.append (acum_cart1)
            
            if acum_cart1 > 21 :
                print (" ")
                print ("Jugador 1, usted se ha superado el límite de valor en sus cartas. Este juego ha acabado.")
                print (" ")
                break

            if player_m == 2 :
                print (" ")
                print (f"el valor final de sus cartas es  {acum_cart1}")
                print (" ")
                break



        if turno % 2 == 1 :
        
            print (" ")
            print (" ")
            print ("Es turno del Jugador 2 ----->")
            print (" ")
            player_m = player_menu ()
            
            if player_m == 1 :
                acum_cart2 += random.randint (1 , 10)
                print (" ")
                print (f"el valor de sus cartas es  {acum_cart2}")
                print (" ")
                player2_list.append (acum_cart2)
            
            if acum_cart2 > 21 :
                print (" ")
                print ("Jugador 2, usted se ha superado el límite de valor en sus cartas. Este juego ha acabado.")
                print (" ")
                break

            if player_m == 2 :
                print (" ")
                print (f"el valor final de sus cartas es  {acum_cart2}")
                print (" ")
                break


        turno +=1
    
    final_list = [player1_list , player2_list]

    print (" ")
    print (" ")
    print (f"Jugador 1, el proceso de su juego se ve así:  {player1_list}")
    print (" ")
    print (f"Jugador 2, el proceso de su juego se ve así:  {player2_list}")
    print (" ")

    choose_winner (final_list)

elif options == 2 :
    print ("Hasta la próximaa :)")
    print (" ")

else :
    print ("Error")
    print (" ")
