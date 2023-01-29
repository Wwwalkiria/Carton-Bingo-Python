import random

def crearCarton():
    carton = []
    cuadrado = "🟩"
    # Crear carton vacio
    fila1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    fila2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    fila3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    carton = [fila1, fila2, fila3]
    # Agregar los cuadrados
    for indice, fila in enumerate(carton):
        while fila.count(cuadrado) < 4:
            indiceCuadrado = random.randint(0, 8)
            esPar = indiceCuadrado % 2 == 0
            if indice == 0 and esPar:
                fila[indiceCuadrado] = cuadrado
            elif indice == 1 and not esPar:
                fila[indiceCuadrado] = cuadrado
            elif indice == 2:
                fila[indiceCuadrado] = cuadrado

    # Completar los numeros
    # Rango de numeros
    # 1 10 20 30 40 50 60 70 80
    # 9 19 29 39 49 59 69 79 90
    completarColumna(carton, 0, 1, 9)
    completarColumna(carton, 1, 10, 19)
    completarColumna(carton, 2, 20, 29)
    # ...

    return carton





def completarColumna(cartonACompletar, numeroColumna, rangoMin, rangoMax):
    # numeroColumna = 3
    # rangoMin = 30
    # rangoMax = 39
    # Rango de numeros
    # 1 10 20 30 40 50 60 70 80
    # 9 19 29 39 49 59 69 79 90
    cantidadCeros = 0
    # Tarea reemplazar por un bucle
    fila1 = cartonACompletar[0]
    fila2 = cartonACompletar[1]
    fila3 = cartonACompletar[2]
    if fila1[numeroColumna] == 0:
        cantidadCeros += 1
    if fila2[numeroColumna] == 0:
        cantidadCeros += 1
    if fila3[numeroColumna] == 0:
        cantidadCeros += 1

    print(f"Hay {cantidadCeros} ceros en la primer columna")

    rango = list(range(rangoMin, rangoMax + 1))
    numerosEnRango = random.sample(rango, cantidadCeros)
    numerosEnRango.sort()

    print(f"Los numeros a asignar son: ", numerosEnRango)
    for indiceRangos in cartonACompletar:
        indiceNRangos = 0
        # Tarea reemplazar por un bucle
        fila1 = cartonACompletar[0]
        fila2 = cartonACompletar[1]
        fila3 = cartonACompletar[2]
        if fila1[numeroColumna] == 0:
            fila1[numeroColumna] = numerosEnRango[indiceNRangos]
            indiceNRangos += 1
        if fila2[numeroColumna] == 0:
            fila2[numeroColumna] = numerosEnRango[indiceNRangos]
            indiceNRangos += 1
        if fila3[numeroColumna] == 0:
            fila3[numeroColumna] = numerosEnRango[indiceNRangos]
            indiceNRangos += 1



def mostrarCarton(carton):
    print(f"{'╔'}{'═'*28}{'╗'}")
    for fila in carton:
        filaTexto = "║"
        for columna in fila:
            if columna != "🟩" and columna >= 0 and columna <= 9:
                filaTexto += f" 0{columna}"
            else:
                filaTexto += f" {columna}"
        filaTexto += " ║"
        print(filaTexto)
    print(f"{'╚'}{'═'*28}{'╝'}")


# Programa
carton = crearCarton()
mostrarCarton(carton)