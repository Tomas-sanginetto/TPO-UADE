def registrar_venta(lst_titulos, lst_entradas, lst_valores, lst_estados):
    '''Registra ventas de entradas. El usuario podrá seleccionar una película y la cantidad de entradas a vender'''

    indice = ingresar_titulo("Seleccione una pelicula:", lst_titulos)

    if lst_estados[indice] == "Finalizada":
        print("No se pueden vender entradas de una pelicula finalizada.")
        return

    disponibles = sum(lst_entradas[indice])

    if disponibles == 0:
        print("Funcion agotada, no quedan entradas disponibles.")
        return

    cantidad = ingresar_positivo("Ingrese cantidad de entradas a vender: ")

    if cantidad > disponibles:
        print("No hay entradas suficientes.")
        print("Entradas disponibles: ", disponibles)
        return

    total = cantidad * lst_valores[indice]

    print("Total a pagar: $", total)

    # Marca como vendidas (False) las primeras 'cantidad' entradas que esten disponibles (True)
    vendidas = 0
    i = 0
    while vendidas < cantidad:
        if lst_entradas[indice][i] == True:
            lst_entradas[indice][i] = False
            vendidas += 1
        i += 1

    print("Venta registrada correctamente.")
