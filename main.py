"""
Vectores - Matrices - Archivos
Archivos: 1) Binarios, 2) Texto


file.object = open(archivo, modo_apertura)
                  ("archivo.txt")           Ubicado en la misma carpeta del proyecto
                  ("D:\\archivo.txt")       Le asignamos una ubicacion especifica donde se encuentra el archivo
fileobject.close()

\ = caracter
\\ = ubicacion

Operaciones que se pueden hacer con un archivo:
escritura - grabar 
lectura - leer

metodo de grabacion - write()
"""


import os


def grabar():
    m = open("archivo.txt", "w")
    m.write("Hola 1k4\n")
    m.write("Alcalde, Alejo Emanuel")
    m.close()


def leer():
    if not os.path.exists("archivo.txt"): # Garantizamos que el archivo exista...
        print("No existe el archivo")
        return
    m = open("archivo.txt", "r")
    linea1 = m.readline()
    linea1 = linea1[:-1]
    linea2 = m.readline()
    m.close()
    print("Contenido del archivo:")
    print(linea1, end= "-")
    print(linea2)


def leer_numeros():
    if not os.path.exists("numeros.txt"): # Garantizamos que el archivo exista...
        print("No existe el archivo")
        return
    m = open("numeros.txt", "r")
    print("Contenido del archivo:")
    for linea in m:
        print(linea, end="")


def leer_numeros_2():
    if not os.path.exists("numeros.txt"): # Garantizamos que el archivo exista...
        print("No existe el archivo")
        return
    acum = 0
    cont = 0
    m = open("numeros.txt", "r")
    while True:
        linea = m.readline()
        if linea == "":
            break
        if linea[-1] == "\n":
            linea = linea[:-1]
        num = int(linea) # Guardamos numeros, en el caso de que en el archivo existan numeros
        print("Numero:", num)
        acum += num
        cont += 1
    prom = acum / cont
    print("Promedio:", prom)


def principal():
    grabar()
    leer()
    leer_numeros()
    leer_numeros_2()



if __name__ == "__main__":
    principal()