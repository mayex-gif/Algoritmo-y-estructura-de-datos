"""
14. Modelo Parcial 2019
Una compañía de servicios de limpieza desea un programa para procesar los datos de los trabajos ofrecidos. Por cada trabajo se tienen los siguientes datos: 
el número de identificación del trabajo, la descripción o nombre del mismo, el tipo de trabajo (un valor de 0 a 3, 0:interior, 1:exterior, 2:piletas, 3:tapizados), 
el importe a cobrar por ese trabajo y la cantidad de personal afectado para prestar ese servicio. Se desea almacenar la información referida a los n trabajos en un 
arreglo de registros de trabajos (definir el Trabajo y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones, que permita gestionar las siguientes tareas:
1- Cargar el arreglo pedido con los datos de los n trabajos. Valide que el número identificador del trabajo sea positivo y que el importe a cobrar sea mayor a cero. 
Puede hacer la carga en forma manual, o puede generar los datos en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos 
una debe programar.
2- Mostrar todos los datos de todos los trabajos, en un listado ordenado de mayor a menor según los importes a cobrar.
3- Determinar y mostrar los datos del trabajo que tenga la mayor cantidad de personal afectado (no importa si hay varios trabajos con la misma cantidad máxima de personal: 
se pide mostrar uno y sólo uno cuya cantidad de personal sea máxima).
4- Determinar si existe un trabajo cuya descripción sea igual a d, siendo d un valor que se carga por teclado. Si existe, mostrar sus datos. Si no existe, informar con un
 mensaje. Si existe más de un registro que coincida con esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre.
5- Determinar y mostrar la cantidad de trabajos por tipo.
"""


class Trabajo:
    def __init__(self, num, nom, tipo, imp, c_per):
        self.numero = num
        self.nombre = nom
        self.tipo = tipo
        self.importe = imp
        self.cant_personal = c_per


def write(trabajo):
    print("Numero:", trabajo.numero, end=" - ")
    print("Nombre:", trabajo.nombre, end=" - ")
    print("Tipo:", trabajo.tipo, end=" - ")
    print("Importe: $", trabajo.importe, end=" - ")
    print("Cantidad de personas:", trabajo.cant_personal)


def principal():
    t = Trabajo(1, "Trabajo prueba", 2, 2344.5, 6)
    write(t)


if __name__ == "__main__":
    principal()
    