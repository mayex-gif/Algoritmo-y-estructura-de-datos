import random
from registro import *
import pickle
import os.path


class Gasto:
    def __init__(self, cod, desc, mes, suc, imp):
        self.codigo = cod
        self.descripcion = desc
        self.mes = mes
        self.sucursal = suc
        self.importe = imp

    def __str__(self):
        mensaje = "Código del gasto: " + str(self.codigo)
        mensaje += " - Descripción: " + self.descripcion
        mensaje += " - Mes: " + str(self.mes)
        mensaje += " - Sucursal: " + str(self.sucursal)
        mensaje += " - Importe: $" + str(self.importe)
        return mensaje


def test():
    gasto = Gasto(1, "Agua", 2, 0, 2546.8)
    print(gasto)


# Menu de opciones
def menu():
    return("\n" + 50 * "=" + " MENU DE OPCIONES " + 50 * "=" + "\n\n 1- Generar arreglo" + "\n 2- Mostar arreglo" + \
    "\n 3- Generar archivo" + "\n 4- Mostar arreglo" + "\n 5- Matriz a partir de vector" + "\n 6- Matriz a partir de archivo"  "\n 7- Mostrar\n\n" + \
     100 * "=" + "\n" + "Ingrese una opcion: \t")


def generar_matriz(mat):
    mat = [[0] * 12 for f in range(3)]
    
    # m = [0] * 3
    # for i in range(len(m)):
    #   m[i] = [0] * 12
    
    
    for i in argen(len(vec)):
        f = vec[i].sucursal
        c = vec[i].mes
        m[f][c] += vec[i].importe


def mostrar_matriz(mat):
    for i in range(0,len(mat)):
        print("")
        for j in range(0,len(mat[i])):
            print("Mes: ", (i+1), "Sucursal: ", (j),"- Gasto total: $", '{:.2f}'.format(mat[i][j]))
    

def generar_matriz_archivo():
    arch = "gastos.dat"
    if not os.path.exist(arch):
        print("El archivo no existe")
        return None
    mat = [12 * [0] for i in range(3)]
    m = open(arch, "rb")
    tam = os.path.getsize(arch)
    while m.tell() < tam:
        reg = pickle.load(m)
        fil = reg.sucursal
        col = reg.mes -1
        mat [fil][col] += reg.importe
    return mat


def generar_vector(gastos, n):
    descripciones = ('Agua', 'Gas', 'Luz', 'Rentas', 'Limpieza', 'Municipalidad')
    for i in range(n):
        cod = i + 1
        desc = random.choice(descripciones)
        mes = random.randint(1, 12)
        suc = random.randint(0, 2)
        imp = round(random.uniform(1000, 10000), 2)
        reg = Gasto(cod, desc, mes, suc, imp)
        add_in_order(gastos, reg)


def add_in_order(gastos, reg):
    n = len(gastos)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if reg.descripcion == gastos[c].descripcion:
            pos = c
            break
        if reg.descripcion > gastos[c].descripcion:
            izq = c + 1
        else:
            der = c - 1
    if izq > der:
        pos = izq
    gastos[pos:pos] = [reg]



def mostrar_vector(gastos):
    for i in range(len(gastos)):
        print(gastos[i])


def generar_archivo(gastos, v):
    m = open("gastos.dat", "wb")
    for i in range(len(gastos)):
        if gastos[i].importe > v:
            pickle.dump(gastos[i], m)
    m.close()


def mostrar_archivo():
    arch = "gastos.dat"
    if not os.path.exists(arch):
        print("El archivo no existe")
        return
    m = open(arch, "rb")
    tam = os.path.getsize(arch)
    while m.tell() < tam:
        gasto = pickle.load(m)
        print(gasto)
    m.close()


def totalizar_mes():
    None


def principal():
    gastos = []
    op = 0

    while op != 5:
        op = int(input(menu()))
        if op == 1:
            n = int(input("Ingrese la cantidad de gastos: "))
            generar_vector(gastos, n)
            input("Presione enter para continuar...")
        elif op == 2:
            mostrar_vector(gastos)
            input("Presione enter para continuar...")
        elif op == 3:
            v = float(input("Ingrese el valor a partir del cual generar el archivo: "))
            generar_archivo(gastos, v)
            input("Presione enter para continuar...")
        elif op == 4:
            mostrar_archivo()
            input("Presione enter para continuar...")
        elif op == 5:
            mat = generar_matriz(gastos)
            mostrar_matriz
            input("Presione enter para continuar...")
        elif op == 6:
            mat_arch = generar_matriz_archivo()
            if mat_arch != None:
                mostrar_matriz(mat_arch)
        elif op == 7:
            print("Desde el vector")
            totalizar_mes(mes, mat)
            print("Desde el archivo")
            totalizar_mes(mes, mat_arch)
            input("Presione enter para continuar...")
    print("\nHasta luego...")


if __name__ == '__main__':
    principal()
