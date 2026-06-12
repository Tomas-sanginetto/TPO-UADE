def registrar_venta(lst_titulos, lst_entradas, lst_valores, lst_estados):
    '''Registra ventas de entradas. El usuario podrá seleccionar una película y la cantidad de entradas a vender'''

    indice = ingresar_titulo("Seleccione una pelicula:", lst_titulos)

    if lst_estados[indice] == "Finalizada":
        print("No se pueden vender entradas de una pelicula finalizada.")
        return

    if lst_entradas[indice] == 0:
        print("Funcion agotada, no quedan entradas disponibles.")
        return

    cantidad = ingresar_positivo("Ingrese cantidad de entradas a vender: ")

    if cantidad > lst_entradas[indice]:
        print("No hay entradas suficientes.")
        print("Entradas disponibles: ", lst_entradas[indice])
        return

    total = cantidad * lst_valores[indice]

    print("Total a pagar: $", total)

    lst_entradas[indice] = lst_entradas[indice] - cantidad

    print("Venta registrada correctamente.")
