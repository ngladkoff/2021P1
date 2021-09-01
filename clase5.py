from dataclasses import dataclass
from typing import List

@dataclass
class Fecha:
    dia: int
    mes: int
    anio: int

@dataclass
class Direccion:
    calle: str
    altura: int
    localidad: str

@dataclass
class Persona:
    nombre: str
    apellido: str
    direcciones: List[Direccion]
    fecha_nac: Fecha


class Servicio:
    def __init__(self, nombre, costo):
        self.nombre= nombre
        self.costo= costo
    def __repr__(self):
        return "Servicio(nombre='{0}', costo='{1}')".format(self.nombre, self.costo)

def imprimir_servicio(srv: Servicio):
    print(srv.nombre, srv.costo)


def main():
    legales= Servicio("Asesoria Legal", 1000)
    contables= Servicio("Asesoria Contable", 1500)
    imprimir_servicio(legales)
    imprimir_servicio(contables)
    direc1 = Direccion("Bunge", 1200, "Pinamar")
    direc2 = Direccion("Bunge", 1300, "Pinamar")
    direcc= [direc1, direc2]
    print(direc1)
    print(legales)
    p= Persona("Carlos", "Perez", direcc, Fecha(1,1,1900))
    print(p.fecha_nac.anio)
    r= Persona("Carlos", "Garcia", direcc, Fecha(1,1,1950))
    print(r.fecha_nac.anio)
    print(p.direcciones)


main()