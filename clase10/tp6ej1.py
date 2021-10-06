#TP6 EJ1

def leer_lineas_archivo(archivo):
    lineas= []
    with open(archivo, 'r', encoding='utf-8') as arch:
        for linea in arch:
            lineas.append(linea[:-1])
    return lineas

def buscar_posicion_caracter(caracter, linea):
    for i in range(len(linea)):
        if linea[i] == caracter:
            return i
    return -1


def quitar_comentarios(lineas_archivo):
    lista= []
    for linea in lineas_archivo:
        i = buscar_posicion_caracter('#', linea)
        if i == -1:
            lista.append(linea)
        else:
            lista.append(linea[0:i])
    return lista

def escribir_archivo(nombre_archivo, lineas_sin_comentarios):
    with open(nombre_archivo, 'w', encoding='utf-8') as arch:
        for linea in lineas_sin_comentarios:
            arch.write(linea + '\n')


def main():
    nombre_archivo= "simulacro_parcial.py"
    lineas_archivo = leer_lineas_archivo(nombre_archivo)
    lineas_sin_comentarios= quitar_comentarios(lineas_archivo)
    escribir_archivo("copia_" + nombre_archivo, lineas_sin_comentarios)

if __name__ == '__main__':
    main()