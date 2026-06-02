lista_generos = ["Acción", "Aventura", "Comedia", "Drama", "Ciencia Ficción", "Terror", "Animación", "Documental"]
for i in range(len(lista_generos)):
    print(i + 1, ":", lista_generos[i])
print("9 : Volver atras")

seleccion_genero = int(input("Introduzca el numero que coincida con su seleccion "))

if seleccion_genero == "1":
    print("Seleccionaste: Acción")
elif seleccion_genero == "2":
    print("Seleccionaste: Aventura")
elif seleccion_genero == "3":
    print("Seleccionaste: Comedia")
elif seleccion_genero == "4":
    print("Seleccionaste: Drama")
elif seleccion_genero == "5":
    print("Seleccionaste: Ciencia Ficción")
elif seleccion_genero == "6":
    print("Seleccionaste: Terror")
elif seleccion_genero == "7":
    print("Seleccionaste: Animación")
elif seleccion_genero == "8":
    print("Seleccionaste: Documental")
elif seleccion_genero == "9":
    print("Volviendo atrás...")
else:
    print("Error, Ingfrese un numero valido")