# Clase Inventario que: (1) tenga método agregar_stock(producto, cantidad) que guarde en un diccionario; 
# (2) tenga método restar_stock(producto, cantidad) que disminuya y retorne True si hay suficiente; 
# (3) tenga método productos_bajo_stock(minimo) que retorne una lista de productos con cantidad < minimo.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crean producto y cantidad para agregar o restar; un mínimo para consultar.
# Proceso: se empieza sumar a lo que ya hay (o crear); restar solo si existe y alcanza; filtrar los que tienen menos que el mínimo. 
# Salida: se ve el True/False al restar; lista de productos con bajo stock; el diccionario de stock.


## Paso 2: Bosquejo
#Empiezo vacío.
#  manzana +10 → 10     pera +3 → 3     manzana +5 → 15
#Restar 10 peras:   hay 3 < 10 → no se puede → False
#Restar 1 kiwi:     no existe → False
#Bajo stock (< 5): manzana 11 no, pera 3 sí → ['pera']

## Paso 3: Descubrir el patrón
# El agregar_stock: mismo patrón de acumulador que un contador: si existe, += cantidad; si no, se crea.

# La restar_stock: es un validador con retorno booleano. Comprueba producto in self.stock and 
# self.stock[producto] >= cantidad; solo entonces resta y retorna True. Si no, retorna False sin modificar nada.

# Los productos_bajo_stock: patrón de filtro con cantidad < minimo (estrictamente menor).

# El Orden del and: primero se verifica que exista, así no se produce un error al consultar un producto inexistente.

# Los Conceptos aplicados: diccionarios, operadores lógicos, retorno booleano, filtros, .items().


## Paso 4: Escribir el código
class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] += cantidad
        else:
            self.stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        resultado = []
        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                resultado.append(producto)
        return resultado

inv = Inventario()
inv.agregar_stock("manzana", 10)
inv.agregar_stock("pera", 3)
inv.agregar_stock("manzana", 5)       

print(inv.restar_stock("manzana", 4)) 
print(inv.restar_stock("pera", 10))    
print(inv.restar_stock("kiwi", 1))     

print(inv.stock)                      
print(inv.productos_bajo_stock(5))

# LÍNEA POR LÍNEA (FRAGMENTOS CLAVE)

# self.stock[producto] += cantidad
# Suma la cantidad al stock existente.

# producto in self.stock and ...
# Primero verifica que exista; el and corta si es falso.

# self.stock[producto] >= cantidad
# Verifica que haya suficiente para restar.

# return True / return False
# Informa si la operación se realizó o no.

# if cantidad < minimo:
# Selecciona productos con stock menor al mínimo.

#### Paso 5: Prueba de escritorio

# ACCIÓN	                        STOCK	            SALIDA
# agregar('manzana', 10)	     {manzana: 10}	          —
# agregar('pera', 3)	      {manzana: 10, pera: 3}	  —
# agregar('manzana', 5)	      {manzana: 15, pera: 3}	  —
# restar('manzana', 4)	      {manzana: 11, pera: 3}	 True
# restar('pera', 10)	      {manzana: 11, pera: 3}	 False
# restar('kiwi', 1)	          {manzana: 11, pera: 3}	 False
# productos_bajo_stock(5)	  {manzana: 11, pera: 3}	['pera']