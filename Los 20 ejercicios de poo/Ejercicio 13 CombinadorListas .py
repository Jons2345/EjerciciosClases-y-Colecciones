# Clase CombinadorListas que: (1) tenga método intercalar(lista1, lista2) que retorne una lista alternando elementos de ambas; 
# (2) tenga método intercalar_multiples(*listas) que reutilice para varias listas.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea dos listas, o varias listas con *listas.
# Proceso: se empieza a recorrer por posición (0, 1, 2…) y en cada posición tomar 
# el elemento de cada lista, si esa lista todavía lo tiene.
# Salida: se ve una sola lista con los elementos alternados.


## Paso 2: Bosquejo
# lista1 = [1, 3]     lista2 = [2, 4]
# Posición 0: de lista1 → 1, de lista2 → 2
# Posición 1: de lista1 → 3, de lista2 → 4
# Resultado: 1, 2, 3, 4
# Si una lista es más corta, la salto cuando se le acaban los elementos.

## Paso 3: Descubrir el patrón

# El intercalar_multiples(*listas): es el método general. Calcula el largo de la lista más larga y recorre esas posiciones.

# El Doble bucle: el for i externo avanza por posición; el for lista interno pasa por cada lista y toma lista[i] solo si i < len(lista).

# El intercalar: no repite código, simplemente llama a intercalar_multiples(lista1, lista2). Esa es la reutilización.

# el max(..., default=0): evita un error si no se pasa ninguna lista.

# Los Conceptos aplicados: listas, bucles anidados, *args, len, expresión generadora, reutilización.


## Paso 4: Escribir el código
class CombinadorListas:
    def intercalar_multiples(self, *listas):
        resultado = []
        largo_maximo = max((len(l) for l in listas), default=0)

        for i in range(largo_maximo):
            for lista in listas:
                if i < len(lista):
                    resultado.append(lista[i])

        return resultado

    def intercalar(self, lista1, lista2):
        return self.intercalar_multiples(lista1, lista2)

            
combinador = CombinadorListas()
print(combinador.intercalar([1,3], [2,4]))

#### Paso 5: Prueba de escritorio

# i	     LISTA	        ¿i < len?	     RESULTADO
# —	    (inicio)	        —	           [ ]
# 0	     [1,3]	          0 < 2 ✓	       [1]
# 0	     [2,4]	          0 < 2 ✓	      [1,2]
# 1	     [1,3]	          1 < 2 ✓	      [1,2,3]
# 1	     [2,4]	          1 < 2 ✓	      [1,2,3,4]

