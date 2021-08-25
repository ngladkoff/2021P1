def ordenar_vector(vector):
    #for j in range(len(vector) - 1):
    contador= 0
    desordenado = True
    while desordenado:
        contador += 1
        print(contador)
        desordenado= False 
        for i in range(len(vector)- 1):
            if vector[i] > vector[i + 1]:
                desordenado= True
                aux = vector[i]
                vector[i] = vector[i +1]
                vector[i + 1] = aux
                # a, b = b, a
def busqueda_binaria(valorBuscado, vector):
    inicio = 0
    final = len(vector) - 1
    while final >= inicio :
        medio = (final + inicio) // 2
        if vector[medio] == valorBuscado:
            return medio
        elif vector[medio] > valorBuscado:
            final = medio -1 
        elif vector[medio] < valorBuscado:
            inicio = medio + 1
    
    return -1


def main ():
    #arreglo_desordenado = [2, 9, 8 , 3, 7,1]
    arreglo_desordenado = [1, 2, 9, 3, 7,8]
    print('Principal')
    print(arreglo_desordenado)
    ordenar_vector(arreglo_desordenado)
    print(arreglo_desordenado)

    indice = busqueda_binaria(6, arreglo_desordenado)
    print(indice)

if __name__ == '__main__' :
    main()