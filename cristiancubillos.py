def validar_codigo(codigo): return len(codigo.strip()) > 0
def validar_titulo(titulo): return len(titulo.strip()) > 0
def validar_genero(genero): return len(genero.strip()) > 0
def validar_duracion(duracion): return duracion > 0
def validar_clasificacion(clasificacion): return clasificacion in ["A", "B", "C"]
def validar_idioma(idioma): return len(idioma.strip()) > 0
def validar_precio(precio): return precio > 0
def validar_cupos(cupos): return cupos >= 0

def buscar_codigo(codigo, cartelera):
    return codigo.lower() in cartelera

def cupos_por_genero(genero, codigo, cartelera):
    input_genero = input("Ingrese el género de la película: ").lower()
    total = 0
    for pelicula, codigo in cartelera.items():
        if codigo.lower() == genero.lower() and codigo in cartelera:
            total = total + genero[codigo]['cupos']
    print(f"El total de cupos para el género es: {total}")

def actualizar_precio(codigo, nuevo_precio, cartelera):
    while True:
        codigo = input("Ingrese el código de la película a actualizar: ").lower()
        try:
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            if not validar_precio(nuevo_precio):
                print("Precio invalido. Debe ser un número positivo.")
            elif actualizar_precio(codigo, nuevo_precio, cartelera):
                print("Precio actualizado correctamente.")
            else:
                print("El codigo no existe.")
        except ValueError:
            print("Debe ingresar valores numericos.")
        if input("¿Desea actualizar otra película? (s/n): ").lower() != 's':
            break

def agregar_pelicula(genero, cartelera):
    codigo = input("Ingrese el código de la película: ").lower()
    titulo = input("Ingrese el título de la película: ").lower()
    genero = input("Ingrese el género de la película: ").lower()
    duracion = int(input("Ingrese la duración de la película (en minutos): "))
    clasificacion = input("Ingrese la clasificación de la película (A, B, C): ").upper()
    idioma = input("Ingrese el idioma de la película: ")
    try:
        precio = float(input("Ingrese el precio de la película: "))
        cupos = int(input("Ingrese la cantidad de cupos disponibles: "))
    except ValueError:
        print("Debe ingresar valores numericos.")
        return
    if not validar_codigo(codigo):
        print("Código inválido. Debe ser un valor no vacío.")
    elif buscar_codigo(codigo, cartelera):
        print("El código ya existe. No se puede agregar la película.")
    elif not validar_titulo(titulo):
        print("Título inválido.")
    elif not validar_genero(genero):
        print("Género inválido.")
    elif not validar_duracion(duracion):
        print("Duración inválida.")
    elif not validar_clasificacion(clasificacion):
        print("Clasificación inválida. Debe ser A, B o C.")
    elif not validar_idioma(idioma):
        print("Idioma inválido.")
    elif not validar_precio(precio):
        print("Precio inválido. Debe ser un número positivo.")
    elif not validar_cupos(cupos):
        print("Cupos inválidos.")
    else:
        agregar_pelicula(genero, cartelera, codigo, titulo, duracion, clasificacion, idioma, precio, cupos)
        print("Película agregada correctamente.")

def eliminar_pelicula(codigo, cartelera):
    codigo = input("Ingrese el código de la película a eliminar: ").lower()
    if elliminar_pelicula(codigo, cartelera):
        print("Película eliminada correctamente.")
    else:
        print("El código no existe. No se puede eliminar la película.")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por género")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")

def main():
    genero = {}
    codigo = {}
    cartelera = {}
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        if opcion == 1:
            cupos_por_genero(genero, codigo, cartelera)
        elif opcion == 2:
            print("estamos trabajando para usted")
        elif opcion == 3:
            actualizar_precio(codigo, 0, cartelera)
        elif opcion == 4:
            agregar_pelicula(codigo, cartelera)
        elif opcion == 5:
            eliminar_pelicula(codigo, cartelera)
        elif opcion == 6:
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()