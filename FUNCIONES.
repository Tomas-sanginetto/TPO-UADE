# Materia: Pensamiento computacional, Algoritmia y Programacion
# Equipo: 08
# Integrantes: Bongiovanni, Chizzini, Marletto, Niederer, Sanginetto
# Docentes: Veronica Galati, Santiago Mendoza
# Descripcion: Sistema de gestion de peliculas CineVerse Complex
def opciones_menu():
    '''Mostrar el menu principal y sus opciones'''
    print("=" * 50)
    print("SISTEMA DE GESTIÓN: CINEVERSE COMPLEX")
    print("1. Registrar Pelicula")
    print("2. Eliminar Pelicula")
    print("3. Modificar Pelicula")
    print("4. Informe General")
    print("5. Salir")
    print("=" * 50)


def registrar_pelicula(lst_titulos, lst_generos, lst_duraciones, lst_salas, lst_entradas, lst_valores, lst_estados):
    '''Pedir y agregar cada uno de los campos de las peliculas nuevas en las listas existentes'''
    continuar = "S"
    while continuar.upper() == "S":
        titulo = validar_titulo("Ingrese la pelicula a registrar:")
        genero = ingresar_genero("Seleccione el genero:")
        duracion = ingresar_positivo("Ingrese la duracion en minutos: ")
        sala = ingresar_positivo("Ingrese el numero de sala: ")
        entradas = 0  # Pelicula nueva no tiene entradas YA vendidas
        valor = ingresar_valor_entrada("Ingrese el valor de la entrada: ")
        estado = ingresar_estado_registro("Seleccione el estado de la pelicula: ")  # Esa funcion para que no aparezca la opcion finalizada

        lst_titulos.append(titulo)
        lst_generos.append(genero)
        lst_duraciones.append(duracion)
        lst_salas.append(sala)
        lst_entradas.append(entradas)
        lst_valores.append(valor)
        lst_estados.append(estado)

        print("Pelicula registrada con exito!")
        continuar = input("Desea registrar otra pelicula? (S/N): ")
        while continuar.upper() != "S" and continuar.upper() != "N":
            print("Opcion invalida")
            continuar = input("Desea registrar otra pelicula? (S/N): ")


def ingresar_opcion(opcion):
    '''Valida que la opcion sea un digito dentro del rango numerico 1-5
    y retorna la variable teclado como entero'''
    while opcion.isdigit() == False or int(opcion) < 1 or int(opcion) > 5:
        print("La opcion seleccionada no es valida")
        opcion = input("Seleccione una opcion:")
    return int(opcion)


def ingresar_positivo(mensaje):
    '''Validar que el input sea un digito mayor a cero
    y retornar el entero de la variable teclado'''
    num = input(mensaje)
    while num.isdigit() == False or int(num) == 0:
        print("Error debe ser un numero positivo")
        num = input(mensaje)
    return int(num)


def ingresar_no_negativo(mensaje):
    '''Validar que el input sea un digito mayor o igual a cero
    y retornar el entero de la variable teclado'''
    num = input(mensaje)
    while num.isdigit() == False or int(num) < 0:
        print("Error, debe ser un número no negativo")
        num = input(mensaje)
    return int(num)


def ingresar_valor_entrada(mensaje):
    '''Validar que el precio sea mayor o igual a cero
    permitiendo numeros con decimales'''
    precio = float(input(mensaje))
    while precio < 0:
        print("Debe ser un valor positivo")
        precio = float(input(mensaje))
    return precio


def ingresar_titulo(mensaje, lst_titulos):
    '''Muestra la lista de peliculas disponibles, pide al usuario que seleccione una
    y retorna el indice de la pelicula seleccionada'''
    print(mensaje)
    for i in range(len(lst_titulos)):
        print(f"{i + 1} {lst_titulos[i]}")

    num = input("Ingrese el numero:")
    while num.isdigit() == False or int(num) < 1 or int(num) > len(lst_titulos):
        print("Valor invalido, intentelo nuevamente")
        num = input("Ingrese el numero:")
    return int(num) - 1  # Devuelve el indice, no titulo


def validar_titulo(mensaje):
    '''Pide al usuario ingresar el nombre de una nueva pelicula, validando que no quede vacio
    y retorna el nombre ingresado'''
    titulo = input(mensaje)
    while titulo == "":
        print("No se ingreso ningun titulo, intentelo denuevo")
        titulo = input(mensaje)
    return titulo


def ingresar_genero(mensaje):
    '''Muestra en pantalla cada genero de la lista, pide ingresar el genero
    y retorna el genero elegido de la lista'''
    print(mensaje)
    lst_generos = ["Acción", "Aventura", "Comedia", "Drama",
                    "Ciencia Ficción", "Terror", "Animación", "Documental"]
    for genero in range(len(lst_generos)):
        print(f"{genero + 1} {lst_generos[genero]}")

    num = input("Ingrese el genero deseado (Ingresar con numeros):")
    while num.isdigit() == False or int(num) < 1 or int(num) > len(lst_generos):
        print("Numero invalido, intentelo denuevo")
        num = input("Ingrese el genero deseado (Ingresar con numeros):")
    return lst_generos[int(num) - 1]


def ingresar_estado(mensaje):
    '''Muestra los posibles estados de la pelicula, pide ingresar el estado
    y retorna el estado ingresado'''
    print(mensaje)
    print("1. En cartelera")
    print("2. Proximo estreno")
    print("3. Funcion especial")
    print("4. Finalizada")
    opciones = ["En cartelera", "Proximo estreno", "Funcion especial", "Finalizada"]
    num = input("Ingrese el estado (segun el numero): ")
    while num.isdigit() == False or int(num) < 1 or int(num) > len(opciones):
        print("Numero invalido, intentelo nuevamente")
        num = input("Ingrese el estado (segun el numero): ")
    return opciones[int(num) - 1]


def ingresar_estado_registro(mensaje):  # Se usa cuando se registra una nueva peli (No puede ser estado = Finalizada)
    '''Muestra los posibles estados en el registro de una pelicula, pide ingresar el estado
    y retorna el estado ingresado'''
    print(mensaje)
    print("1. En cartelera")
    print("2. Proximo estreno")
    print("3. Funcion especial")
    opciones = ["En cartelera", "Proximo estreno", "Funcion especial"]
    num = input("Ingrese el estado (segun el numero): ")
    while num.isdigit() == False or int(num) < 1 or int(num) > len(opciones):
        print("Numero invalido, intentelo nuevamente")
        num = input("Ingrese el estado (segun el numero): ")
    return opciones[int(num) - 1]


# ===================================================================================================================


def informe_general(lst_titulos, lst_generos, lst_duraciones, lst_salas, lst_entradas, lst_valores, lst_estados):
    '''Valida que la lista de titulos no este vacia,luego ordena los titulos por cantidad de entradas
    o en caso de necesitarlo en orden alfabetico, por ultimo genera una matriz con cada uno de los atributos de cada titulo y la imprime'''
    if len(lst_titulos) == 0:
        print("No hay peliculas registradas")
        return  # No devuelve nada, solo termina la funcion
    # Return anticipado para que no ejecute todo el resto del codigo sin necesidad
    # METODO DE BURBUJEO
    n = len(lst_titulos)
    for i in range(n - 1):  # Cuenta las pasadas completas
        for j in range(n - 1 - i):  # Recorre comparando el elemento j con j+1
            # Dentro de la condicion logica se lleva a cabo un "Swapeo", es equivalente a usar un aux pero mas comprimido y en una sola linea
            if lst_entradas[j] < lst_entradas[j + 1] or (lst_entradas[j] == lst_entradas[j + 1] and lst_titulos[j] > lst_titulos[j + 1]):
                lst_titulos[j],   lst_titulos[j+1] = lst_titulos[j+1],   lst_titulos[j]
                lst_generos[j],   lst_generos[j+1] = lst_generos[j+1],   lst_generos[j]
                lst_duraciones[j], lst_duraciones[j+1] = lst_duraciones[j+1],lst_duraciones[j]
                lst_salas[j],     lst_salas[j+1] = lst_salas[j+1],     lst_salas[j]
                lst_entradas[j],  lst_entradas[j+1] = lst_entradas[j+1],  lst_entradas[j]
                lst_valores[j],   lst_valores[j+1] = lst_valores[j+1],   lst_valores[j]
                lst_estados[j],   lst_estados[j+1] = lst_estados[j+1],   lst_estados[j]
    print("=" * 50)
    print("     INFORME GENERAL - PELÍCULAS")
    print("=" * 50)
    matriz = []
    i = 0
    while i < len(lst_titulos):
        fila = [lst_titulos[i], lst_generos[i], lst_duraciones[i],
                lst_salas[i], lst_entradas[i], lst_valores[i], lst_estados[i]]
        matriz.append(fila)
        i += 1

    # imprimir desde la matriz
    i = 0
    while i < len(matriz):
        print(f"Título:            {matriz[i][0]}")
        print(f"Género:            {matriz[i][1]}")
        print(f"Duración:          {matriz[i][2]} minutos")
        print(f"Sala:              {matriz[i][3]}")
        print(f"Entradas vendidas: {matriz[i][4]}")
        print(f"Valor entrada:     ${matriz[i][5]}")
        print(f"Estado:            {matriz[i][6]}")
        print("-" * 50)
        i += 1

    input("Presione Enter para volver al menu principal")


# ===================================================================================================================


def eliminar_pelicula(lst_titulos, lst_generos, lst_duraciones, lst_salas, lst_entradas, lst_valores, lst_estados):
    '''Valida que haya minimo un titulo, valida que la pelicula haya sido finalizada
    pide una confirmacion y elimina cada uno de los datos de la pelicula eliminada'''
    if len(lst_titulos) == 0:
        print("No hay peliculas registradas.")
        return  # En caso de no existir peliculas registradas, no seguir con la ejecucion

    indice = ingresar_titulo("Seleccione la pelicula a eliminar:", lst_titulos)

    if lst_estados[indice] != "Finalizada":  # Borrar unicamente funciones finalizadas
        print("Solo se pueden eliminar peliculas con estado Finalizada.")
        return  # Si se cumple esa funcion cortar aca la funcion

    confirmacion = input(f"Esta seguro que desea eliminar '{lst_titulos[indice]}'? (S/N): ")
    while confirmacion.upper() != "S" and confirmacion.upper() != "N":
        print("Opcion invalida.")
        confirmacion = input("Esta seguro? (S/N): ")

    if confirmacion.upper() == "S":
        lst_titulos.pop(indice)
        lst_generos.pop(indice)
        lst_duraciones.pop(indice)
        lst_salas.pop(indice)
        lst_entradas.pop(indice)
        lst_valores.pop(indice)
        lst_estados.pop(indice)
        print("Pelicula eliminada con exito.")
    else:
        print("Eliminacion cancelada.")

# ===================================================================================================================


def opciones_modificar():
    '''Muestra el menu interactivo para modificar peliculas'''
    print("--- Que desea modificar? ---")
    print("1. Titulo")
    print("2. Genero")
    print("3. Duracion")
    print("4. Sala")
    print("5. Entradas vendidas")
    print("6. Valor entrada")
    print("7. Estado")
    print("8. Volver al menu principal")


def modificar_pelicula(lst_titulos, lst_generos, lst_duraciones, lst_salas, lst_entradas, lst_valores, lst_estados):
    '''Valida que la lista de titulos no este vacia, permite seleccionar una pelicula 
    y modificar sus atributos, repite hasta que el usuario decida volver'''
    if len(lst_titulos) == 0:
        print("No hay peliculas registradas.")
        return

    indice = ingresar_titulo("Seleccione la pelicula a modificar:", lst_titulos)
    # Cual pelicula modificar?

    opciones_modificar()
    opcion = input("Seleccione una opcion: ")
    while opcion.isdigit() == False or int(opcion) < 1 or int(opcion) > 8:
        print("Opcion invalida")
        opcion = input("Seleccione una opcion: ")
    opcion = int(opcion)  # Para que while no compare str con int (Error)
    # Que atributo modificar?

    while opcion != 8:
        if opcion == 1:
            lst_titulos[indice] = validar_titulo("Ingrese el nuevo titulo: ")
        elif opcion == 2:
            lst_generos[indice] = ingresar_genero("Ingrese el nuevo genero:")
        elif opcion == 3:
            lst_duraciones[indice] = ingresar_positivo("Ingrese la nueva duracion en minutos: ")
        elif opcion == 4:
            lst_salas[indice] = ingresar_positivo("Ingrese el nuevo numero de sala: ")
        elif opcion == 5:
            lst_entradas[indice] = ingresar_no_negativo("Ingrese las nuevas entradas vendidas: ")
        elif opcion == 6:
            lst_valores[indice] = ingresar_valor_entrada("Ingrese el nuevo valor de entrada: ")
        elif opcion == 7:
            lst_estados[indice] = ingresar_estado("Ingrese el nuevo estado:")

        print("Modificacion realizada con exito!")
        opciones_modificar()
        opcion = input("Seleccione una opcion: ")
        while opcion.isdigit() == False or int(opcion) < 1 or int(opcion) > 8:
            print("Opcion invalida")
            opcion = input("Seleccione una opcion: ")
        opcion = int(opcion)
