
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

def ingresar_numero(mensaje, min, max):
    numero= 0
    while True:
        try:
            texto= input(mensaje)
            numero = convertir_texto_numero(texto, min, max)
            return numero
        except ValueError:
            print("Debe ingresar un numero")
        except ValorMenorMin:
            print("ingrese nro mayor a " + str(min))
        except ValorMayorMax:
            print("ingrese nro menor a " + str(max))


def main():
    edad= ingresar_numero("Ingrese su edad: ", 0, 150)
    print(edad)
    nota= ingresar_numero("Ingrese la nota: ", 1, 10)
    print(nota)

if __name__ == '__main__':
    main()
