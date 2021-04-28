import random

print("*" * 50)
print("\nTrabajo Practico 1 AED: el juego de dados\n")
print("*" * 50)


# Carga de datos inicial: nombre de jugadores


player1 = input('\nNombre del primer jugador: ')
player2 = input('\nNombre del segundo jugador: ')
score1 = 0
score2 = 0


# Primera ronda: Generacion del primer lanzamiento jugador 1


print("\n\nEs el turno de", player1)
print("\nIntenta sacar 3 valores iguales con los dados para ganar 6 puntos")

input("\n*** Presiona enter para lanzar los dados ***")
dado1 = random.randint(1, 6)
print("\nTirada de dado1:", dado1)
dado2 = random.randint(1, 6)
print("Tirada de dado2:", dado2)
dado3 = random.randint(1, 6)
print("Tirada de dado3:", dado3)


# Primera ronda: Generacion del segundo lanzamiento del jugador 1


if (dado1 != dado2 and dado1 != dado3) and (dado2 != dado3):
    score1 = 0

if dado3 == dado2 and dado3 != dado1:
    score1 = 3
    print("\n¡¡¡Casi lo logras!!!")
    print("Tienes 3 puntos, pero todavia puedes ganar los 6")
    input("\n*** Presiona Enter para relanzar el dado 1 ***")
    dado1 = random.randint(1, 6)
    print("\nNueva tirada de dado1:", dado1)

if dado3 == dado1 and dado3 != dado2:
    score1 = 3
    print("\n¡¡¡Casi lo logras!!!")
    print("Tienes 3 puntos, pero todavia puedes ganar los 6")
    input("\n*** Presiona Enter para relanzar el dado 2 ***")
    dado2 = random.randint(1, 6)
    print("\nNueva tirada de dado2:", dado2)

if dado1 == dado2 and dado1 != dado3:
    score1 = 3
    print("\n¡¡¡Casi lo logras!!!")
    print("Tienes 3 puntos, pero todavia puedes ganar los 6")
    input("\n*** Presiona Enter para relanzar el dado 3 ***")
    dado3 = random.randint(1, 6)
    print("\nNueva tirada de dado3:", dado3)

if dado1 == dado2 and dado1 == dado3:
    score1 = 6

if score1 == 6:
    print("¡¡¡Felicitaciones!!! \nLo haz logrado")
else:
    print("Mala suerte \nNo lo haz logrado")

print("\n\nPuntaje:", score1)
input("\n*** Presiona Enter para finalizar su turno ***")


# Primera ronda: Generacion del primer lanzamiento jugador 2


print("\n\nEs el turno de", player2)
print("\nIntenta sacar 3 valores iguales con los dados para sumar 6 puntos")

input("\n*** Presiona enter para lanzar los dados ***")
dado1 = random.randint(1, 6)
print("\nTirada de dado1:", dado1)
dado2 = random.randint(1, 6)
print("Tirada de dado2:", dado2)
dado3 = random.randint(1, 6)
print("Tirada de dado3:", dado3)


# Primera ronda: Generacion del segundo lanzamiento del jugador 2


if dado1 != dado2 and dado1 != dado3 and dado2 != dado3:
    score2 = 0

if dado3 == dado2 and dado3 != dado1:
    score2 = 3
    print("\n¡¡¡Casi lo logras!!!")
    print("Tienes 3 puntos, pero todavia puedes ganar los 6")
    input("\n*** Presiona enter para reelanzar el dado 1 ***")
    dado1 = random.randint(1, 6)
    print("\nNueva tirada de dado1:", dado1)

if dado3 == dado1 and dado3 != dado2:
    score2 = 3
    print("\n¡¡¡Casi lo logras!!!")
    print("Tienes 3 puntos, pero todavia puedes ganar los 6")
    input("\n*** Presiona enter para reelanzar el dado 2 ***")
    dado2 = random.randint(1, 6)
    print("\nNueva tirada de dado2:", dado2)

if dado1 == dado2 and dado1 != dado3:
    score2 = 3
    print("\n¡¡¡Casi lo logras!!!")
    print("Tienes 3 puntos, pero todavia puedes ganar los 6")
    input("\n*** Presiona enter para reelanzar el dado 3 ***")
    dado3 = random.randint(1, 6)
    print("\nNueva tirada de dado3:", dado3)

if dado1 == dado2 and dado1 == dado3:
    score2 = 6

if score2 == 6:
    print("¡¡¡Felicitaciones!!! \nLo haz logrado")
else:
    print("Mala suerte \nNo lo haz logrado")


print("\n\nPuntaje:", score2)
input("\n*** Presiona Enter para finalizar su turno ***")


# Segunda ronda: Lanzamiento jugador 1


print("\n\nEs el turno de", player1)
print("¿Cuál crees que será la paridad de la suma de los dados de tu próxima tirada?")
print("Si aciertas, a tu puntaje sumaras el valor del mayor dado \nDe lo contrario se le restara el valor del menor")
apuesta = int(input("\nPulsa 1 seguido de Enter para apostar por impar\
\nPulsa 2 seguido de Enter para apostar por par\n"))
assert apuesta == 1 or apuesta == 2

input("\n*** Presiona enter para lanzar los dados ***")
dado1 = random.randint(1, 6)
print("\nTirada de dado1:", dado1)
dado2 = random.randint(1, 6)
print("Tirada de dado2:", dado2)
dado3 = random.randint(1, 6)
print("Tirada de dado3:", dado3)

dadoMayor = max(dado1, dado2, dado3)
dadoMenor = min(dado1, dado2, dado3)

if (dado1 + dado2 + dado3) % 2 == 0:
    if apuesta == 2:
        score1 = score1 + dadoMayor
        print("¡¡¡Felicidades!!! \nHaz acertado en tu predicción")
        if dado1 % 2 == 0 and dado2 % 2 == 0 and dado3 % 2 == 0:
            score1 = score1*2
            print("\nBONUS por paridad apostada en cada dado \n¡Puntaje DOBLE!")
    else:
        score1 = score1 - dadoMenor
        print("Por poco lo logras \nMejor suerte la proxima")
elif apuesta == 1:
    score1 = score1 + dadoMayor
    print("¡¡¡Felicidades!!! \nHaz acertado en tu predicción")
    if dado1 % 2 != 0 and dado2 % 2 != 0 and dado3 % 2 != 0:
        score1 = score1*2
        print("\nBONUS por paridad apostada en cada dado \n¡Puntaje DOBLE!")
else:
    score1 = score1 - dadoMenor
    print("Por poco lo logras \nMejor suerte la proxima")

print("\n\nSu puntaje final:", score1)
input("\n*** Presiona Enter para finalizar su turno ***")


# Segunda ronda: Paridad dados jugador 2


print("\n\nEs el turno de", player2)
print("¿Cuál crees que será la paridad de la suma de los dados de tu próxima tirada?")
print("Si aciertas, a tu puntaje sumaras el valor del mayor dado \nDe lo contrario se le restara el valor del menor")
apuesta = int(input("\nPulsa 1 seguido de Enter para apostar por impar\
\nPulsa 2 seguido de Enter para apostar por par\n"))
assert apuesta == 1 or apuesta == 2

input("\n*** Presiona enter para lanzar los dados ***")
dado1 = random.randint(1, 6)
print("\nTirada de dado1:", dado1)
dado2 = random.randint(1, 6)
print("Tirada de dado2:", dado2)
dado3 = random.randint(1, 6)
print("Tirada de dado3:", dado3)

dadoMayor = max(dado1, dado2, dado3)
dadoMenor = min(dado1, dado2, dado3)

if (dado1 + dado2 + dado3) % 2 == 0:
    if apuesta == 2:
        score2 = score2 + dadoMayor
        print("¡¡¡Felicidades!!! \nHaz acertado en tu predicción")
        if dado1 % 2 == 0 and dado2 % 2 == 0 and dado3 % 2 == 0:
            score2 = score2*2
            print("\nBONUS por paridad apostada en cada dado \n¡Puntaje DOBLE!")
    else:
        score2 = score2 - dadoMenor
        print("Por poco lo logras \nMejor suerte la proxima")
elif apuesta == 1:
    score2 = score2 + dadoMayor
    print("¡¡¡Felicidades!!! \nHaz acertado en tu predicción")
    if dado1 % 2 != 0 and dado2 % 2 != 0 and dado3 % 2 != 0:
        score2 = score2*2
        print("\nBONUS por paridad apostada en cada dado \n¡Puntaje DOBLE!")
else:
    score2 = score2 - dadoMenor
    print("Por poco lo logras \nMejor suerte la proxima")

print("\n\nSu puntaje final:", score2)
input("\n*** Presiona Enter para finalizar su turno ***")


# Resultado: Determinacion de puntajes


print("\n\nPuntaje final de", player1, "es:", score1)
print("Puntaje final de", player2, "es:", score2)


# Resultado: Determinacion de ganador


if score1 == score2:
    print("\nHay empate")
elif score1 > score2:
    print("\nEl ganador es:", player1)
else:
    print("\nEl ganador es:", player2)
print("¡¡¡Felicidades!!!")

print("\n\n****** TERMINO EL JUEGO ******")
