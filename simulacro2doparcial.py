# Simulacro Segundo Parcial
from dataclasses import dataclass
from typing import List


@dataclass
class Prestacion:
    nro_afiliado: int
    cod_prestacion: int
    importe: float


def leer_archivo():
    lista = []
    with open('obrasocial.csv', 'r', encoding='utf-8') as arch:
        for linea in arch:
            campos = linea[:-1].split(';')
            pr = Prestacion(0,0,0.0)
            pr.nro_afiliado = int(campos[0])
            pr.cod_prestacion = int(campos[1])
            lista.append(pr)
            # lista.append(Prestacion(int(campos[0]), int(campos[1]), 0.0))
    return lista


def calcular_importes(prestaciones: List[Prestacion]):
    for prestacion in prestaciones:
        prestacion.importe = calcular_importe(prestacion)


def calcular_importe(prestacion: Prestacion):
    imp_prest = calcular_imp_prest(prestacion.cod_prestacion)
    por_afiliado = calcular_por_afiliado(prestacion.nro_afiliado, prestacion.cod_prestacion)
    importe = imp_prest * (1 - por_afiliado/100)
    return importe


def calcular_imp_prest(cod_prestacion):
    if cod_prestacion == 100:
        return 1000
    elif cod_prestacion == 200:
        return 2000
    elif cod_prestacion == 300:
        return 3000
    elif cod_prestacion == 400:
        return 4000
    else:
        return 0


def calcular_por_afiliado(nro_afiliado, cod_prestacion):
    if nro_afiliado <= 30000:
        return 0
    elif nro_afiliado > 60000:
        return 80
    else:
        if cod_prestacion == 100 or cod_prestacion == 200:
            return 0
        else:
            return 40


def crear_liquidacion(prestaciones: List[Prestacion]):
    with open('liq.txt', 'w', encoding='utf-8') as arch:
        arch.write(f'{"Nro. Afiliado":^20}|{"Cod.Prestacion":^20}|{"Importe":>15}\n')
        for prest in prestaciones:
            arch.write(f'{prest.nro_afiliado:^20}|{prest.cod_prestacion:^20d}|{prest.importe:15f}\n')


def calcular_totales(prestaciones):
    totales = [0,0,0,0,0]
    totales[0] = calcular_importe_total(prestaciones)
    totales[1] = len(prestaciones)
    totales[2] = calcular_cant_srv_categ(0, prestaciones)
    totales[3] = calcular_cant_srv_categ(1, prestaciones)
    totales[4] = calcular_cant_srv_categ(2, prestaciones)
    return totales


def calcular_cant_srv_categ(cat, prestaciones: List[Prestacion]):
    cant= 0
    for prest in prestaciones:
        if obtener_cat(prest.nro_afiliado) == cat:
            cant += 1
    return cant


def obtener_cat(nro_afiliado):
    if nro_afiliado <= 30000:
        return 0
    elif nro_afiliado > 60000:
        return 2
    else:
        return 1


def calcular_importe_total(prestaciones: List[Prestacion]):
    total = 0
    for prest in prestaciones:
        total += prest.importe
    return total


def imprimir_totales(totales):
    print(f'Importe total a reintegrar por la Obra Social {totales[0]}')
    print(f'Cantidad total de Servicios {totales[1]}')
    print(f'Cantidad servicios Star {totales[2]}')
    print(f'Cantidad servicios Medium {totales[3]}')
    print(f'Cantidad servicios Basic {totales[4]}')


def main():
    # LEER ARCHIVO CSV
    prestaciones = leer_archivo()
    # CALCULAR IMPORTES
    calcular_importes(prestaciones)
    # CREO LIQUIDACION
    crear_liquidacion(prestaciones)
    # CALCULAR TOTALES
    totales = calcular_totales(prestaciones)
    # MOSTRAMOS TOTALES
    imprimir_totales(totales)

if __name__ == "__main__":
    main()
