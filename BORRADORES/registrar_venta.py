def registrar_venta(lst_titulos, lst_entradas, lst_valores, lst_estados, lst_stock):
    '''Registra ventas de entradas. El usuario podrá seleccionar una película y la cantidad de entradas a vender'''

    indice = ingresar_titulo("Seleccione una pelicula:", lst_titulos)

    if lst_estados[indice] == "Finalizada":
        print("No se pueden vender entradas de una pelicula finalizada.")
        return

    cantidad = ingresar_positivo("Ingrese cantidad de entradas a vender: ")

    if cantidad > lst_stock[indice]:
        print("No hay stock suficiente.")
        print("Stock disponible: ", lst_stock[indice])
        return

    total = cantidad * lst_valores[indice]

    print("Total a pagar: $", total)

    lst_stock[indice] = lst_stock[indice] - cantidad
    lst_entradas[indice] = lst_entradas[indice] + cantidad

    print("Venta registrada correctamente.")
