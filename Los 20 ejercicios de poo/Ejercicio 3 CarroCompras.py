# Clase CarroCompras que: (1) tenga método agregar_articulo(nombre, precio) que guarde en un diccionario {nombre: precio}; 
# (2) tenga método total_carrito() que retorne la suma de todos los precios; 
# (3) tenga método articulos_por_rango(precio_min, precio_max) que retorne una lista con artículos dentro del rango.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crean datos de  pares nombre/precio de artículos
# Proceso: se empieza a aguardar en un diccionario {nombre: precio}; sumar precios; filtrar por rango
# Salida: se ve el total del carrito; lista de nombres dentro de un rango de precio
 
## Paso 2: Bosquejo
# Diccionario: {"libro": 20, "lapiz": 5}
# Total = 20 + 5 = 25

# ¿"libro" (20) está en [1,10]? No, 20 > 10 → descartar
# ¿"lapiz" (5) está en [1,10]? Sí, 1 ≤ 5 ≤ 10 → incluir
# Resultado: ['lapiz']

## Paso 3: Descubrir el patrón
# El Método agregar_articulo(nombre, precio): asignación directa a diccionario, 
# self.articulos[nombre] = precio. Si el nombre ya existe, se sobreescribe el precio.

# El Método total_carrito(): se usa el sum() sobre .values() del diccionario.

# El Método articulos_por_rango(): la comprensión de lista que recorre .items() y filtra con una condición compuesta precio_min <= precio <= precio_max.

# Conceptos aplicados: diccionarios, comprensión de listas, operadores relacionales encadenados.

## Paso 4: Escribir el código
class CarroCompras:
    def __init__(self):
        self.articulos = {}
    
    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio
        
    def total_carrito(self):
        return sum(self.articulos.values())
    
    def articulos_por_rango(self, precio_min, precio_max):
        return [
            nombre
            for nombre, precio in self.articulos.items()
            if precio_min <= precio <= precio_max
        ]
        
artic = CarroCompras()
artic.agregar_articulo("libro", 20)
artic.agregar_articulo("lapiz", 5)
print(artic.total_carrito())
        
#### Paso 5: Prueba de escritorio

# Acción	                       self.articulos	            Salida
# c = CarroCompras()	                 {}	                      —
# agregar_articulo("libro", 20)	   {'libro': 20}	              —
# agregar_articulo("lapiz", 5)	   {'libro': 20, 'lapiz': 5}	  —
# total_carrito()	                sin cambio	                  25
# articulos_por_rango(1, 10)	    sin cambio	                ['lapiz']