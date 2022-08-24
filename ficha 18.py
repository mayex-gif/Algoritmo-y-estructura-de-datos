"""
2. Analizando Temperaturas
El Servicio Metereológico Nacional solicitó un programa que mediante un menu de opciones, permita analizar las amplitudes térmicas desde diferentes puntos de vista, para ello las opciones a las que el programa debe responder son:

Cargar n analisis térmicos (n ingresado por el usuario), cuyos datos son: región, mes (numero del 1 al 12), temperatura máxima, temperatura mínima.
Permitir informar la temperatura máxima promedio en el primer semestre
Permitir informar la región y el mes en que se registró la menor mínima del año
Salir
"""


import random
random.seed(10)


class Temperatura:
    def __init__(self, region, mes, t_max, t_min):
        self.region = region
        self.mes = mes
        self.temp_max = t_max
        self.temp_min = t_min


def write(temperatura):
    print("Region:", temperatura.region, end = " - ")
    print("Mes:", temperatura.mes, end = " - ")
    print("Temperatura maxima:", temperatura.temp_max, end = " - ")
    print("Temperatura minima:", temperatura.temp_min)

# Por cada (temperaturas) creamos un registro temperatura
def cargar(temperaturas):
    regiones = ("NOA", "CENTRO", "LITORAL", "PATAGONIA", "CUYO")
    for i in range(len(temperaturas)):
        region = random.choice(regiones)
        mes = random.randint(1,12)
        t_max = random.randint(20, 45)
        t_min = random.randint(-10,20)
        temperaturas[i] = Temperatura(region, mes, t_max, t_min)


def mostrar(temperaturas):
    for i in range(len(temperaturas)):
        write(temperaturas[i])

# Punto 2
def prom_prim_sem(temperaturas):
    acumulador = contador = 0
    for i in range(len(temperaturas)):
        if temperaturas[i].mes <= 6:
            contador += 1
            acumulador += temperaturas[i].temp_max
    if contador > 0:
        promedio = acumulador / contador
    else:
        promedio = 0
    return promedio

# Punto 3
def reg_mes_tempmin(temperaturas):
    menor_temp = 0
    for i in range(len(temperaturas)):
        if temperaturas[i].temp_min < temperaturas[i + 1].temp_min:
            menor_temp = temperaturas[i].temp_min


def principal():
    n = int(input("Ingrese la cantidad de temperaturas: "))
    temperaturas = [0] * n
    cargar(temperaturas)
    mostrar(temperaturas)
    print("Temperatura maxima promedio: ", prom_prim_sem(temperaturas))


if __name__ == "__main__":
    principal()