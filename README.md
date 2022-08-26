# Ingenieria-Trabajos-y-Tareas

Avance 1
=============
Juego de Cartas 21
-------------
A01276329/Juan Yael Avalos Mayorga

----------------------

El juego de 21 es un juego de cartas, donde 2 o más participantes. Este juego empieza cuando el qué pasa las cartas da 1 carta a cada 1 (El valor de las cartas como J, Q o K equivalen a 10). Después de esto, si los jugadores lo deciden, pueden llevarse otra carta. Si la suma de las cartas es arriba de 21, el jugador pierde. En este juego gana quien su suma le da 21 o quien se quede más cerca de este.
Algoritmo

Lo que voy hacer en este algoritmo es recrear el juego de cartas 21 entre 2 personas en python, para esto recrearé en el código los sig pasos para que el juego funcione

1. Primero que pida al jugador si quiere empezar a jugar
2. Si dice que no que le diga un mensaje de que cuando quiera jugar reinicie
3. Si quiere jugar, el codigo generará un número aleatorio entre 1 y  10.
4. El programa le enseñará al jugador el número, y le hará la pregunta de si se queda con el, o pide otro numero.
5. Si se queda con el, el programa guardará el número, y empezará a jugar con el otro competidor.
6. Si decide otro número, el programa sacara otro número aleatorio del 1 al 10, lo presentará al jugador y lo va a sumar con el número anterior.
7. Si la suma da más de 21, el programa dirá que es turno del otro jugador debido a que este perdió, guardara el número y empezara a jugar con el otro participante.
8. Si La suma da menos de 21, se repetirán los pasos 6, 7 y 8.
9. Cuando termine de jugar el primer jugador, la computadora guardará su número y empezará el mismo proceso con el segundo jugador.
10. El Juego termina hasta que uno de los 2 logre sacar un 21 o que cuando los jugadores decidan quedarse con el número, en ese momento el programa va a comparar los 2 numeros y dará como ganador el participante que se acerque más a 21.
11. Cuando alguno de los jugadores gane, el programa señalará al ganador y anunciará el fin del juego

Avance 1
=============

Operadores
------------------------
Este programa será complejo, sin embargo las operaciones de este son muy sencillas. Aquí solo se usará 1 operador, el cual es "SUMA" (+). Este operador lo ocuparemos cuando la computadora vaya sumando los numeros de los jugadres y que cheque que no se excedan de 21. Este también lo ocuparé en una función donde a una variable se le vaya sumando 1 cada vez que un jugador participe, esto es con función de que los numeros pares hagan que un participante pueda jugar su turno, mientras que en los numeros impares el otro jugador juege.
