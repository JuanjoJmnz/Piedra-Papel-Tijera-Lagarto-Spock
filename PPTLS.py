import random
import time

print("Las reglas del juego son: \n"
"\tPiedra gana a Tijeras y a Lagarto.\n" \
"\tTijeras gana a Papel y a Lagarto.\n" \
"\tPapel gana a Piedra y a Spock.\n" \
"\tLagarto gana a Spock y a Papel.\n" \
"\tSpock gana a Piedra y a Tijeras.\n")

while True:
    print("Elige una opción \n 1 - Piedra \n 2 - Papel \n 3 - Tijera \n 4 - Lagarto \n 5 - Spock")

    eleccion = int(input("Elige: "))

    while eleccion > 5 or eleccion < 1:
        eleccion = int(input("Elección no válida, elige de nuevo: "))

    if eleccion == 1:
        eleccion_nombre = "Piedra"
    elif eleccion == 2:
        eleccion_nombre = "Papel"
    elif eleccion == 3:
        eleccion_nombre = "Tijera"
    elif eleccion == 4:
        eleccion_nombre = "Lagarto"
    else:
        eleccion_nombre = "Spock"

    print("Has elegido: " + eleccion_nombre)
    print("Turno del ordenador.")

    eleccion_ord = random.randint(1,5)

    if eleccion_ord == 1:
        eleccion_ord_nombre = "Piedra"
    elif eleccion_ord == 2:
        eleccion_ord_nombre = "Papel"
    elif eleccion_ord == 3:
        eleccion_ord_nombre = "Tijera"
    elif eleccion == 4:
        eleccion_ord_nombre = "Lagarto"
    else:
        eleccion_ord_nombre = "Spock"

    print("Pensando...")
    time.sleep(3)
    
    print("El ordenador ha elegido: " + eleccion_ord_nombre)
    print(eleccion_nombre, " VS ", eleccion_ord_nombre)

    print("Calculando ganador...")
    time.sleep(3)
    
    if eleccion_nombre == eleccion_ord_nombre:
        resultado = "Empate"
    elif (eleccion == 3 and eleccion_ord == 1) or (eleccion_ord == 3 and eleccion == 1) or (eleccion == 4 and eleccion_ord == 1) or (eleccion_ord == 4 and eleccion == 1):
        resultado = "Piedra"
    elif (eleccion == 1 and eleccion_ord == 2) or (eleccion_ord == 1 and eleccion == 2) or (eleccion == 5 and eleccion_ord == 2) or (eleccion_ord == 5 and eleccion == 2):
        resultado = "Papel"
    elif (eleccion == 2 and eleccion_ord == 3) or (eleccion_ord == 2 and eleccion == 3) or (eleccion == 4 and eleccion_ord == 3) or (eleccion_ord == 4 and eleccion == 3):
        resultado = "Tijeras"
    elif (eleccion == 5 and eleccion_ord == 4) or (eleccion_ord == 5 and eleccion == 4) or (eleccion == 2 and eleccion_ord == 4) or (eleccion_ord == 2 and eleccion == 4):
        resultado = "Lagarto"
    elif (eleccion == 1 and eleccion_ord == 5) or (eleccion_ord == 1 and eleccion == 5) or (eleccion == 3 and eleccion_ord == 5) or (eleccion_ord == 3 and eleccion == 5):
        resultado = "Spock"

    if resultado == "Empate":
        print("Hay un empate.")
    elif resultado == eleccion_nombre:
        print("¡Has ganado!")
    else:
        print("¡El ordenador ha ganado!")

    print("¿Quieres jugar de nuevo? (S/N)")
    jugar_nuevo = input().lower()
    if jugar_nuevo == "n":
        break

print("¡Gracias por jugar!")