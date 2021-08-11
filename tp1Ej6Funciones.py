
def parte1(p1):
    for i in range(p1):
        print("**********")


def parte2(cant_filas):
    for i in range(1, cant_filas + 1):
        # print("*" * (i + 1) * 2)
        for f in range(i):
            print("**", end='')
        print()
    return "listo"