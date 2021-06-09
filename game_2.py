import random

player1 = input('\nNombre del primer jugador: ')
player2 = input('\nNombre del segundo jugador: ')

max_score_player1 = max_score_player2 = 0 # accumulate points for each player
rounds = rounds_won_player1 = rounds_won_player2 = rounds_tied = 0 #total rounds/ rounds won for each player/ rounds tied
hit_player1 = hit_player2 = percentage_player1 = percentage_player2 = 0
accumulator_player1 = accumulator_player2 = 0

target = int(input('Puntaje a alcanzar(mayor que 10, por favor): '))

if target < 10:
    print("ERROR Ingrese un valor mayor a 10")
    target = int(input('Puntaje a alcanzar: (mayor que 10, por favor) '))

def throw_dice():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c = random.randint(1, 6)
    print('valor de los dados: (',a, ',', b, ',', c,')')
    return a, b, c

def turn(player):
    print("\n\nEs el turno de", player)
    print("¿Cuál crees que será la paridad de la suma de los dados de tu próxima tirada?")

    bet = int(input("\nPulsa 1 seguido de Enter para apostar por impar\
    \nPulsa 2 seguido de Enter para apostar por par\n"))
    assert bet == 1 or bet == 2
    input("\n*** Presiona enter para lanzar los dados ***")
    return bet

def even_odd(a, b, c, bet):
    hit = 0
    if (a + b + c) % 2 == 0 and bet == 2:
        hit+=1
    elif (a + b + c) % 2 != 0 and bet == 1:
        hit+=1
    return hit

def jugada(a, b, c, bet):
    major_dice = max(a, b, c)
    minor_die  = min(a, b, c)
    score = 0

    if (a + b + c) % 2 == 0:
        if bet == 2:
            score = major_dice
            if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
                score = major_dice*2
        else:
            score -= minor_die
    elif bet == 1:
        score = major_dice
        if a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
            score = major_dice*2
    else:
        score -= minor_die

    return score

while max_score_player1 < target and max_score_player2 < target: #target score
    bet = turn(player1)
    a, b, c = throw_dice()
    hit_player1 += even_odd(a, b, c, bet)
    accumulator_player1 = jugada(a, b, c, bet)
    max_score_player1 = max_score_player1 + accumulator_player1
    print("\n\nPuntaje de este turno:", accumulator_player2)

    bet = turn(player2)
    a, b, c = throw_dice()
    hit_player2 += even_odd(a, b, c, bet)
    accumulator_player2 += jugada(a, b, c, bet)
    max_score_player2 = max_score_player2 + accumulator_player2
    print("\n\nPuntaje de este turno:", accumulator_player2)

    #save total rounds
    rounds+= 1
    #save rounds won
    if accumulator_player1 > accumulator_player2:
        rounds_won_player1 = rounds_won_player1 + 1
    elif accumulator_player2 > accumulator_player1:
        rounds_won_player1 = rounds_won_player1 + 1
    else:
        rounds_tied = rounds_tied + 1 #save rounds tied

##************************************ END ******************************************************

print('\n*** FIN DEL JUEGO ***')

#Show score and name
print("\n\nEl puntaje del jugador", player1, ' es: ', max_score_player1)
print("\nEl puntaje del jugador", player2, ' es: ', max_score_player2, '\n')

print('***** ESTADISTICAS *****')

# El porcentaje de aciertos para cada jugador (considerando acierto si la suma de los dados coincidió con la paridad
percentage_player1 = (hit_player1 * 100 // rounds)
percentage_player2 = (hit_player2 * 100 // rounds)


#show won and
if max_score_player1 > max_score_player2:
    print('El ganador es:', player1)
    if percentage_player1 > percentage_player2:
            print('El ganador tuvo mayor porcentaje de aciertos')
    elif percentage_player1 < percentage_player2:
            print('El perdedor tuvo mayor porcentaje de aciertos')
    else:
            print('Con mismos Porcentajes de aciertos')

elif max_score_player2 > max_score_player1:
    print('El ganador es:', player2)
    if percentage_player2 > percentage_player1:
            print('El ganador tuvo mayor porcentaje de aciertos')
    elif percentage_player2 < percentage_player1:
            print('El perdedor tuvo mayor porcentaje de aciertos')
    else:
            print('Con mismos Porcentajes de aciertos')
else:
    if eachScore1 > eachScore2:
        print('\nEl ganador es: ', player1)
    elif eachScore2 > eachScore1:
        print('\nEl ganador es: ', player2)
    else:
        print('\n ¡Hay un empate!')

#show percentage
print('\nPorcentaje de aciertos del jugador: ', player1, '->', percentage_player1, '%')
print('Porcentaje de aciertos del jugador: ', player2, '->', percentage_player2, '%')

# La cantidad de jugadas realizadas (recordando que una jugada consiste en los turnos de ambos jugadores).
print('\nLa cantidad de jugadas realizadas son: ', rounds)

# Si hubo al menos una jugada con puntaje empatado entre ambos jugadores.
if rounds_tied > 0:
    print('\nHubo al menos una jugada terminada en empate. En total: ', rounds_tied)

# El puntaje promedio obtenido por jugada por cada jugador.





# Si algún jugador ganó en al menos 3 turnos seguidos.
