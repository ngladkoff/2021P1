# from constantes import NOMBRE_SISTEMA, IVA
import constantes as ctes
import funciones as f1
import funciones2 as f2

def mostrar_menu():
    print(ctes.NOMBRE_SISTEMA)
    print(ctes.IVA)
    op= int(input("Ingrese opcion: "))
    if op == 1:
        f1.opcion_1(4)
    elif op == 2:
        f2.opcion_2()


def main():
    print("Mostrar menu desde modulo menu")
    mostrar_menu()
