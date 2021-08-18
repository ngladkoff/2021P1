def sumaAcumulada (lista):
    listaAcumulada = []
    sum = 0
    for i in range (len(lista)):
        sum += lista[i]
        listaAcumulada.append(sum)
    return listaAcumulada

print( sumaAcumulada([1,2,3,10,20]))

def decifrar (clave):
    clave1 = ""
    clave2 = ""
    for i in range(len (clave)):
        if ((i + 1) % 2 == 0):
            clave2 += clave[i]
        else :
            clave1 += clave[i]
    return clave1, clave2

print(decifrar("1829345"))        