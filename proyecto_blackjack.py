""""
Este programa será complejo, sin embargo las operaciones de este son muy sencillas.
Aquí solo se usará 2 operadores, el cual es "SUMA" (+) y "MODULO" (%).
El operador de suma lo ocuparemos cuando la computadora vaya sumando los numeros de los jugadres
y que cheque que no se excedan de 21.
El operador de modulo lo ocuparé para saber los turnos de cada jugador. Para esto ocuparé una variable extra. en este ejemplo es (n)
A esta variable se le irá sumando 1 cada vez que la función de jugar empiece y termine, despues de esto hallaremos el residuo sobre 2 de n+1
Cuando el residuo sea 1, será turno del jugador 1
Cuando el residuo sea 2, será el turno del jugador 2
"""
#SUMA
turno_1=10
turno_2=5
valor_final= turno_1+turno_2
print(f"los puntos finales del juagador 1 son  {valor_final}, podemos continuar con el otro turno")

#MODULO
n=0
turno=n+1
if turno %2 == 1:
    print("es turno del jugador 1")

if turno %2 == 0:
    print("es turno del jugador 2")
