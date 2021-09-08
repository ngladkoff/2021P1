from dataclasses import dataclass


@dataclass
class Solicitud:
    """
    Clase que define el tipo de dato donde vamos a guardar la solicitud
    """
    nro: int
    cliente: str
    zona: int
    tecnico: int


class ValMinMaxError(Exception):
    """
    Error por fuera de rango
    """
    pass


def validar_valor(valor, valmin, valmax):
    """
    Función para validar si un valor está dentro de un rango
    Si no lo está levanta el error ValMinMaxError
    """
    if valor < valmin:
        raise ValMinMaxError
    if valor > valmax:
        raise ValMinMaxError


def ingresar_numero(mensaje, min, max, msgerror):
    """
    Función para solicitar al usuario el ingreso de un 
    número entero

    Args:
        mensaje (str): Mensaje a mostrar al momento de solicitar el valor
        min (int): Valor mínimo admitido
        max (int): Valor máximo admitido
        msgerror (str): Mensaje a mostrar si el valor ingresado esta fuera de rango

    Returns:
        [int]: Retorna el valor ingresado
    """
    while True:
        try:
            valor = int(input(mensaje))
            validar_valor(valor,min,max)
            return valor
        except ValueError:
            print("Debe ingresar un número")
        except ValMinMaxError:
            print(msgerror)


def cargar_solicitud(solicitudes):
    """
    Función para solicitar los datos al usuario de una solicitud
    y cargarlos en una nueva solicitud

    Args:
        solicitudes (List<Solicitud>): Lista de solicitudes

    Returns:
        [Solicitud]: Retorna una solicitud cargada
    """
    solicitud = Solicitud(0,'',0,0)
    print(solicitud)
    solicitud.cliente = input('Ingrese un cliente :')
    solicitud.zona = ingresar_numero('Ingrese una zona 1-Pinamar, 2-Ostende, 3-Valeria, 4-Carilo',1,4,'Ingrese una zona valida entre 1 y 4' )
    solicitud.nro = len(solicitudes) + 1
    return solicitud


def buscar_cliente_en_otra_solicitud(solicitudes, solicitud):
    """
    Función para buscar si el cliente ya tiene asignado técnico en otra solicitud

    Args:
        solicitudes (Lista<Solicitud>): Lista de Solicitudes
        solicitud (Solicitud): Solicitud sobre la que estamos buscando asignar técnico

    Returns:
        [type]: [description]
    """
    for i in range(len(solicitudes)):
        if solicitud.cliente == solicitudes[i].cliente and solicitudes[i].tecnico != 0:
            return solicitudes[i].tecnico
    return 0


def tecnico_disponible(tecnico, solicitudes):
    """
    Función para verificar si un técnico 
    tiene disponibilidad para que se le 
    asignen más solicitudes

    Args:
        tecnico (int): Número de técnico
        solicitudes (List<Solicitud>): Lista de solicitudes

    Returns:
        [bool]: Retorna Verdadero si tiene disponibilidad
    """
    cont = 0
    for i in range(len(solicitudes)):
        if solicitudes[i].tecnico == tecnico:
            cont += 1
    if cont >= 4 :
        return False
    else: 
        return True


def buscar_zona_tecnico(tec, solicitudes):
    """
    Función para buscar si un técnico ya fue asignado a una zona

    Args:
        tec (int): Número de técnico a buscar
        solicitudes (List<Solicitud>): Lista de solicitudes

    Returns:
        int: Número de zona a la que el tecnico está asignado, o 0 si no lo está
    """
    # Recorro la lista de solicitudes
    for i in range(0, len(solicitudes)):
        # Si sobre la solicitud del indice i
        # el técnico asignado coincide con el técnico
        # que estoy buscando
        if solicitudes[i].tecnico == tec:
            # Devuelvo a que zona está asignado ese tecnico
            # sacando el dato de la solicitud a la que está asignado
            return solicitudes[i].zona

    # Si salí del for, quiere decir que recorrí la lista y no encontré 
    # ninguna solicitud en la que el tecnico asignado a la solicitud 
    # coincidiera con el técnico buscado
    # Por eso devuelvo 0 (no asignao a ninguna zona)
    return 0



def buscar_tecnico(i, solicitudes):

    # Primero tengo que buscar si para el mismo cliente ya hay otra solicitud con técnico asignado
    tecnico = buscar_cliente_en_otra_solicitud(solicitudes, solicitudes[i])
    # Si encontramos técnico
    if tecnico != 0:
        # Verifico si tiene disponibilidad
        if tecnico_disponible(tecnico, solicitudes):
            # Entonces encontré el tecnico para la solicitud, lo devuelvo
            return tecnico

    # Si llegué a este punto o bien técnico es 0 porque no había otra solicitud para el mismo cliente
    # o bien el tecnico no tenía disponibilidad
    # Entonces recorro la lista de técnicos y trato de asignarle uno

    for tec in range(1, 11):
        # Primero verifico si el técnico tiene disponibilidad
        # Para eso reutilizo la función que hicimos antes
        if not tecnico_disponible(tec, solicitudes):
            # Si el técnico no tiene disponibilidad
            # continuo con el próximo técnico
            continue

        # Si el tecnico tiene disponibilidad tengo que validar
        # si el técnico ya está asignado a una solicitud para verificar la zona
        zona_tecnico = buscar_zona_tecnico(tec, solicitudes)

        # Si el técnico no está asignado a ninguna zona
        # o si el técnico está asignado a la misma zona que la solicitud a procesar
        if zona_tecnico == 0 or zona_tecnico == solicitudes[i].zona:
            # entonces encontré el técnico y lo devuelvo
            return tec

    # Si llegué hasta acá es porque no pude asignar técnico, asi que devuelvo cero
    return 0


def asignar_tecnicos(solicitudes):
    """
    Función para asignar técnicos a las solicitudes

    Args:
        solicitudes (List<Solicitud>): Lista de solicitudes
    """

    # Recorro la lista de solicitudes (porque tengo que procesarlas todas)
    for i in range(len(solicitudes)):
        """
        El ejercicio nos da una serie de pautas para la asignación de tecnicos
        la primera es que si ya tiene tecnico no hagamos nada, si no tiene que
        intentemos buscar un técnico para esa solicitud que cumpla una serie de
        reglas y por último que avisemos al usuario si no pudimos encontrar un 
        tecnico para alguna solicitud.
        Estos 3 pasos son los que vamos a hacer.
        """

        # Primer paso -> Primer validación: si ya tiene técnico asignado entonces no lo cambio
        if solicitudes[i].tecnico != 0:
            # Sigo con la próxima solicitud, con esta solicitud no hago nada más
            continue

        # Segundo paso -> Si no tiene técnico asignado entonces necesito buscar técnico
        # Por lo tanto paso esa responsabilidad de buscar técnico a otra función
        # para no ensuciar esta función con toda esa lógica... que la encapsulo en 
        # la función buscar_tecnico()
        # (acá estoy agregando una función más que lo q vimos en clase)
        tecnico = buscar_tecnico(i, solicitudes)

        # Tercer paso -> Verifico si pude encontrar un técnico
        if tecnico == 0:
            print("No se pudo encontrar un técnico para la solicitud " + str(i + 1))
        else:
            solicitudes[i] = tecnico


def menu():
    print("=" * 10)
    print("Menu")
    print("0-Salir")
    print("1-Cargar Solicitud")
    print("2-Asignar Técnicos")
    print("3-Listado")
    print("=" * 10)
    op = ingresar_numero("Ingrese opción: ", 0, 3, "Ingrese un número entre 0 y 3")
    return op


def main():
    solicitudes = []
    while True:

        op= menu()
        if op == 1:
            #Llamo a la función para cargar solicitud
            solicitud = cargar_solicitud(solicitudes)
            #Agrego la nueva solicitud a la lista de solicitudes
            solicitudes.append(solicitud)
            print("La solicitud se ha agregado")
        elif op == 2:
            #Llamo a la función para asignar los tecnicos a todas las solicitudes
            asignar_tecnicos(solicitudes)
        elif op == 3:
            #Llamo a la función para mostrar por pantalla todas las solicitudes
            imprimir_solicitudes(solicitudes)
        elif op == 0:
            print("Chau")
            return
        else:
            print("Opción inválida")


if  __name__ == "__main__":
    main()