def cargar_csv(direccion:str)-> list:
    matriz = []
    with open(direccion,"r") as archivo:
        for linea in archivo:
            lista_linea = linea.split(";")
            contrabarra = lista_linea[9]
            lista_linea[9] = contrabarra[0]
            for i in range(len(lista_linea)):
                lista_linea[i] = int(lista_linea[i])
            matriz.append(lista_linea)
    return matriz

def ingresar_numero(texto_si_no_es:str,cantidad_de_largo:int):
    numero = input("ingresa un numero de no mas de 3 cifras")
    validacion_numero = numero.isdigit()
    largo_numero = len(numero)
    while validacion_numero == False or largo_numero > cantidad_de_largo:
        numero = input(texto_si_no_es)
        validacion_numero = numero.isdigit()
        largo_numero = len(numero) 
    return int(numero)

def numeros_consecutivos(matriz,numero)-> list:
    lista_consecutivos = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])-1):
            if matriz[i][j] < numero:
                a = siguiente(i,j,matriz,numero)
                if a != None:
                    lista_consecutivos.append(a)
    return lista_consecutivos

def siguiente(i,j,matriz,numero,acumulador = None,contador=0) -> tuple:
    lista = []
    if j > 9:
        return None

    if acumulador == None:
        acumulador = matriz[i][j] + matriz[i][j+1]
    else:
        acumulador += matriz[i][j+1]

    if matriz[i][j] + 1 == matriz[i][j+1]:
        contador += 1
        if acumulador < numero:
            return siguiente(i,j+1,matriz,numero,acumulador,contador)
        elif acumulador > numero:
            return None
        if acumulador == numero:
            for k in range(contador):
                lista.append(matriz[i][j+k])
            return lista
    else: 
        return None




