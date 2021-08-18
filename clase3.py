"""
lista = ['juan', 'pedro', 8, True]
for i in range(lista):
    print(i)

for i in lista:
    print(i)



a = 100
try:
    b = int(input("Ingrese numero: "))
    print("ingreso:", b)
    print(a/b)
except ZeroDivisionError:
    print("no se puede dividir por cero")
except ValueError:
    print("debe ingresar un numero")
except Exception:
    print("Error desconocido")
except:
    print("captura todo")


print("chau")

"""
class FueraDeRangoError(Exception):
    pass

def ingreso(min, max):
    numero = int(input("Ingrese un nro: "))
    if numero < min or numero > max:
        raise FueraDeRangoError()
    return numero


def ingresar_numero():
    numero= 0
    while True:
        try:
            numero= ingreso(1,100)
        except ValueError:
            print("Debe ingresar un numero")
        # except FueraDeRangoError:
        #     print("ingrese nro de 1 a 100")

def main():
    print(ingresar_numero())

if __name__ == '__main__':
    main()
