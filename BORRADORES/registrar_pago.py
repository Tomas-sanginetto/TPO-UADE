def registrar_pago(total):
    '''Solicita la forma de pago y calcula el vuelto con la menor cantidad de billetes posibles'''

    opciones_pago = ["Efectivo", "Tarjeta de credito"]
    indice = seleccionar_opcion(opciones_pago, "Seleccione la forma de pago:")

    if indice == 1:  # Tarjeta de credito
        total_con_recargo = round(total * 1.10)
        print(f"Recargo del 10% aplicado. Total a pagar: ${total_con_recargo}")
        return True

    # Efectivo
    restante = total
    while restante > 0:
        entregado = ingresar_no_negativo(f"Importe a pagar: ${restante}. Ingrese el importe entregado (0 para cancelar): ")
        if entregado == 0:
            print("Pago cancelado.")
            return False
        restante = restante - entregado
        if restante > 0:
            print(f"Aun falta pagar: ${restante}")

    vuelto = -restante  # restante quedo en 0 o negativo; el vuelto es el valor absoluto

    if vuelto > 0:
        print(f"Vuelto: ${vuelto}")
        denominaciones = [10000, 2000, 1000, 500, 200, 100, 50, 20, 10]
        for billete in denominaciones:
            cantidad = vuelto // billete
            if cantidad > 0:
                print(f"{cantidad} billete(s)/moneda(s) de ${billete}")
                vuelto = vuelto % billete

    return True
