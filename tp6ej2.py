import random
from dataclasses import dataclass

@dataclass
class DatosLluvia:
    dia: int
    mes: int
    lluvia: int

def generar_datos():
    lista= []
    cant = random.randint(50,200)
    for i in range(cant):
        d= DatosLluvia(0,0,0)
        d.dia= random.randint(1, 28)
        d.mes= random.randint(1,12)
        d.lluvia= random.randint(0,1000)
        lista.append(d)

    return lista

def crear_archivo(lista):
    with open("lluvias.csv", "w", encoding="utf-8") as arch_lluvias:
        for i in range(len(lista)):
            linea= f"{lista[i].dia};{lista[i].mes};{lista[i].lluvia}\n"
            arch_lluvias.write(linea)

def leer_archivo():
    lista= []
    with open("lluvias.csv", "r", encoding="utf-8") as arch_lluvias:
        for registro in arch_lluvias:
            # "5;12;670\n"
            lluvia= registro[:-1].split(";")
            #["5";"12";"670"]
            dato= DatosLluvia(int(lluvia[0]), int(lluvia[1]), int(lluvia[2]))
            lista.append(dato)
    return lista

def generar_total(lista):
    total= 0
    for elemento in lista:
        total += elemento.lluvia
    return total

def generar_matriz_vacia():
    m= []
    for f in range(31):
        fila= []
        for c in range(12):
            fila.append(0)
        m.append(fila)
    return m

def generar_reporte(lista):
    m= generar_matriz_vacia()
    for e in lista:
        m[e.dia - 1][e.mes - 1] = e.lluvia
    return m


def main():
    lista_lluvia= generar_datos()
    crear_archivo(lista_lluvia)
    lista_lluvia2= leer_archivo()
    total= generar_total(lista_lluvia2)
    print("Total:", total)
    reporte= generar_reporte(lista_lluvia2)
    #imprimir reporte


if __name__ == '__main__':
    main()