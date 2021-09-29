# Ejercicio integrador brii
from dataclasses import dataclass
@dataclass
class Departamentos:
   numero_unidad: int
   descripcion : str
   metros_cuadrados: int
   estado: int
   precio_venta: float
class valorfueraderango(Exception):
    pass
def validarvalor(valor,min,max):
    if valor < min or valor > max: 
        raise valorfueraderango

def ingresar_numero(mensaje, min, max, mensajeerror):
    while True:
        try:
            valor = int(input(mensaje))
            validarvalor(valor,min,max)
            return valor
        except ValueError:
            print('Ingrese un numero entero: ')
        except valorfueraderango:
            print(mensajeerror)
def metros ():
    print('Ingresar los metros deseados del departamento.')
    metros = ingresar_numero('Ingrese los metros cuadrados: ',1, 1000, 'Debe ingresar un numero:')
    if metros < 100:
        return 10
    elif metros > 100 and metros < 200:
        return 8
    elif metros > 200:
        return 5
    else:
        return 0
def depa_descripcion(metros):
    depa= Departamentos(0,'',0,0,0.0)
    if metros == 10:
        depa.descripcion = 'pequenio'
    elif metros == 8:
        depa.descripcion = 'mediano'
    elif metros == 5:
        depa.descripcion = 'grande'
        
        
def estado_departamento():
    print('Ingrese si el departamento se encuentra: \nSi esta libre: 1 \nSi esta reservado: 2 \nSi esta vendido: 3')
    estado = int(input('Ingrese la opcion que corresponda: '))
    
    if estado == 1:
        return 1
    elif estado == 2:
        return 2
    elif estado == 3:
        return 3
    
def preponderacion_estado(departamentos):
    departamentos_libres= []
    for i in range (len(departamentos)):
        if departamentos[i].estado == 1:
            departamentos_libres.append(departamentos[i].estado)
            departamentos_libres.append(departamentos[i].descripcion)
    return departamentos_libres
   
    
    

def datos_depa (departamentos):
    depart= Departamentos(0,'',0,0,0.0)
    depart.numero_unidad = len(departamentos) + 1
    depart.descripcion = input('Ingrese una descripcion:  ')
    depart.metros_cuadrados = metros()
    depart.estado = estado_departamento()
    #depart.precio_venta= pass
    return depart

def menu():
    print ('Bienvenido a Constructora')
    print(f'Elija una opcion para continuar.')
    print(f'------------------------------')
    print(f'Opcion 0: Salir del sistema.')
    print(f'Opcion 1: Cargar departamentos.')
    print(f'Opcion 2: Listar todos los departamentos en estado "Libre".') 
    print(f'Opcion 3: Informar la cantidad de departamentos en cada estado.')
    print(f'Opcion 4: Reservar departamentos.')
    valor = ingresar_numero('Ingrese una opcion: ', 0, 4, 'Ingrese un numero entre 0 y 4.')
    return valor
def main ():
    departamentos= []
    while True:
        seleccion = menu()
        if seleccion == 0:
            print ('gracias por usar nuestro programa \n Adios!')
           
            break
        elif seleccion == 1:
            datos = datos_depa(departamentos)
            departamentos.append(datos)
        elif seleccion == 2:
            salida= preponderacion_estado(departamentos)
            print(salida)
            
if __name__=='__main__':
    main()