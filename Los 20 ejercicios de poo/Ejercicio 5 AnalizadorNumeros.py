# Clase AnalizadorNumeros que: (1) tenga método es_par(numero) que retorne True/False;
# (2) tenga método separar(*numeros) que retorne un diccionario {'pares': [...], 'impares': [...]} reutilizando es_par;
# (3) tenga método cantidad_pares_impares() que retorne una tupla (cant_pares, cant_impares).

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea un número (para es_par); varios números (para separar)
# Proceso: se empieza a clasificar cada número según el resto de dividir entre 2
# Salida: se ve el estado de True/False; diccionario {'pares':[...], 'impares':[...]}; tupla (cant_pares, cant_impares)

 
## Paso 2: Bosquejo
# Entran: 2,3,4,5,6,7,8
#   2 % 2 = 0 → par
#   3 % 2 = 1 → impar
#   4 % 2 = 0 → par
#   5 % 2 = 1 → impar
#   6 % 2 = 0 → par
#   7 % 2 = 1 → impar
#   8 % 2 = 0 → par
# pares = [2,4,6,8] (4 elementos)
# impares = [3,5,7] (3 elementos)

## Paso 3: Descubrir el patrón

# El Método es_par(numero): validador booleano con el operador módulo %.

# El Método separar(*numeros): recorre *args con un for, reutiliza es_par() dentro de un if/else para repartir cada
# número en dos listas, y guarda el resultado en self.resultado (estado interno).

# El Método cantidad_pares_impares(): no vuelve a recorrer nada, reutiliza len() sobre las listas ya guardadas en 
# self.resultado y las retorna como tupla (dato inmutable, ideal para un par fijo de valores).

# Los Conceptos aplicados: operador módulo, *args, diccionarios, tuplas, atributo de estado (self.resultado), reutilización de métodos.

## Paso 4: Escribir el código        
class AnalizadorNumeros:
    def __init__(self):
        self.resultado = {'pares': [], 'impares': []}
 
    def es_par(self, numero):
        return numero % 2 == 0
        
    def separar(self, *numeros):
        pares = []
        impares = []
        for numero in numeros:
            if self.es_par(numero):
                pares.append(numero)
            else:
                impares.append(numero)
         
        self.resultado = {'pares': pares, 'impares': impares}
        return self.resultado
 
    def cantidad_pares_impares(self):
        cant_par = len(self.resultado['pares'])
        cant_impar = len(self.resultado['impares'])
        return (cant_par, cant_impar) 
    
resul = AnalizadorNumeros()
print(resul.es_par(2))   
print(resul.separar(2,3,4,5,6,7,8)) 
print(resul.cantidad_pares_impares())


# Línea por línea (fragmentos clave)

# return numero % 2 == 0	            
# Operador módulo: si el resto de dividir entre 2 es 0, el número es par.

# if self.es_par(numero): pares.append(numero)               
# Reutilización: separar llama a es_par para decidir en qué lista guardar cada número.

# self.resultado = {'pares': pares, 'impares': impares}
# Guarda el resultado como atributo, para que otro método lo use sin recorrer todo de nuevo.
	
# return (cant_par, cant_impar)	       
# Retorna una tupla: un par de valores fijos e inmutables.


#### Paso 5: Prueba de escritorio

# Acción	                 self.resultado	                          Salida
# a = AnalizadorNumeros()	{'pares':[], 'impares':[]}	                 —
# es_par(2)	                 sin cambio	                               True
# separar(2,3,4,5,6,7,8)	{'pares':[2,4,6,8], 'impares':[3,5,7]}	  igual al diccionario
# cantidad_pares_impares()	 sin cambio	                                (4, 3)