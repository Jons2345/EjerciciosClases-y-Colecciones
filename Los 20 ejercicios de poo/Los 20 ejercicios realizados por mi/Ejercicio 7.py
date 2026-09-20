# Crea una clase GestorProductos que:

# Tenga un método agregar_producto(nombre, precio) que guarde el producto en un diccionario (nombre → precio).
# Tenga un método productos_caros(precio_minimo) que retorne una lista de nombres de los productos cuyo precio sea ≥ precio_minimo.
# Tenga un método precio_promedio() que retorne el promedio de los precios.

class GestorProductos:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, precio):
        self.productos[nombre] = precio

    def productos_caros(self, precio_minimo):
        resultado = []
        for nombre, precio in self.productos.items():
            if precio >= precio_minimo:
                resultado.append(nombre)
        return resultado

    def precio_promedio(self):
        if len(self.productos) == 0:
            return 0
        return sum(self.productos.values()) / len(self.productos)


gestor = GestorProductos()
gestor.agregar_producto("Mouse", 20)
gestor.agregar_producto("Teclado", 45)
gestor.agregar_producto("Monitor", 250)

print(gestor.productos_caros(100))    
print(gestor.precio_promedio())       
print(gestor.producto_mas_barato())  