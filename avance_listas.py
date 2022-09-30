"""
En este avance implementaré listas a mi proyecto
"""

import random



# Definimos una función para imprimir el valor de que el jugador tiene con sus cartas

def print_cart (num) :

        print (f"Su cartas tienen un valor de {num}")
        print (" ")



# Definimos una función para el contador para el turno del jugador

def contador() : 

    n=0
    turno=n+1

    if turno %2 == 1:
        print("es turno del jugador 1")

        if turno %2 == 0:
            print("es turno del jugador 2")



# Definimos una función que sirva  para imprimir el valor final de las cartas del jugador

def cart_s ( num ) :
        print (f"El numero final de sus cartas es {num}")
        print (" ")



# Definimos una función para imprimir que el jugador se excedió en el valor de sus cartas
def cart_e ( num ):
        print (f"Usted se ha excedido del valor máximo para ganar con {num} en sus cartas")
        print (" ")



# Definimos una función para el juego para el jugador 1, implementando while

def player1_game ():
    
    print ( "Es turno del jugador 1, empecemos con su juego" )
    print ( " " )
    print_cart (num1)

    i = 0
    player_list = [num1]

    while (i < 21) :
        
        cont_game = int (input("Si desea tomar otra carta presione 1, y si desea quedarse con el valor de sus cartas presione 2: "))
        print (" ")

        if cont_game == 1 :
            sum_cart= i + num1
            i= sum_cart + random.randint(1,10)
            print_cart (i)
            player_list.append (i)
            
        if cont_game == 2 :
            cart_s (i)
            print (f"La evolución de su juego se ve así: {player_list}")
            break

        if i > 21 :
            cart_e ( i )
            print (f"La evolución de su juego se ve así: {player_list}")
            break

 
    print ( " " )
    print ( " " )
    print ( " " )            


# Definimos una función para el juego para el jugador 2, implementando while

def player2_game ():
     
    print ( "Es turno del jugador 2, empecemos con su juego" )
    print ( " " )
    print_cart (num2)

    i = 0
    player_list = [num2]

    while (i < 21) :
        
        cont_game = int (input("Si desea tomar otra carta presione 1, y si desea quedarse con el valor de sus cartas presione 2: "))
        print (" ")

        if cont_game == 1 :
            sum_cart= i + num2
            i= sum_cart + random.randint(1,10)
            print_cart (i)
            player_list.append (i)
            
        if cont_game == 2 :
            cart_s (i)
            print (f"La evolución de su juego se ve así: {player_list}")
            break

        if i > 21 :
            cart_e ( i )
            print (f"La evolución de su juego se ve así: {player_list}")
            break

 
    print ( " " )
    print ( " " )
    print ( " " )            

# Aqui iniciamos el Juego

in_game = int (input("Bienvenidos a este juego de cartas llamado 21, si desea jugar presione 1: "))
print (" ")

num1 = random.randint(1,10)
num2 = random.randint(1,10)

if in_game == 1 :
   
   player1_game()
   player2_game()