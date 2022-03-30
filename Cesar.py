import random
import time


def cesar():
    cifrado = False
    descifrado = False
    fuerza = False

    ############ INTERFAZ##################
    print("1. ¿Querés encriptar?")
    print("2. ¿Querés desencriptar?")
    print("3. ¿Querés desencriptar utilizando fuerza bruta?")
    opcion = input("Elija la opcion deseada: ")

    if opcion == "1":
        cifrado = True

    if opcion == "2":
        descifrado = True

    if opcion == "3":
        fuerza = True

    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    if cifrado:  ################################################# CIFRADO

        textoingresado = input("Ingrese la palabra para cifrar: ")
        clavealeatoria = random.randint(1, 27)
        mensajecifrado = ""

        for letra in textoingresado.upper():
            if letra in alfabeto:
                posicion = alfabeto.index(letra)
                posicion = (posicion + clavealeatoria) % len(alfabeto)
                mensajecifrado += alfabeto[posicion]

            else:
                mensajecifrado += letra

        if 0 < clavealeatoria <= 27:
            print("Texto inicial ingresado: " + format(textoingresado))
            print("Resultado: " + format(mensajecifrado))
            print("Clave generada: " + format(clavealeatoria))
            cesar()

    if descifrado:  ################################################# DESCIFRADO

        textoingresado = input("Ingrese la palabra para descifrar: ")
        clave = input("Ingrese la clave: ")
        mensajecifrado = ""

        for letra in textoingresado.upper():
            if letra in alfabeto:
                posicion = alfabeto.index(letra)
                posicion = (posicion - int(clave)) % len(alfabeto)
                mensajecifrado += alfabeto[posicion]

            else:
                mensajecifrado += letra

        if 0 < int(clave) <= 27:
            print("Texto inicial ingresado: " + format(textoingresado))
            print("Resultado: " + format(mensajecifrado))
            print("Clave ingresada: " + format(clave))
            cesar()

    if fuerza:  ################################################# FUERZA BRUTA

        textoingresado = input("Ingrese la palabra para descifar: ")
        contador = 1
        posicion = 0
        mensajecifrado = ""

        while contador <= 27:

            for letra in textoingresado.upper():
                if letra in alfabeto:
                    posicion = alfabeto.index(letra)
                    posicion = (posicion + contador) % len(alfabeto)
                    mensajecifrado += alfabeto[posicion]

                else:
                    mensajecifrado += letra

            print("Texto inicial ingresado: {} \n".format(textoingresado))
            print("Resultado de la fuerza bruta: {}".format(mensajecifrado))
            time.sleep(0.4)
            print(int(27 - contador))
            mensajecifrado = ""
            contador = contador + 1

        input('Apriete cualquier tecla para volver al menú')
        cesar()


cesar()
