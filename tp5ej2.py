class TextoNumeroError(Exception):
    pass

def sumar_numeros(numero1: str, numero2: str):
    try:
        # return int(numero1 + numero2)
        return int(numero1) + int(numero2)
    except ValueError:
        raise TextoNumeroError

def main():
    try:
        a= sumar_numeros("a", "-2")
        print("suma:",a)
    except TextoNumeroError:
        print("error")


if __name__ == '__main__':
    main()

