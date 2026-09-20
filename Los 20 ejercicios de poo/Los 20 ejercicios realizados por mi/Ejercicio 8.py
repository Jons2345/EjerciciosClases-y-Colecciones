# Crea una clase Biblioteca que:

# Tenga un método crear_seccion(nombre_seccion) que inicie una sección como una lista vacía dentro de un diccionario.
# Tenga un método agregar_libro(seccion, libro) que añada el libro a la sección indicada.
# Tenga un método seccion_mayor_libros() que retorne el nombre de la sección con más libros.

class Biblioteca:
    def __init__(self):
        self.secciones = {}

    def crear_seccion(self, nombre_seccion):
        if nombre_seccion in self.secciones:
            print(f"La sección '{nombre_seccion}' ya existe.")
        else:
            self.secciones[nombre_seccion] = []

    def agregar_libro(self, seccion, libro):
        if seccion in self.secciones:
            self.secciones[seccion].append(libro)
        else:
            print(f"La sección '{seccion}' no existe.")

    def seccion_mayor_libros(self):
        if not self.secciones:
            return None
        return max(self.secciones, key=lambda nombre: len(self.secciones[nombre]))

biblioteca = Biblioteca()

biblioteca.crear_seccion("Ciencia")
biblioteca.crear_seccion("Novela")

biblioteca.agregar_libro("Ciencia", "Cosmos")
biblioteca.agregar_libro("Novela", "Cien años de soledad")
biblioteca.agregar_libro("Poesía", "Veinte poemas")  

print(biblioteca.secciones)
print(biblioteca.seccion_mayor_libros())














