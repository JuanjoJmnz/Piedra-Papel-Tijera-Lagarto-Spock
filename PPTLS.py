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
    elif eleccion_ord == 4:
        eleccion_ord_nombre = "Lagarto"
    else:
        eleccion_ord_nombre = "Spock"

    print("Pensando...")
    time.sleep(3)
    
    print("El ordenador ha elegido: " + eleccion_ord_nombre)
    print(eleccion_nombre, " VS ", eleccion_ord_nombre)

    print("Calculando ganador...")
    time.sleep(3)

    gana_a = {
        1: [3, 4],
        2: [1, 5],
        3: [2, 4],
        4: [5, 2],
        5: [1, 3]
    }
    
    if eleccion_nombre == eleccion_ord_nombre:
        resultado = "Empate"
    elif eleccion_ord in gana_a[eleccion]:
        resultado = eleccion_nombre
    else:
        resultado = eleccion_ord_nombre

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