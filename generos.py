lista_generos = ["Acción", "Aventura", "Comedia", "Drama", "Ciencia Ficción",
                 "Terror", "Animación", "Documental"]
for i in range(len(lista_generos)):
    print(i + 1, ":", lista_generos[i])
    
print("9 : Volver atras")

seleccion_genero = int(input("Introduzca el numero que coincida con su seleccion "))

while seleccion_genero < 1 or seleccion_genero > len(lista_generos):
    print("Numero invalido, intentelo denuevo")
    seleccion_genero = int(input("Ingrese el genero deseado (Ingresar con numeros):"))

print("Opcion seleccionada:", lista_generos[seleccion_genero - 1])
