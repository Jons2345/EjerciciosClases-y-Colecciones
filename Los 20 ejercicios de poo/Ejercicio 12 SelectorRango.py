## Clase SelectorRango que: (1) tenga método crear_rango(inicio, fin) que retorne una tupla con números en ese rango; 
# (2) tenga método elementos_en_multiples_rangos(*rangos) que reciba múltiples tuplas (inicio,fin) 
# y retorne una lista combinada sin duplicados usando un conjunto.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea dos números (inicio, fin) para un rango; varias tuplas (inicio, fin) para combinar.
# Proceso: se empieza a generar cada rango, meter sus números en un conjunto (que elimina repetidos) y convertirlo a lista.
# Salida: se ve una tupla con el rango; una lista combinada sin duplicados.

 
## Paso 2: Bosquejo
# Rango (1,5) → 1, 2, 3, 4      (el 5 NO entra)
# Rango (2,8) → 2, 3, 4, 5, 6, 7  (el 8 NO entra)
# Los junto en una bolsa que no acepta repetidos:
#   {1,2,3,4} + {2,3,4,5,6,7} = {1,2,3,4,5,6,7}
# Los repetidos (2, 3, 4) quedan una sola vez.

## Paso 3: Descubrir el patrón

# El crear_rango: range(inicio, fin) genera los números y tuple(...) los convierte en tupla. Como range 
# excluye el final, fin no está incluido.

# El elementos_en_multiples_rangos(*rangos): *rangos recibe varias tuplas. Cada una se desempaqueta con for inicio, fin in rangos.

# El Reutilización: dentro del bucle se llama a self.crear_rango, y set.update() agrega todos sus números al conjunto.

# El Conjunto: un set no guarda duplicados, así que la lista final ya sale limpia.

# Los Conceptos aplicados: tuplas, conjuntos, *args, desempaquetado, reutilización de métodos.

## Paso 4: Escribir el código
class SelectorRango:
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin))        
    
    def elementos_en_multiples_rangos(self, *rangos):
        multiples_rangos = set()
        
        for inicio, fin in rangos: 
            numeros = self.crear_rango(inicio, fin)
            multiples_rangos.update(numeros)
        
        return list(multiples_rangos)

selector = SelectorRango()
print(selector.elementos_en_multiples_rangos((1, 5), (2, 8)))


# LÍNEA POR LÍNEA (FRAGMENTOS CLAVE)

# tuple(range(inicio, fin))
# Genera los números de inicio a fin-1 y los guarda en una tupla.

# def ...(self, *rangos):
# Captura cualquier cantidad de tuplas como una tupla de tuplas.

# for inicio, fin in rangos:
# Desempaqueta cada tupla (inicio, fin) en dos variables.

# multiples_rangos.update(numeros)
# Agrega todos los números al conjunto; los repetidos se ignoran.

# return list(multiples_rangos)
# Convierte el conjunto en lista para retornarlo.

#### Paso 5: Prueba de escritorio

# ACCIÓN	                                CONJUNTO	       SALIDA
# multiples_rangos = set()	                  { }	             —
# rangos = ((1,5), (2,8))	                  { }	             —
# (1,5) → crear_rango = (1,2,3,4)	        {1,2,3,4}	         —
# (2,8) → crear_rango = (2,3,4,5,6,7)	 {1,2,3,4,5,6,7}	     —
# return list(...)	                     {1,2,3,4,5,6,7}	[1,2,3,4,5,6,7]
