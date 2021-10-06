# Clase 10 - Archivos
from dataclasses import dataclass
from os import replace

@dataclass
class Cliente:
    nombre: str
    codigo: str

@dataclass
class Alumno:
    apellido: str
    dni: str
    nombre: str
    provincia: str
    idProvincia: str
    localidad: str
    sede: str
    direccion: str
    llamado: str


"""
open('./datos/nombre_archivo', 'modo', encoding='utf-8')
modo:
r -> solo lectura, si no existe da error
w -> escritura, si existe lo sobreescribe, si no existe lo crea
a -> agregar, agrega al final del archivo, si no existe lo crea
x -> crear, si existe da error
"""

def main_escribir():
    with open('./clase10/archivo2.txt', 'w', encoding='utf-8') as arch1:
        for i in range(100):
            arch1.write(f'{i} - Cliente {i}\n')
        #arch1.write("UADE - Programación 1\n")
        #arch1.write("Archivos de texto\n")

    print("Archivo generado")

    """
    0001Cliente1
    0002Cliente2
    """
def main_leer():
    lista_clientes= []

    with open('./clase10/archivo1.txt', 'r', encoding='utf-8') as arch1:
        #texto= arch1.read()
        #print(texto)
        for linea in arch1:
            cli= Cliente(linea[4:-1],linea[0:4])
            lista_clientes.append(cli)

    print(lista_clientes)

def main_csv():
    lista_alumnos= []
    with open('personas-certificadas.csv', 'r', encoding='utf-8') as arch:
        primer_linea= True
        for linea in arch:

            if primer_linea:
                primer_linea= False
                continue

            campos= linea[:-1].split(',')
            alumno= Alumno(campos[1], 
                           campos[0], 
                           campos[2], 
                           campos[3],
                           campos[4], 
                           campos[5],
                           campos[6],
                           campos[7],
                           campos[8])
            lista_alumnos.append(alumno)
    
    for i in range(2):
        print(lista_alumnos[i])

    contador_cba= 0
    contador_tuc= 0
    al_cba= []
    al_tuc= []
    for al in lista_alumnos:
        if al.idProvincia == "14":
            contador_cba += 1
            al_cba.append(al)
        if al.idProvincia == "90":
            contador_tuc += 1
            al_tuc.append(al)


    print("Alumnos cordoba: ", contador_cba)
    print("Alumnos tucuman: ", contador_tuc)

    with open('al_cba.csv', 'w', encoding='utf-8') as arch:
        for a in al_cba:
            arch.write(f"{a.dni}|{a.apellido}|{a.nombre}\n")



if __name__ == '__main__':
    # main_escribir()
    # main_leer()
    main_csv()