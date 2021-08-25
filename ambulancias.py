INDICE_NUMERO_AMBULANCIA= 0
INDICE_DIA_AMBULANCIA = 1
INDICE_SERVICIOS_AMBULANCIA = 2
INDICE_KILOMETROS_AMBULANCIA = 3

class ErrorValorMinimo(Exception):
    pass

class ErrorValorMaximo(Exception):
    pass

def inicializar_vector(vector, cant, valor_inicial):
    for i in range(0, cant):
        vector.append(valor_inicial)
    

def cargar_totales_ambulancias(ambulancias, ambulancias_numeros, ambulancias_servicios, ambulancias_kilometros):
    
    # Buscar numeros ambulancias
    for ambulancia in ambulancias:
        if ambulancia[INDICE_NUMERO_AMBULANCIA] not in ambulancias_numeros:
            ambulancias_numeros.append(ambulancia[INDICE_NUMERO_AMBULANCIA])

    tamanio= len(ambulancias_numeros)
    inicializar_vector(ambulancias_kilometros, tamanio, 0)
    inicializar_vector(ambulancias_servicios, tamanio, 0)

    for i in range(0, len(ambulancias_numeros)):
        for ambulancia in ambulancias:
            if (ambulancia[INDICE_NUMERO_AMBULANCIA] == ambulancias_numeros[i]):
                ambulancias_servicios[i] += ambulancia[INDICE_SERVICIOS_AMBULANCIA]
                ambulancias_kilometros[i] += ambulancia[INDICE_KILOMETROS_AMBULANCIA]


def buscar_indice_ambulancia_mayor_km_por_servicio(ambulancias):
    indice_mayor= 0
    for i in range(0, len(ambulancias)):
        promedio_i= ambulancias[i][INDICE_KILOMETROS_AMBULANCIA]/ ambulancias[i][INDICE_SERVICIOS_AMBULANCIA]
        promedio_mayor= ambulancias[indice_mayor][INDICE_KILOMETROS_AMBULANCIA]/ ambulancias[indice_mayor][INDICE_SERVICIOS_AMBULANCIA]
        if promedio_i > promedio_mayor:
            indice_mayor= i
    return indice_mayor

def ingresar_numero(mensaje,valmin,valmax):
    ingreso_usuario = int(input(mensaje))
    if ingreso_usuario < valmin:
        raise ErrorValorMinimo
    elif ingreso_usuario > valmax:
        raise ErrorValorMaximo
    return ingreso_usuario

def ingresar_dia():
    while True:
        try:
            dia= ingresar_numero("Ingrese el numero de dia", 1, 31)
            return dia
        except ValueError:
            print("Debe ingresar un numero entero")
        except ErrorValorMinimo:
            return 1
        except ErrorValorMaximo:
            print("Debe ingresar un numero de dia valido")


def informar_ambulancia_mayor_servicios_dia(dia, ambulancias):
    mayor_i= -1

    for i in range(0, len(ambulancias)):
        if dia == ambulancias[i][INDICE_DIA_AMBULANCIA]:
            if mayor_i == -1:
                mayor_i= i
            if ambulancias[i][INDICE_SERVICIOS_AMBULANCIA] > ambulancias[mayor_i][INDICE_SERVICIOS_AMBULANCIA]:
                mayor_i= i

    print("el movil de mayor cant srv es ", ambulancias[mayor_i][INDICE_NUMERO_AMBULANCIA])

def principal():
    ambulancias=[[1000,2,5,9],[200,2,4,8],[303,4,6,5],[1000,4,4,9],[1000,6,5,8],[200,3,5,10],[3,5,5,7],[2,4,4,11],[3,6,4,10]] 
    ambulancias_numeros= []
    ambulancias_servicios= []
    ambulancias_kilometros= []

    print('Ambulancias')
    cargar_totales_ambulancias(ambulancias, ambulancias_numeros, ambulancias_servicios, ambulancias_kilometros)

    indice_mayor_promedio= buscar_indice_ambulancia_mayor_km_por_servicio(ambulancias)
    #imprimo_promedio_km_por_srv()
    print(indice_mayor_promedio)
    dia= ingresar_dia()
    informar_ambulancia_mayor_servicios_dia(dia, ambulancias)





if __name__ == '__main__':
    principal()


