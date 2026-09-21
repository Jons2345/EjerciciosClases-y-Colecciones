# Crea una clase RegistroVentas que:

# 1) Tenga un método registrar_venta(producto, cantidad) que guarde en un 
# diccionario el total de unidades vendidas de cada producto (si el producto ya existe, suma la cantidad; si no, lo crea).
# 2) Tenga un método producto_mas_vendido() que retorne el producto con más unidades vendidas (o None si no hay ventas).
# 3) Tenga un método unidades_vendidas(producto) que retorne cuántas unidades
# se vendieron de ese producto (0 si nunca se vendió).


class RegistroVentas:
    def __init__(self):
        self.ventas = {}

    def registrar_venta(self, producto, cantidad):
        if producto in self.ventas:
            self.ventas[producto] += cantidad
        else:
            self.ventas[producto] = cantidad

    def producto_mas_vendido(self):
        if not self.ventas:
            return None
        return max(self.ventas, key=self.ventas.get)

    def unidades_vendidas(self, producto):
        return self.ventas.get(producto, 0)


registro = RegistroVentas()

registro.registrar_venta("laptop", 2)
registro.registrar_venta("mouse", 10)
registro.registrar_venta("laptop", 3)

print(registro.unidades_vendidas("laptop"))    
print(registro.unidades_vendidas("mouse"))     
print(registro.unidades_vendidas("monitor"))    
print(registro.producto_mas_vendido())          

















