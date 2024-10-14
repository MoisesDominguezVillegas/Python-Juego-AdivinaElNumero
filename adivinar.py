import random

MINIMO = 1

dificultad = input("Elige la dificultad (Facil, Medio o Dificil): ")

if dificultad == "Facil":
    maximo = 10
elif dificultad == "Medio":
    maximo = 100
elif dificultad == "Dificil":
    maximo = 1000
elif dificultad not in "Facil Medio Dificil":
    print("ERROR NO SE ENCONTRO LA DIFICULTAD")
    maximo = 10


numero_azar = random.randint(MINIMO, maximo)
intentos = 0

while True:
    intento_usuario = int(input(f"Introduce un numero [{MINIMO} - {maximo}]: "))
    intentos += 1
    
    if intento_usuario > numero_azar:
        print("El numero es mas bajo")
    elif intento_usuario < numero_azar:
        print("El numero es mas alto")
    else:
        break
print("Has acertado! El numero era " + str(numero_azar))
print(f"Has tardado {intentos} intentos.")