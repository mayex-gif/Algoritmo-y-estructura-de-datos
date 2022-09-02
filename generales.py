def menu():
    return ("\n" + 50 * "=" + " MENU DE OPCIONES " + 50 * "=" + "\n\n" +
            " 1 - Cargar trabajos\n" +
            " 2 - Mostrar trabajos\n" +
            " 3 - Cantidad de trabajos de cada tipo\n" +
            " 4 - Mostrar los datos cuyo importe a cobrar sea mayor al importe promedio\n" +
            " 5 - Buscar trabajo por su numero identificador y su tipo de trabajo\n" +
            " 6 - Salir\n\n" +
            "Ingrese su opcion: ")


def validar(limite, mensaje):
    numero = limite
    while numero <= limite:
        numero = int(input(mensaje))
        if numero <= limite:
            print('Error... El numero ingresado debe ser mayor a', limite)
    return numero\


def write(registro):
    t = ( "Número de identificacion: {:<4} | Tipo de trabajo: {:<2} | Precio: ${:<5} | Cantidad de personal afectado: {:<2} | Descripción: {}")
    return t.format(registro.numero, registro.tipo, registro.precio, registro.cantidad, registro.descripcion)


def mostrar_vector(arreglo):
    acum = 0
    for i in arreglo:
        if i.cantidad > 3:
            acum += i.precio
            print(write(i))