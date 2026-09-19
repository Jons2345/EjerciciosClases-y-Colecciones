# Clase DivisorFinder que: (1) tenga método encontrar_divisores(numero) que retorne
# una tupla con todos los divisores; 
# (2) tenga método es_perfecto(numero) que retorne True si la suma 
# de sus divisores (excepto él mismo) es igual a él;
# (3) tenga método encontrar_multiples_divisores(*numeros) 
# que retorne un diccionario {número: tupla_divisores}.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea un número, o varios números con *numeros.
# Proceso: se empieza a probar todos los i de 1 a numero y quedarse con los que dan residuo 0; 
# sumar los divisores sin el propio número y comparar.
# Salida: se ve la tupla de divisores; True/False; diccionario {número: tupla_divisores}.


## Paso 2: Bosquejo
# Divisores de 12: pruebo del 1 al 12
#   12 % 1 = 0 ✓   12 % 2 = 0 ✓   12 % 3 = 0 ✓   12 % 4 = 0 ✓
#   12 % 5 = 2 ✗   12 % 6 = 0 ✓   ... 12 % 12 = 0 ✓
#   → (1, 2, 3, 4, 6, 12)
# ¿6 es perfecto? Divisores 1+2+3+6 = 12; sin el 6 → 6. ¿6 == 6? Sí.
# ¿12 es perfecto? 1+2+3+4+6+12 = 28; sin el 12 → 16. ¿16 == 12? No.

## Paso 3: Descubrir el patrón

# El encontrar_divisores: patrón de filtro con módulo: if numero % i == 0 significa que i divide exactamente. 
# El rango llega a numero + 1 para incluir al propio número.

# El es_perfecto: reutiliza encontrar_divisores. Como la lista incluye al número, se calcula sum(divisores)
# numero y se compara con el número.

# El encontrar_multiples_divisores(*numeros): recorre los números y guarda en un diccionario resultado[n] = self.encontrar_divisores(n).

# La Tuplas: se convierte la lista a tupla al final porque el resultado no debe modificarse.

# Los Conceptos aplicados: operador %, bucles for, tuplas, sum, *args, diccionarios, reutilización.

## Paso 4: Escribir el código
class DivisorFinder: 
    
    def encontrar_divisores(self, numero):
        divisor = []
        
        for i in range (1, numero + 1):
            if numero % i == 0:
                divisor.append(i)
                
        return tuple(divisor)
    
    def  es_perfecto(self, numero):
        divisor = self.encontrar_divisores(numero)
        suma = sum(divisor) - numero
        return suma == numero
    
    
    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for n in numeros:
            resultado[n] = self.encontrar_divisores(n)
        return resultado

f = DivisorFinder()
print(f.encontrar_divisores(12))
print(f.es_perfecto(6))
print(f.es_perfecto(12))
print(f.encontrar_multiples_divisores(6, 12, 15))


#### Paso 5: Prueba de escritorio

# ACCIÓN	                      DIVISORES	      SUMA − NÚMERO	         SALIDA
# es_perfecto(6)	             (1,2,3,6)	       12 − 6 = 6	      6 == 6 → True
# es_perfecto(12)	           (1,2,3,4,6,12)	   28 − 12 = 16      16 == 12 → False
# multiples(6, 12, 15) · n=6	 (1,2,3,6)	          —	             {6: (1,2,3,6)}
# n=12	                       (1,2,3,4,6,12)	      —	            {..., 12: (1,2,3,4,6,12)}
# n=15	                         (1,3,5,15)	          —	            {..., 15: (1,3,5,15)}