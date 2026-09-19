## Clase ContadorFrecuencia que: (1) tenga método agregar_elemento(elemento) que guarde en un diccionario contando repeticiones; 
# (2) tenga método elemento_mas_frecuente() que retorne el elemento con mayor frecuencia;
# (3) tenga método frecuencia_elemento(elemento) que retorne cuántas veces aparece.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea los lementos que se agregan uno por uno ("manzana", "banana"…); para consultar, un elemento.
# Proceso: se empieza a realizar las funciones, si el elemento ya es clave, sumar 1; si no, crearlo con 1. 
# Buscar la clave con el valor más alto.
# Salida: se ve el diccionario de frecuencias; el elemento más frecuente; cuántas veces aparece.

 
## Paso 2: Bosquejo
# Llegan: manzana, manzana, banana, naranja, manzana, banana
# Hago una tabla de conteo con palitos:
#   manzana  |||  = 3
#   banana   ||   = 2
#   naranja  |    = 1
# El mayor es manzana.
# ¿Y "kiwi"? No está en la tabla, entonces 0.


## Paso 3: Descubrir el patrón

# El agregar_elemento: es un contador con diccionario. La pregunta clave es if elemento in self.frecuencias:
# si existe se hace += 1, si no se crea con = 1.

# EL elemento_mas_frecuente: max(diccionario, key=diccionario.get) recorre las claves y compara por su valor. 
# Si el diccionario está vacío se retorna None para evitar un error.

# El frecuencia_elemento: .get(elemento, 0) retorna el valor o 0 si la clave no existe, sin necesidad de un if.

# El Atributo frecuencias: un diccionario vacío creado en __init__ que se comparte entre todos los métodos.

# Los Conceptos aplicados: diccionarios, condicionales, max con key, valor por defecto de .get.

## Paso 4: Escribir el código

class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}
    
    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1
        
    def elemento_mas_frecuente(self):
        if not self.frecuencias: 
            return None
        return max(self.frecuencias, key=self.frecuencias.get)
            
    def frecuencia_elemento(self,elemento):
        return self.frecuencias.get(elemento, 0)

contador = ContadorFrecuencia()
contador.agregar_elemento("manzana")
contador.agregar_elemento("manzana")
contador.agregar_elemento("banana")
contador.agregar_elemento("naranja")
contador.agregar_elemento("manzana")
contador.agregar_elemento("banana")

print(contador.frecuencias)

#### Paso 5: Prueba de escritorio

# ACCIÓN	                     FRECUENCIAS	                      SALIDA
# c = ContadorFrecuencia()	        {}	                                —
# agregar("manzana")	         {manzana: 1}	                        —
# agregar("manzana")	         {manzana: 2}	                        —
# agregar("banana")    	        {manzana: 2, banana: 1}	                —
# agregar("naranja")	        {manzana: 2, banana: 1, naranja: 1}	    —
# agregar("manzana")	        {manzana: 3, banana: 1, naranja: 1}	    —
# agregar("banana")	            {manzana: 3, banana: 2, naranja: 1}	    —
# elemento_mas_frecuente()	    (sin cambios)	                      manzana
# frecuencia_elemento("kiwi")	(sin cambios)	                         0