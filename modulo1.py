from registro import *
import random


def cargar(n, trabajos):
    for i in range (n):
        num = i + 1
        nombre = "Trabajo" + str(num)
        tipo = random.randint(0, 3)
        importe = random.uniform(100, 1000)
        cant_personal = random.randint(1, 10)
        reg = Trabajo(num, nombre, tipo, importe, cant_personal) 
        trabajos.append(reg)


def mostrar(trabajos):
    for i in range(len(trabajos)):
        write(trabajos[i])


def ordenar(trabajos):
    n = len(trabajos)
    for i in range(n-1):
        for g in range(i+1, n):
            if trabajos[g].importe > trabajos[i].importe:
                trabajos[i] , trabajos[g] = trabajos[g], trabajos[i]


# Busqueda secuencial
def linear_search_por_nombre(trabajos):
    n = len(trabajos)
    x = str(input('\nIngrese un nombre a buscar: ')) # Valor a buscar
    for i in range(n):
        if x == trabajos[i].nombre:
            return i
    return -1


# 5- Determinar y mostrar la cantidad de trabajos por tipo.
def cant_trabajos_tipo(trabajos):
    cont_0 = cont_1 = cont_2 = cont_3 = 0
    n = len(trabajos)
    x = str(input('\nIngrese un tipo a buscar: '))  # Valor a buscar
    for i in range(n):
        if x == trabajos[i].tipo and trabajos[i].tipo == 0:
            cont_0 += 1
        elif x == trabajos[i].tipo and trabajos[i].tipo == 1:
            cont_1 += 1
        elif x == trabajos[i].tipo and trabajos[i].tipo == 2:
            cont_2 += 1
        elif x == trabajos[i].tipo and trabajos[i].tipo == 3:
            cont_3 += 1
    return -1


def principal():
    n = int(input("Ingrese la cantidad de trabajos a procesar:"))
    trabajos = []
    cargar(n, trabajos)
    ordenar(trabajos)
    mostrar(trabajos)
    pos_nombre = linear_search_por_nombre(trabajos)
    if pos_nombre == -1:
        print("No se encuentra un trabajo con la descripcion ingresada...")
    else:
        print("Trabajo encontrado!")
        write(trabajos[pos_nombre])
    
if __name__ == "__main__":
    principal()
