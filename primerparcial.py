from dataclasses import dataclass
import random

@dataclass
class Alumno:
    apellido: str
    nombre: str
    edad: int
    carrera: int
    mat_aprobadas: int

@dataclass
class Producto:
    nombre: str
    categoria: int
    stock: int
    precio: float


class ErrorCadenaVacia(Exception):
    pass

class ValorNoEncontrado(Exception):
    pass

# Ejercicio 2 Tema 2
def main_ejercicio2_tema2():
    try:
        # cantidad_vocales= contar_vocales("")
        cantidad_vocales= contar_vocales("dfgtesda")
        print(f"Cantidad de vocales: {cantidad_vocales}")
    except ErrorCadenaVacia:
        print("La cadena esta vacia")

def es_vocal(letra):

    """
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        return True
    else:
        return False
    """
    vocales = "aeiouAEIOUáéíóú"
    # print(letra in vocales)
    return letra in vocales

    """
    for vocal in vocales:
        if letra == vocal:
            return True
    return False
    """
    """
    if letra in vocales:
        return True
    return False
   """

def contar_vocales(texto):

    if len(texto) == 0:
        raise ErrorCadenaVacia

    cantidad= 0
    for i in range(len(texto)):
        if es_vocal(texto[i]):
            cantidad += 1
    # NO print
    return cantidad

def main_ejercio1_tema3():
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    try:
        posicion = buscar_valor_matriz(5,mat)
        print(f"Posicion: {posicion[0]} , {posicion[1]}")
    except ValorNoEncontrado:
        print("No encontrado")


def buscar_valor_matriz(valor_a_buscar, matriz):
    print(valor_a_buscar in matriz)
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if valor_a_buscar == matriz[fila][columna]:
                # matriz[fila][columna] = 8
                return [fila, columna]

    raise ValorNoEncontrado

def buscar_mayor_matriz(matriz):
    mayor = matriz[0][0]
    f= 0
    c= 0

    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] > mayor:
                mayor = matriz[fila][columna]
                f = fila
                c= columna
    return [f, c]

def main_ej3_1_tema3():
    lista_alumnos = generar_alumnos()
    # print(lista_alumnos)

    mayor_cant_mat(lista_alumnos)


def generar_alumnos():
    lista= []
    for i in range(10):
        lista.append(Alumno(
            "Apellido" + str(i),
            "Nombre" + str(i),
            20 + i,
            random.randint(1,3),
            random.randint(0, 30)
        ))

    return lista

def mayor_cant_mat(lista_alumnos):
    carrera= ingrese_numero("Ingrese carrera (1-3)", 1,3)
    alumno_mayor= None
    mayor= -1
    for alumno in lista_alumnos:
        if alumno.carrera == carrera:
            if alumno.mat_aprobadas > mayor:
                mayor = alumno.mat_aprobadas
                alumno_mayor= alumno
    if mayor == -1:
        print("no hay alumnos")
    else:
        print(f"Nombre: {alumno_mayor.nombre}")
        print(f"Apellido: {alumno_mayor.apellido}")
        print(f"Edad: {alumno_mayor.edad}")


def ingrese_numero(msg, min, max):
    while True:
        try:
            nro = int(input(msg))
            if nro < min or nro > max:
                print("Numero fuera de rango")
            else:
                return nro
        except ValueError:
            print("Ingrese un nro")

def main_ej3_3_tema3():
    lista= generar_alumnos()
    imprimir_lista(lista)

def imprimir_lista(lista):
    for alumno in lista:
        if alumno.carrera == 1 and alumno.edad > 30:
            print(f"{alumno.nombre} | {alumno.apellido} | {alumno.edad}")

def main_ej3_2_tema1():
    lista= generar_alumnos()
    try:
        promedio= promedio_edad_soft(lista)
        print(f"Prom: {promedio}")
    except ZeroDivisionError:
        print("No hay al..")


def promedio_edad_soft(lista):
    cont= 0
    acc = 0
    for alumno in lista:
        if alumno.carrera == 3:
            acc += alumno.edad
            cont += 1
    return acc / cont


def main():
    # main_ejercicio2_tema2()
    # main_ejercio1_tema3()
    # main_ej3_1_tema3()
    # main_ej3_3_tema3()
    main_ej3_2_tema1()

if __name__ == '__main__':
    main()
    #print(es_vocal("n"))