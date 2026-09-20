# Crea una clase Inventario que:

# Tenga un método agregar_producto(nombre, cantidad) que guarde en una lista de tuplas (nombre, cantidad).
# Tenga un método productos_agotados() que retorne solo los productos cuya cantidad sea 0.
# Tenga un método eliminar_producto(nombre) que borre el producto de la lista.
# Tenga un método total_unidades() que retorne la suma de todas las cantidades. (este es nuevo)



class Inventario:
    def __init__(self):
        self.lista = []

    def agregar_producto(self, nombre, cantidad):
        producto = (nombre, cantidad)
        self.lista.append(producto)

    def productos_agotados(self):
        resultado = []
        for nombre, cantidad in self.lista:
            if cantidad == 0:
                resultado.append((nombre, cantidad))
        return resultado

    def eliminar_producto(self, nombre):
        for producto in self.lista:
            if producto[0] == nombre:
                self.lista.remove(producto)
                break

    def total_unidades(self):
        total = 0
        for nombre, cantidad in self.lista:
            total += cantidad
        return total


invt = Inventario()

invt.agregar_producto("Lapiz", 50)
invt.agregar_producto("Cuaderno", 0)
invt.agregar_producto("Borrador", 20)

print("Agotados:", invt.productos_agotados())
print("Total unidades:", invt.total_unidades())

invt.eliminar_producto("Cuaderno")
print("Después de eliminar:", invt.lista)


