# Crea una clase Inventario que:
# 1) Tenga un método validar_precio(precio) que retorne True si el precio es mayor que 0 y menor o igual a 10000, y False en caso contrario.
# 2) Tenga un método cargar_precios(*args) que reciba múltiples precios, los valide, agregue solo los válidos a una lista interna y retorne esa lista.
# 3) Tenga un método total() que retorne la suma de los precios almacenados.


class Inventario:
    def __init__(self):
        self.lista = []
    
    def validar_precio(self, precio):
        return precio > 0 and precio <= 10000 
        
    def cargar_precios(self, *args):
        for precio in args:
            if self.validar_precio (precio):
                self.lista.append(precio)
        return self.lista
            
    
    def total(self):
        return sum(self.lista)

invent = Inventario()
print(invent.cargar_precios(5000, 30, 1000))
print(invent.total())













