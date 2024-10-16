from funciones import *
from os import system

bandera_main = True
bandera_opcion_1 = False
bandera_opcion_2 = False

while bandera_main:
    opcion = input("Bienvenido\n1. Cargar CSV\n2. Ingresar Numero\n3. Numeros Consecutivos\n4. Consecutivos cantidad minima\n5.Consecutivos cantidad Maxima\n6. Salir\n=")
    match opcion:
        case "1":
            matriz = cargar_csv("final_Facundo_Maidana\data_final_20241015.csv")
            bandera_opcion_1 = True
        case "2":
            if bandera_opcion_1:
                numero = ingresar_numero("RE-ingresa un numero de no mas de 3 cifras",3)
                bandera_opcion_2 = True
            else:
                print("FALTA OPCION 1")
        case "3":
            if bandera_opcion_1:
                if bandera_opcion_2:
                    lista = numeros_consecutivos(matriz,numero)
                    print(lista)
                else:
                    print("Falta opcion 2")
            else:
                print("FALTA OPCION 1")
        case "4":
            if bandera_opcion_1:
                if bandera_opcion_2:
                    pass
                else:
                    print("Falta opcion 2")
            else:
                print("FALTA OPCION 1")
        case "5":
            if bandera_opcion_1:
                if bandera_opcion_2:
                    pass
                else:
                    print("Falta opcion 2")
            else:
                print("FALTA OPCION 1")
        case "6":
            bandera_main = False
    system("pause")
    system("cls")