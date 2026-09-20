# Crea una clase Inventario que:

# 1) agregar_producto(nombre): agregue el producto a un conjunto (para evitar duplicados) y a una lista (para conservar el orden en que llegaron). Si el producto ya existe, no debe hacer nada.
# 2) contar_productos(): retorne cuántos productos únicos hay.
# 3) agregar_varios(*args): reciba cualquier cantidad de productos y reutilice agregar_producto para cada uno.
# 4) hay_producto(nombre) (nuevo): retorne True si el producto está en el inventario y False si no.


class Inventario:
    def __init__(self):
        self.product = set()
        self.lista = []
    
    def agregar_producto(self,nombre):
        if nombre not in self.product:
            self.product.add(nombre)
            self.lista.append(nombre)
            
    def contar_productos(self):
        return len(self.product)      
    
    def agregar_varios(self,*args):
        for product in args:
            self.agregar_producto(product)
            
    def  hay_producto(self, nombre):
        return nombre in self.product
            
invent = Inventario()
invent.agregar_varios("manzana", "pera", "manzana")
print(invent.contar_productos())
print(invent.hay_producto("queso"))
print(invent.lista)
