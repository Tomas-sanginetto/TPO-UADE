# Materia: Pensamiento computacional, Algoritmia y Programacion
# Equipo: 08
# Integrantes: Bongiovanni, Chizzini, Marletto, Niederer, Sanginetto
# Docentes: Veronica Galati, Santiago Mendoza
# Descripcion: Sistema de gestion de peliculas CineVerse Complex
from funciones import *


def main():
    '''Inicia el programa llamando a cada una de las funciones
    permitiendo utilizar sus instrucciones y controlar el flujo del programa'''
    lst_titulos = []
    lst_generos = []
    lst_duraciones = []
    lst_salas = []
    lst_entradas = []
    lst_valores = []
    lst_estados = []

    opciones_menu()
    n = input("Seleccione una opcion: ")
    while n.isdigit() == False:  # Ingresar_opcion tiene dentro la condicion de que sea n >= 1 y n <= 5
        print("Ingrese un numero, intentelo nuevamente")
        n = input("Seleccione una opcion: ")
    n = ingresar_opcion(n)
    while n != 5:

        if n == 1:
            registrar_pelicula(lst_titulos, lst_generos, lst_duraciones, lst_salas, lst_entradas, lst_valores, lst_estados)  # Registrar
        elif n == 2:
            eliminar_pelicula(lst_titulos, lst_generos, lst_duraciones, lst_salas, lst_entradas, lst_valores, lst_estados)  # Eliminar
        elif n == 3:
            modificar_pelicula(lst_titulos, lst_generos, lst_duraciones, lst_salas, lst_entradas, lst_valores, lst_estados)  # Modificar
        elif n == 4:
            informe_general(lst_titulos, lst_generos, lst_duraciones, lst_salas, lst_entradas, lst_valores, lst_estados)  # Informe General

        opciones_menu()
        n = input("Seleccione una opcion:")
        while n.isdigit() == False:
            print("Ingrese un numero, intentelo nuevamente")
            n = input("Seleccione una opcion: ")
        n = ingresar_opcion(n)
    print("Gracias por usar CineVerse Complex")



main()
