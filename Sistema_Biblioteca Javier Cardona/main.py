import os
from libro import Libro
from usuario import Usuario
from prestamo import Prestamo
from archivos import cargar_datos, guardar_datos
from datetime import datetime

DATA_DIR = "data"
LIBROS_PATH = os.path.join(DATA_DIR, "libros.json")
USUARIOS_PATH = os.path.join(DATA_DIR, "usuarios.json")
PRESTAMOS_PATH = os.path.join(DATA_DIR, "prestamos.json")

def registrar_libro():
    libros = cargar_datos(LIBROS_PATH)
    id_libro = input("ID del libro: ")
    if any(l["id_libro"] == id_libro for l in libros):
        print("❌ ID ya existe.")
        return
    titulo = input("Título: ")
    autor = input("Autor: ")
    anio = input("Año de publicación: ")
    categoria = input("Categoría: ")
    libro = Libro(id_libro, titulo, autor, anio, categoria)
    libros.append(libro.to_dict())
    guardar_datos(LIBROS_PATH, libros)
    print("✅ Libro registrado.")

def registrar_usuario():
    usuarios = cargar_datos(USUARIOS_PATH)
    id_usuario = input("ID del usuario: ")
    if any(u["id_usuario"] == id_usuario for u in usuarios):
        print("❌ ID ya existe.")
        return
    nombre = input("Nombre completo: ")
    carrera = input("Carrera: ")
    usuario = Usuario(id_usuario, nombre, carrera)
    usuarios.append(usuario.to_dict())
    guardar_datos(USUARIOS_PATH, usuarios)
    print("✅ Usuario registrado.")

def realizar_prestamo():
    libros = cargar_datos(LIBROS_PATH)
    usuarios = cargar_datos(USUARIOS_PATH)
    prestamos = cargar_datos(PRESTAMOS_PATH)

    id_libro = input("ID del libro: ")
    id_usuario = input("ID del usuario: ")

    libro = next((l for l in libros if l["id_libro"] == id_libro and l["disponible"]), None)
    if not libro:
        print("❌ Libro no disponible o no existe.")
        return
    if not any(u["id_usuario"] == id_usuario for u in usuarios):
        print("❌ Usuario no existe.")
        return

    libro["disponible"] = False
    fecha_prestamo = datetime.now().strftime("%Y-%m-%d")
    nuevo_prestamo = Prestamo(id_libro, id_usuario, fecha_prestamo)
    prestamos.append(nuevo_prestamo.to_dict())
    guardar_datos(LIBROS_PATH, libros)
    guardar_datos(PRESTAMOS_PATH, prestamos)
    print("✅ Préstamo realizado.")

def registrar_devolucion():
    libros = cargar_datos(LIBROS_PATH)
    prestamos = cargar_datos(PRESTAMOS_PATH)

    id_libro = input("ID del libro: ")
    for prestamo in prestamos:
        if prestamo["id_libro"] == id_libro and not prestamo["fecha_devolucion"]:
            prestamo["fecha_devolucion"] = datetime.now().strftime("%Y-%m-%d")
            for libro in libros:
                if libro["id_libro"] == id_libro:
                    libro["disponible"] = True
                    break
            guardar_datos(PRESTAMOS_PATH, prestamos)
            guardar_datos(LIBROS_PATH, libros)
            print("✅ Devolución registrada.")
            return
    print("❌ No se encontró préstamo activo para ese libro.")

def consultar_libros_disponibles():
    libros = cargar_datos(LIBROS_PATH)
    disponibles = [l for l in libros if l["disponible"]]
    for libro in disponibles:
        print(libro)

def consultar_todos_los_libros():
    libros = cargar_datos(LIBROS_PATH)
    if not libros:
        print("No hay libros registrados.")
        return
    for libro in libros:
        print(libro)

def menu():
    os.makedirs(DATA_DIR, exist_ok=True)
    while True:
        print("\n--- MENÚ BIBLIOTECA ---")
        print("1. Registrar libro")
        print("2. Registrar usuario")
        print("3. Realizar préstamo")
        print("4. Registrar devolución")
        print("5. Ver libros disponibles")
        print("6. Ver todos los libros")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_libro()
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            realizar_prestamo()
        elif opcion == "4":
            registrar_devolucion()
        elif opcion == "5":
            consultar_libros_disponibles()
        elif opcion == "6":
            consultar_todos_los_libros()
        elif opcion == "7":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    menu()
