# Por último, se pide elaborar y mostrar las siguientes estadísticas:

# La cantidad de jugadas realizadas (recordando que una jugada consiste en los turnos de ambos jugadores).
# Si hubo al menos una jugada con puntaje empatado entre ambos jugadores.
# El puntaje promedio obtenido por jugada por cada jugador.
# El porcentaje de aciertos para cada jugador (considerando acierto si la suma de los dados coincidió con la paridad
# apostada). Indicar también si el ganador es el que tuvo mayor porcentaje de aciertos.
# Si algún jugador ganó en al menos 3 turnos seguidos.

import random

player1 = input('\nNombre del primer jugador: ')
player2 = input('\nNombre del segundo jugador: ')
maxScore1 = maxScore2 = 0
rounds = roundsWon1 = roundsWon2 = roundsTied = 0
average = hitPlayer1 = hitPlayer2 = percentagePlayer1 = percentagePlayer2 = 0
objetivo = int(input('Puntaje a alcanzar(mayor que 10, por favor): '))

if objetivo < 10:
    print("ERROR Ingrese un valor mayor a 10")
    objetivo = int(input('Puntaje a alcanzar: (mayor que 10, por favor) '))

def tiradaDados():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c = random.randint(1, 6)
    print('valor de los dados: (',a, ',', b, ',', c,')')
    return a, b, c

def turno(player):
    print("\n\nEs el turno de", player)
    print("¿Cuál crees que será la paridad de la suma de los dados de tu próxima tirada?")
    print("Si aciertas, a tu puntaje sumaras el valor del mayor dado \nDe lo contrario se le restara el valor del menor")

    apuesta = int(input("\nPulsa 1 seguido de Enter para apostar por impar\
    \nPulsa 2 seguido de Enter para apostar por par\n"))
    assert apuesta == 1 or apuesta == 2
    input("\n*** Presiona enter para lanzar los dados ***")
    return apuesta

def par_impar(a,b,c, apuesta):
    hit = 0
    if (a + b + c) % 2 == 0 and apuesta == 2:
        hit+=1
    elif (a + b + c) % 2 != 0 and apuesta == 1:
        hit+=1
    return hit

def jugada(a, b, c, apuesta):
    dadoMayor = max(a, b, c)
    dadoMenor = min(a, b, c)
    score = 0

    if (a + b + c) % 2 == 0:
        if apuesta == 2:
            score = dadoMayor
            print("¡¡¡Felicidades!!! \nHaz acertado en tu predicción")
            if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
                score = dadoMayor*2
                print("\nBONUS por paridad apostada en cada dado \n¡Puntaje DOBLE!")
        else:
            score -= dadoMenor
            print("Por poco lo logras \nMejor suerte la proxima")
    elif apuesta == 1:
        score = dadoMayor
        print("¡¡¡Felicidades!!! \nHaz acertado en tu predicción")
        if a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
            score = dadoMayor*2
            print("\nBONUS por paridad apostada en cada dado \n¡Puntaje DOBLE!")
    else:
        score -= dadoMenor
        print("Por poco lo logras \nMejor suerte la proxima")

    return score

# correntScore = jugada(a, b, c, apuesta)
# print("\n\nPuntaje de este turno:", correntScore)


while maxScore1 < objetivo and maxScore2 < objetivo:
    apuesta = turno(player1)
    a, b, c = tiradaDados()
    hitPlayer1 += par_impar(a, b, c, apuesta)
    maxScore1 += jugada(a, b, c, apuesta)
    eachScore1 = jugada(a, b, c, apuesta)
    print("\n\nPuntaje de este turno:", eachScore1)

    apuesta = turno(player2)
    a, b, c = tiradaDados()
    hitPlayer2 += par_impar(a, b, c, apuesta)
    maxScore2 += jugada(a, b, c, apuesta)
    eachScore2 = jugada(a, b, c, apuesta)
    print("\n\nPuntaje de este turno:", eachScore2)

    rounds+= 1

    if eachScore1 > eachScore2:
        roundsWon1 = roundsWon1 + 1
    elif eachScore2 > eachScore1:
        roundsWon1 = roundsWon1 + 1
    else:
        roundsTied = roundsTied + 1


print("\n\nEl puntaje del jugador:", player1, ' es: ', maxScore1)
print("\nEl puntaje del jugador:", player2, ' es: ', maxScore2, '\n')

percentagePlayer1 = (hitPlayer1 * 100 // rounds)
percentagePlayer2 = (hitPlayer2 * 100 // rounds)

if maxScore1 > maxScore2:
    print('El ganador es:', player1)
    if percentagePlayer1 > percentagePlayer2:
            print('El ganador tuvo mayor porcentaje de aciertos')
    elif percentagePlayer1 < percentagePlayer2:
            print('El perdedor tuvo mayor porcentaje de aciertos')
    else:
            print('Mismos Porcentajes')

elif maxScore2 > maxScore1:
    print('El ganador es:', player2)
    if percentagePlayer2 > percentagePlayer1:
            print('El ganador tuvo mayor porcentaje de aciertos')
    elif percentagePlayer2 < percentagePlayer1:
            print('El perdedor tuvo mayor porcentaje de aciertos')
    else:
            print('Mismos Porcentajes')
else:
    if eachScore1 > eachScore2:
        print('\nEl ganador es: ', player1)
    elif eachScore2 > eachScore1:
        print('\nEl ganador es: ', player2)
    else:
        print('\n ¡Hay un empate!')

## Estadísticas

# La cantidad de jugadas realizadas (recordando que una jugada consiste en los turnos de ambos jugadores).
print('\n La cantidad de jugadas realizadas son: ', rounds)

# Si hubo al menos una jugada con puntaje empatado entre ambos jugadores.
if roundsTied > 0:
    print('hubo al menos una jugada terminada en empate. En total: ', roundsTied)

# El puntaje promedio obtenido por jugada por cada jugador.




print('\n Porcentaje de aciertos del jugador: ', player1, '->', percentagePlayer1, '%')
print('\n Porcentaje de aciertos del jugador: ', player2, '->', percentagePlayer2, '%')

# Si algún jugador ganó en al menos 3 turnos seguidos.
