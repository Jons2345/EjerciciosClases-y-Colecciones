# Crea una clase Inventario que:

# 1) Tenga un método agregar(producto, cantidad) que guarde el producto en un diccionario. 
# Si el producto ya existe, debe sumar la cantidad a la que ya había (no sobrescribirla).
# 2) Tenga un método productos_agotados() que retorne una lista con los productos cuya cantidad sea 0.
# 3) Tenga un método producto_mas_stock() que retorne el nombre y la cantidad del producto con mayor stock.


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def productos_agotados(self):
        agotados = []
        for producto, cantidad in self.productos.items():
            if cantidad == 0:
                agotados.append(producto)
        return agotados

    def producto_mas_stock(self):
        if not self.productos:
            return None
        nombre = max(self.productos, key=self.productos.get)
        return nombre, self.productos[nombre]

inv = Inventario()
inv.agregar("Manzanas", 50)
inv.agregar("Peras", 0)
inv.agregar("Naranjas", 30)
inv.agregar("Manzanas", 10)

print(inv.productos_agotados())    
print(inv.producto_mas_stock())   

print(inv.retirar("Naranjas", 10)) 
print(inv.retirar("Naranjas", 50))
print(inv.retirar("Uvas", 5))      