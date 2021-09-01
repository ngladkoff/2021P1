from dataclasses import dataclass
from typing import List

@dataclass
class Fecha:
    dia:int
    mes:int
    anio:int

@dataclass
class Horario:
    horas:int
    minutos:int
    segundos:int

@dataclass
class Producto:
    nombre:str
    precio_unitario:float
    fecha: Fecha

class FueraDeRangoError(Exception):
    pass

class ValorMenorMin(Exception):
    ...

class ValorMayorMax(Exception):
    ...

def convertir_texto_numero(texto, min, max):
    numero = int(texto)
    if numero < min:
        raise ValorMenorMin()
    if numero > max:
        raise ValorMayorMax
    return numero


def ingresar_numero(mensaje, min, max, errmsgmin, errmsgmax):
    numero = 0
    while True:
        try:
            texto = input(mensaje)
            numero = convertir_texto_numero(texto, min, max)
            return numero
        except ValueError:
            print("Debe ingresar un numero")
        except ValorMenorMin:
            print(errmsgmin)
        except ValorMayorMax:
            print(errmsgmax)

"""
# 1
h= Horario(0,0,0)
h.hora= int(input("hora"))
h.minutos= int(input("min"))
# 2
hora= int(input("hora"))
minutos= int(input("min"))
horario= Horario(hora, minutos, 0)
"""
def cargar_horario():
    horario= Horario(0,0,0)
    horario.horas = ingresar_numero('Ingrese hora:',
                                    0,
                                    23,
                                    'La hora debe ser mayor o igual a 0', 
                                    'La hora debe ser menor o igual a 23')
    
    horario.minutos = ingresar_numero('Ingrese minutos',0,59,'Los min deben ser mayor o igual a 0', 'Los min deben ser menores o igual a 59')
    horario.segundos = ingresar_numero('Ingrese segundos',0,59,'Los seg deben ser mayor o igual a 0', 'Los seg deben ser menores o igual a 59')
    return horario

def main():
    print(cargar_horario())

if __name__== '__main__':
    main()