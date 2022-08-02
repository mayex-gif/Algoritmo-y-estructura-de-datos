"""
Desarrollar un programa que represente el recorrido de ida y vuelta del Tren de la Costa.

El recorrido del tren abarca las siguientes estaciones: Maipú, Borges, Libertador, Anchorena, Barrancas, San Isidro R,
 Punta Chica, Marina Nueva, San Fernando R, Canal, Delta.

Se pide cargar un vector que contenga el nombre de las estaciones y otros dos que representen el viaje de ida y de
vuelta del tren, respectivamente. En los dos últimos, se cargará la cantidad de pasajeros que ascendieron al tren en
la estación correspondiente.

Con la información cargada, plantear el siguiente menú de opciones:

Mostrar los datos cargados
Cuántos pasajeros en total subieron en el viaje de ida, y cuántos en el viaje de vuelta
En qué estación subió la mayor cantidad de pasajeros, durante el viaje de ida
En cuántas estaciones del viaje de vuelta no subieron pasajeros, y qué porcentaje representan
sobre el total de estaciones
Mostrar las estaciones la cantidad de pasajeros del viaje de ida fue mayor a la del viaje de vuelta
"""
# Imports
import random


# Cargar vector de cantidad 'n' por teclado
def reed(v, e):
    n = len(v)  # Tamaño vector
    # print('\nIngrese la cantidad de personas que sube en cada estacion:')
    for i in range(n):
        # v[i] = int(input('Estacion ' + str(e[i]) + ': '))
        v[i] = int(random.randint(1, 100))
    return v


# Opcion-1
def mostrar_datos_cargados(v):


# Principal
def principal():
    estaciones = ["Maipú", "Borges", "Libertador", "Anchorena", "Barrancas", "San Isidro R", "Punta Chica",
                  "Marina Nueva", "San Fernando R", "Canal", "Delta"]

    opcion = 0
    menu = "Menu\n 1-Mostrar los datos cargados \n 2-Pasajeros en total en ida o vuelta\n 3-Estacio en la que mas " \
           "subieron durante la ida\n 4-En cuantas no subieron pasajeros durante la vuelta y su porcentaje\n " \
           "5-Mostrar las estaciones la cantidad de pasajeros del viaje de ida fue mayor a la del viaje de vuelta\n " \
           "6-Salir"

    # CrearListasTamaño'estaciones'
    ida = len(estaciones) * [0]
    vuelta = len(estaciones) * [0]
    reed(ida, estaciones)
    reed(vuelta, estaciones)

    while opcion == 0:
        print(menu)
        opcion = int(input("Ingrese la opcion que desea reaizar."))
        while opcion <= 0 or opcion >= 7:
            print("\nERROR - USTED INGRESO UN NUMERO \n")
            opcion = int(print("Ingrese la opcion que desea reaizar. "))
        if opcion == 1:
            a = 1


if __name__ == "__main__":
    principal()
