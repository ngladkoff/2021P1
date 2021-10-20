import random
from dataclasses import dataclass

@dataclass
class jugada:
    ruleta: str
    numero: int

def generar_archivo():
    ruletas = 'ABCD'
    with open('casino.csv', 'w',encoding='utf-8') as arch:
        for i in range(1000):
            for i in ruletas:
                numero = random.randint(0, 36)
                arch.write(i + ',' + str(numero) + '\n')

def leer_archivo():
    lista = []
    with open('casino.csv', 'r', encoding='utf-8') as arch:
        for linea in arch:
            campos = linea[:-1].split(',')
            jug = jugada(campos[0], int(campos[1]))
            lista.append(jug)

    return lista 

def inicializar_matriz():
    matriz =[]
    for i in range(37):
        lista = []
        for j in range(4):
            lista.append(0)
        matriz.append(lista)
    return matriz

def decodificar(letra):
    if letra == 'A':
        return 0
    if letra == 'B':
        return 1
    if letra == 'C':
        return 2
    if letra == 'D':
        return 3    

def calcular_totales(jugadas):
    matriz = inicializar_matriz()
    for jug in jugadas:
        matriz[jug.numero][decodificar(jug.ruleta)] += 1
    return matriz

def calcular_frecuencias(totales):
    for r in range(4):
        acum = 0
        for i in range(len(totales)):    
            acum += totales[i][r]
        if acum != 0 :
            for i in range (len(totales)):
                totales[i][r] = totales[i][r]/acum
    return totales

def mostrar_frecuencias(listado):
    with open("frec.txt", "w", encoding="utf-8") as a:
        print('|{0:^12}|{1:^12}|{2:^12}|{3:^12}|{4:^12}|'.format('Numero','Frecuencia A','Frecuencia B','Frecuencia C','Frecuencia D'))
        a.write('|{0:^12}|{1:^12}|{2:^12}|{3:^12}|{4:^12}|\n'.format('Numero','Frecuencia A','Frecuencia B','Frecuencia C','Frecuencia D'))
        for listaInd in range(len(listado)):
            #print('|{0:^12}|{1:^.10f}|{2:^.10f}|{3:^.10f}|{4:^.10f}|'.format(listaInd,listado[listaInd][0],listado[listaInd][1],listado[listaInd][2],listado[listaInd][3]))
            print(f'|{listaInd:^12}|{listado[listaInd][0]:^12.5f}|{listado[listaInd][1]:^.10f}|{listado[listaInd][2]:^.10f}|{listado[listaInd][3]:^.10f}|')
            a.write(f'|{listaInd:^12}|{listado[listaInd][0]:^12.5f}|{listado[listaInd][1]:^.10f}|{listado[listaInd][2]:^.10f}|{listado[listaInd][3]:^.10f}|\n')

def buscar_incidencias(frecuencias):
    incidencias = []
    ruletas='ABCD'
    for columna in range(4):
        for fila in range(len(frecuencias)):
            desvio = frecuencias[fila][columna] - 1/37
            if abs(desvio) > 0.005:
                incidencias.append([ruletas[columna], fila, frecuencias[fila][columna], desvio])
    return incidencias

def mostrar_incidencias(incidencias):
    print('|{0:^12}|{1:^12}|{2:^12}|{3:^12}'.format('Ruleta','Numero','Frecuencia','Desvio'))
    for fila in incidencias:
        print(f'|{fila[0]:^12}|{fila[1]:^12d}|{fila[2]:^.10f}|{fila[3]:^.10f}|')

def guardar_incidencias_archivo(incidencias):
    with open('incidencias.csv', 'w', encoding= 'utf-8') as arch:
        for fila in incidencias:
            arch.write(f'{fila[0]},{fila[1]},{fila[2]},{fila[3]}\n')
    



def main():
    # generar_archivo()
    jugadas = []
    jugadas = leer_archivo()
    totales = calcular_totales(jugadas)
    frecuencias = calcular_frecuencias(totales)
    mostrar_frecuencias(frecuencias)
    incidencias = buscar_incidencias(frecuencias)
    mostrar_incidencias(incidencias)
    guardar_incidencias_archivo(incidencias)
    print(len(incidencias))


if __name__ == '__main__':
    main ()