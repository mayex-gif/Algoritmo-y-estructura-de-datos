"""
Se pide desarrollar un programa en Python para el enunciado que sigue. El programa obligatoriamente deberá plantearse 
como un proyecto que contenga al menos dos módulos (uno para la definición del tipo de registro y las funciones para gestionarlo 
(a criterio del estudiante) y otro módulo deberá contener el programa principal que obligatoriamente debe ser planteado en base a un menú de opciones y con funciones para toda situación posible.

Una empresa agropecuaria necesita un programa para procesar los datos de los trabajos ofrecidos. Por cada trabajo se tienen los 
siguientes datos: el número de identificación, la descripción del trabajo, el tipo de trabajo (un número entero entre 0 y 19, para indicar por ejemplo: 0: 
siembra, 1: control de plagas, 2: cosecha, etc.), el importe a cobrar por ese trabajo y la cantidad de personal afectado al mismo. Se desea almacenar la 
información referida a estos trabajos en un arreglo de registros de tipo Trabajo (definir el tipo Trabajo y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos, que permita 
gestionar las siguientes tareas:

1-      Cargar el arreglo pedido con los datos de los n trabajos. Valide que el número identificador del trabajo sea positivo y que el tipo del servicio 
esté entre 0 y 19. Puede hacer la carga en forma manual, o puede generar los datos en forma automática (con valores aleatorios) o puede disponer de ambas 
técnicas si lo desea. Pero al menos una debe programar.

2-      Mostrar todos los datos de todos los trabajos cuya cantidad de personal sea mayor a 3, en un listado ordenado de mayor a menor según los números de 
identificación de esos trabajos. Al final del listado, mostrar además la suma de los importes de todos los registros mostrados.

3-      Determinar y mostrar la cantidad de trabajos que se ofrecen de cada tipo posible de (un contador para los trabajos tipo 0, otro para el tipo 1, etc.) 
En total, 20 contadores. Muestre solo los resultados mayores a cero.

4-      Mostrar los datos de todos los trabajos cuyo importe a cobrar sea mayor al importe promedio de todos los trabajos del arreglo

5-      Determinar si existe un trabajo cuyo número de identificación sea igual a num y que sea del tipo t, siendo num y t dos valores que se cargan por teclado. 
Si existe, mostrar sus datos. Si no existe, informar con un mensaje. Si existe más de un registro que coincida con esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre.
"""

from generales import *
import random


class Agro:
    def __init__(self, num, desc, tipo, prec, cant):
        self.numero = num
        self.descripcion = desc
        self.tipo = tipo
        self.precio = prec
        self.cantidad = cant


def cargar_datos(n):
    v = n * [0]
    for i in range(n):
        num = random.randint(1, 10000)
        desc = random.randint(1,10)
        tipo = random.randint(0, 19)
        prec = random.randint(1000, 5000)
        cant = random.randint(1, 15)
        v[i] = Agro(num, desc, tipo, prec, cant)
    return v


def selection_sort(arreglo):
    n = len(arreglo)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arreglo[i].numero < arreglo[j].numero:
                arreglo[i], arreglo[j] = arreglo[j], arreglo[i]


def contar_por_tipo(arreglo):
    acum = [0] * 20
    for i in arreglo:
        acum[i.tipo] += 1

    for i in range(len(acum)):
        if acum[i] > 0:
            t = ("Tipo de trabajo N°: {:<2} | Cantidad de trabajos: {}")
            print(t.format(i, acum[i]))


def mostrar_may_prom(arreglo):
    total = prom = 0
    for i in arreglo:
        total += i.precio
    prom = total // len(arreglo)
    for i in arreglo:
        if i.precio > prom:
            return print(write(i))
    print("El promedio es: $", prom)


def buscar_por_nt(arreglo, n, t):
    for i in arreglo:
        if i.numero == n and i.tipo == t:
            print (write(i))
    return print("\nNo existe ese registro...")


def principal():
    trabajos = None
    opcion = 0
    while opcion != 6:
        opcion = int(input(menu()))
        if opcion == 1:
            print("\n" + 50 * "=" + " CARGAR DATOS " + 50 * "=" + "\n")
            n = validar(0, "Ingrese un numero(mayor que 0): ")
            trabajos = cargar_datos(n)
        if trabajos is not None and len(trabajos) > 0:
            if opcion == 2:
                print("\n" + 50 * "=" + " MOSTRAR DATOS " + 50 * "=" + "\n")
                selection_sort(trabajos)
                mostrar_vector(trabajos)
                input("Presione enter para continuar...")
            elif opcion == 3:
                print("\n" + 50 * "=" + " CONTADOR POR TIPO " + 50 * "=" + "\n")
                contar_por_tipo(trabajos)
                input("Presione enter para continuar...")
            elif opcion == 4:
                print("\n" + 50 * "=" + " MOSTRAR MAYORES AL PROMEDIO " + 50 * "=" + "\n")
                mostrar_may_prom(trabajos)
                input("Presione enter para continuar...")
            elif opcion == 5:
                print("\n" + 50 * "=" + " BUSCAR POR NUMERO DE IDENTIFICADOR " + 50 * "=" + "\n")
                n = int(input("\nIngrese un numero de identificador a buscar: "))
                t = int(input("Ingrese un tipo de trabajo a buscar: "))
                buscar_por_nt(trabajos, n, t)
                input("\nPresione enter para continuar...")


if __name__ == "__main__":
    principal()
