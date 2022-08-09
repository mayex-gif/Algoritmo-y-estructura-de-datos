"""
2. Empresa de transportes
Una empresa dedicada al transporte de mercadería solicita un programa para manejar estadísticas de sus envios.
Para ello solicita un programa, controlado por menú con opciones para lo siguiente:

- Ingresar los datos de los transportes realizados en el mes, de cada uno se conoce:
    - dia del mes (1-31)
    - Descripción
    - Monto del transporte

- Determinar el monto promedio obtenido en el mes
- Genere un listado de los envíos realizados, ordenado por importe en forma decreciente
- Determine que día del mes tuvo mayor cantidad de transportes realizados
"""


# Imports
import random


# Opcion-1
def cargar(dias, descripcion, monto):
    for i in range(len(dias)):
        dias[i] = int(random.randint(1, 31))
        descripcion[i] = "Transpoder " + str(i + 1)
        monto[i] = int(random.uniform(1000, 10000))


# Opcion-2
def promedio_mensual(monto):
    acumulador = 0
    for i in range(len(monto)):
        acumulador += monto[i]
    return acum / len(monto)

# Opcion-3
def selection_sort(dias, descripcion, monto):
    n = len(dias)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if monto[i] < monto[j]:
                monto[i], monto[j] = monto[j], monto[i]
                descripcion[i], descripcion[j] = descripcion[j], descripcion[i]
                dias[i]. dias[j] = dias[j], dias[i]


# Opcion-4
def mayor_cantidad(dias):
    cont = [0] * 31
    for i in range (len(dias)):
        cont[dias[i] - 1] += 1

    mayor = 0
    for i in range(1, len(cont)):
        if cont[i] > cont[mayor]:
            mayor = i
    return mayor


# Principal
def principal():
    opcion = 0
    menu = "Menu\n 1-Ingresar los datos de los transportes realizados en el mes \n 2-Determinar el monto promedio obtenido \"
    " en el mes\n 3-Genere un listado de los envíos realizados, ordenado por importe en forma decreciente\n 4-Determine que \"
    "día del mes tuvo mayor cantidad de transportes realizados\n 5-Salir\n"
    n = int(input("Ingrese la cantidad de envios: "))
    dias = [0] * n
    descripcion = [0] * n
    monto = [0] * n

    while opcion == 0:
        print(menu)
        opcion = int(input("Ingrese la opcion que desea reaizar."))
        while opcion <= 0 or opcion >= 6:
            print("\nERROR - USTED INGRESO UN NUMERO \n")
            opcion = int(print("Ingrese la opcion que desea reaizar. "))
        if opcion == 1:
            cargar(dias, descripcion, monto)
        elif opcion == 2:
            promedio_mensual(monto)
        elif opcion == 3:
            selection_sort(dias, descripcion, monto)
        elif opcion == 4:
            mayor_cantidad(dias)
            print("Dia Del mes que tuvo mayor cantidad de transportes realizados: ",mayor + 1)
        elif opcion == 5:
            print("Usted selecciono la opcion '5-Salir'\n")
            print("MUCHAS GRACIAS POR USAR NUESTROS SERVICIOS")
        


if __name__ == "__main__":
    principal()