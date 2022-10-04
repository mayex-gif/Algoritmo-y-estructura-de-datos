"""
2. Colegio Profesiones
Un colegio o asociación de profesionales mantiene información sobre sus distintos miembros. 
Por cada miembro se registran los campos siguientes: número de dni del profesional (un número entero), 
nombre del profesional (una cadena), importe que paga al colegio por mes, tipo de afiliación (un valor 
entre 0 y 4 incluidos, por ejemplo de la forma 0: vitalicio, 1: transitorio, 2: indirecto, etc.) y un 
número que identifica el tipo de trabajo que desempeña (un número entero entre 0 y 14 incluidos, para indicar 
(por ejemplo): 0: empleado, 1: jefe o director, 2: administrativo, etc.) Se pide definir un tipo registro Profesional 
con los campos que se indicaron, y un programa completo con menú de opciones para hacer lo siguiente:

1- Cargar los datos de n registros de tipo Profesional en un arreglo de registros (cargue n por teclado).
 Puede cargar los datos manualmente, o puede generarlos aleatoriamente. El arreglo debe crearse de forma que 
 siempre quede ordenado de menor a mayor, según el dni de los profesionales. Se considerará incorrecta la solución basada en cargar el arreglo completo y ordenarlo al final.

2- Mostrar el arreglo creado en el punto 1, a razón de un registro por línea.

3- Buscar en el arreglo creado en el punto 1 un profesional con dni igual a un valor doc (doc es cargado por teclado). 
Si no existe, informar con un mensaje. Si existe mostrar todos sus datos, al final agregar un mensaje que indique que 
tiene el importe desactualizado, si es menor a un valor imp (tambien cargado por teclado)

4- A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todos los profesionales cuyo 
tipo de trabajo sea 3, 4 o 5 y cuyo importe pagado mensual sea mayor a un valor x que se carga por teclado.

5- Mostrar el archivo creado en el punto 3, a razón de un registro por línea en la pantalla.

6- Buscar en el arreglo creado en el punto 1 un registro en el cual el nombre del profesional sea igual a nom
 (cargar nom por teclado). Si existe, mostrar por pantalla todos los datos de ese registro. Si no existe, 
 informar con un mensaje. La búsqueda debe detenerse al encontrar el primer registro que coincida con el patrón pedido.

7- Usando el arreglo creado en el punto 1, determine la cantidad de profesionales de cada posible tipo d 
afiliación por cada posible tipo de trabajo (o sea, 5 * 15 = 75 contadores en una matriz de conteo). Muestre sólo los resultados que sean diferentes de 0.
"""


import random
import pickle
import os.path


class Miembro:
    def __init__(self, dni, nom, imp, tip, ide):
        self.num_dni = dni
        self.nombre = nom
        self.importe = imp
        self.tipo = tip
        self.identificacion = ide


def menu():
    cadena = "\n" + "\033[0;37m" + 41 * "=" + "\033[1;33m" + " MENU DE OPCIONES " + "\033[0;37m" + "=" * 41 + "\n" + "\033[1;36m" + \
            "\n\t1 - Cargar vector\n" + \
            "\t2 - Buscar alumno por nombre\n" + \
            "\t3 - Generar una matriz cohn la cantidad de alumnos por deporte y año\n" + \
            "\t4 - Generar un archivo con alumnos de un año\n" + \
            "\t5 - Mostrar el contenido archivo generado en el punto 4\n" + \
            "\t6 - Salir\n\n" + \
            "\033[0;37m" + "=" * 100 + "\n\nIngrese una opcion:\t"
    return int(input(cadena))


def agregar_en_orden(arreglo, registro):
    n = len(arreglo)
    izq, der = 0, n - 1
    pos = n
    while izq <= der:
        c = (izq + der) // 2
        if registro.num_dni == arreglo[c].num_dni:
            pos = c
            break
        elif registro.num_dni < arreglo[c].num_dni:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    arreglo[pos:pos] = [registro]


# 1- Cargar los datos de n registros de tipo Profesional en un arreglo de registros (cargue n por teclado).
# Puede cargar los datos manualmente, o puede generarlos aleatoriamente. El arreglo debe crearse de forma que 
# siempre quede ordenado de menor a mayor, según el dni de los profesionales. Se considerará incorrecta la solución basada en cargar el arreglo completo y ordenarlo al final.
def cargar_datos(arreglo):
    n = int(input("\n\tIngrese la cantidad de datos a cargar:\t"))
    nombres = ["Alejo", "Fabricio", "Judas", "Joaquin", "Romina", "Eduardo", "Miley"] 
    for i in range(n):
        # dni = random.randint(30000000, 49999999)
        dni = random.randint(100, 200)
        nom = random.choice(nombres)
        imp = random.randint(1000, 9999)
        tip = random.randint(0, 4)
        ide = random.randint(0, 14)
        reg = Miembro(dni, nom, imp, tip, ide)
        agregar_en_orden(arreglo, reg)


# 2- Mostrar el arreglo creado en el punto 1, a razón de un registro por línea.
def mostrar_vector(arreglo):
    for i in arreglo:
        print(to_string(i))


def tipo(registro):
    tipos = ["Vitalicion", "Transitorio", "Indirecto", "Directo", "Suplente"]
    for i in range(len(tipos)):
        if registro == i:
            return tipos[i]

def identificacion(registro):
    identificaciones = ["Empleado", "Jefe", "Administrativo", "Subjefe", "Operativo", "Seguridad", "Salud", "Empresario", 
    "Codificador", "Buscador", "Empleador", "Relacionador", "Identificador", "Decodificador", "Traductor"]
    for i in range(len(identificaciones)):
        if registro == i:
            return identificaciones[i]


def to_string(registro):
    t = "DNI: {:<8} | Nombre: {:<8} | Importe: {:<4} | Tipo: {:<11} | Identificacion: {}"
    return t.format(registro.num_dni, registro.nombre, registro.importe, tipo(registro.tipo), identificacion(registro.identificacion))


# 3- Buscar en el arreglo creado en el punto 1 un profesional con dni igual a un valor doc (doc es cargado por teclado). 
# Si no existe, informar con un mensaje. Si existe mostrar todos sus datos, al final agregar un mensaje que indique que 
# tiene el importe desactualizado, si es menor a un valor imp (tambien cargado por teclado)
def buscar_miembro(arreglo):
    doc = int(input("\n\tIngrese un dni a buscar:\t"))
    n = len(arreglo)
    muestra = False
    for i in arreglo:
        if doc == i.num_dni:
            print(to_string(i))
            imp = int(input("\nIngrese un importe para determinar si esta desactualizado:\t"))
            muestra = True
    if not muestra:
        print("\nNombre no encontrado...")
        muestra = False
    elif muestra and i.importe < imp:
        print("\nTiene el importe desactualizado")


# 4- A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todos los profesionales cuyo 
# tipo de trabajo sea 3, 4 o 5 y cuyo importe pagado mensual sea mayor a un valor x que se carga por teclado.
def generar_archivo(arreglo):
    tipos = 3, 4, 5
    x = int(input("\nIngrese un importe(los que se muestran van a ser mayor):\t"))
    m = open("anio.dat", "wb")
    for i in arreglo:
        if i.tipo in tipos and i.importe > x:
            pickle.dump(i, m)
    m.close()
    print("\nArchivo anio.dat generado correctamente")


# 5- Mostrar el archivo creado en el punto 3, a razón de un registro por línea en la pantalla.
def mostrar_archivo():
    arch = "anio.dat"
    if not os.path.exists(arch):
        print("El archivo no existe")
        return
    m = open(arch, "rb")
    tam = os.path.getsize(arch)
    while m.tell() < tam:
        alumno = pickle.load(m)
        print(to_string(alumno))
    m.close()


# 6- Buscar en el arreglo creado en el punto 1 un registro en el cual el nombre del profesional sea igual a nom
# (cargar nom por teclado). Si existe, mostrar por pantalla todos los datos de ese registro. Si no existe, 
# informar con un mensaje. La búsqueda debe detenerse al encontrar el primer registro que coincida con el patrón pedido.



# 7- Usando el arreglo creado en el punto 1, determine la cantidad de profesionales de cada posible tipo d 
# afiliación por cada posible tipo de trabajo (o sea, 5 * 15 = 75 contadores en una matriz de conteo). Muestre sólo los resultados que sean diferentes de 0.


def principal():
    miembros = []
    opcion = 0
    while opcion != 8:
        opcion = menu()
        if opcion == 1:
            cargar_datos(miembros)
            print("\n\tVector generado con exito")
            input("\nPresione enter para continuar...")
        if len(miembros) == 0 and opcion != 8:
            print("\n\tNo hay datos generados")
            input("\nPresione enter para continuar...")

        elif opcion == 2:
            mostrar_vector(miembros)
            input("\nPresione enter para continuar...")

        elif opcion == 3:
            buscar_miembro(miembros)
            input("\nPresione enter para continuar...")

        elif opcion == 4:
            generar_archivo(miembros)
            input("\nPresione enter para continuar...")

        elif opcion == 5:
            mostrar_archivo()
            input("\nPresione enter para continuar...")

        elif opcion == 6:
            input("\nPresione enter para continuar...")

        elif opcion == 7:
            input("\nPresione enter para continuar...")
        
    print("\nSaliendo...")


if __name__ == "__main__":
    principal()