
from Nuevofunciones import *

def registrar_venta(lst_titulos, lst_entradas, lst_valores, lst_estados, lst_stock):
    '''Registra ventas de entradas. El usuario podrá seleccionar una película y la cantidad de entradas a vender'''

    i = ingresar_titulo(
        "Seleccione una pelicula: ",
        lst_titulos
    )
    
    if lst_estados[i] == "Finalizada":
        print("No se pueden vender entradas de una pelicula finalizada.")
        return

    cantidad = ingresar_positivo(
        "Ingrese cantidad de entradas a vender: "
    )

    if cantidad > lst_stock[i]:
        print("No hay stock suficiente.")
        print("Stock disponible: ", lst_stock[i])
        return

    total = cantidad * lst_valores[i]

    print("Total a pagar: $", total)

    lst_stock[i] = lst_stock[i] - cantidad
    lst_entradas[i] = lst_entradas[i] + cantidad

    print("Venta registrada correctamente.")
