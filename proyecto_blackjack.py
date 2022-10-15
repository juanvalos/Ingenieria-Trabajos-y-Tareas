

"""
    En este Avance agregaré estructuras de decisión en mi programa. 
"""
import random


#Esta es la función de la suma de las cartas
def suma_cartas():

    num1=random.randint(1,10)
    num2=num1 + random.randint(1,10)

    iniciar_juego=input("Bienvenidos a este juego de cartas llamado 21, si desea jugar presione 1: ")
    
    if iniciar_juego =="1" :
        print (f"Su carta tiene un valor de {num1}")
        cont_juego=input("Si desea continuar presione 1: ")

        if cont_juego=="1":
            print(f"La suma de sus numeros es {num2}")
            
#esta es la función del contador para el turno del jugador
def contador(): 

    n=0
    turno=n+1

    if turno %2 == 1:
        print("es turno del jugador 1")

        if turno %2 == 0:
            print("es turno del jugador 2")

suma_cartas()
contador()
