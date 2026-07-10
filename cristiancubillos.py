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
    print(f"El total de cupos para el género {genero} es: {total}")

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
def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, precio, cupos, cartelera):
    if buscar_codigo(codigo, cartelera):
        return False
    genero[codigo.lower()] = [titulo, genero, duracion, clasificacion, idioma, precio, cupos]
    cartelera[codigo.lower()] = [titulo, genero, duracion, clasificacion, idioma, precio, cupos]
    return True
    


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
    cartelera = {}
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        if opcion == 1:
            cupos_por_genero(cartelera)
        elif opcion == 2:
            print("estamos trabajando para usted")
        elif opcion == 3:
            actualizar_precio(cartelera)
        elif opcion == 4:
            agregar_pelicula(cartelera)
        elif opcion == 5:
            print("estamos trabajando para usted")
        elif opcion == 6:
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()