# Clase InversorSecuencia que: (1) tenga método invertir_lista(lista) que retorne la lista 
# invertida sin usar reversed() (usa manual con bucles); 
# (2) tenga método invertir_multiples(*listas) que reutilice el anterior para invertir 
# varias listas y retorne un diccionario {lista_original: lista_invertida}.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea una lista, o varias listas
# Proceso: se empieza a invertir el orden manualmente (sin reversed()), recorriendo con índices hacia atrás
# Salida: se ve el esatdo de lista invertida; diccionario {original: invertida} para varias listas
 
## Paso 2: Bosquejo
# Lista: [1, 2, 3, 4] → índices 0,1,2,3 → len=4
# Empiezo en índice 3 (len-1) y bajo hasta 0:
#   i=3 → tomo lista[3]=4 → invertida=[4]
#   i=2 → tomo lista[2]=3 → invertida=[4,3]
#   i=1 → tomo lista[1]=2 → invertida=[4,3,2]
#   i=0 → tomo lista[0]=1 → invertida=[4,3,2,1]
#   i=-1 → me detengo (range llega hasta -1 exclusivo)

## Paso 3: Descubrir el patrón

# El Método invertir_lista(lista): usa range(len(lista)-1, -1, -1) y un for que recorre índices de atrás 
# hacia adelante con paso -1, y va llenando una lista nueva.

# El Método invertir_multiples(*listas): recibe varias listas con *args, y reutiliza
# invertir_lista() por cada una, guardando el par en un diccionario. 
# la lista original se convierte a tuple() porque las listas no pueden ser llaves de diccionario.

# Los Conceptos aplicados: range() con paso negativo, indexación manual, *args, diccionarios con tuplas como llave, reutilización de métodos.

## Paso 4: Escribir el código
class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            resultado[tuple(lista)] = self.invertir_lista(lista)
        return resultado

secuencia = InversorSecuencia()
secuencia.invertir_lista([1, 2, 3, 4])

#### Paso 5: Prueba de escritorio

# i	    lista[i]	invertida
# 3	       4	     [4]
# 2	       3	     [4, 3]
# 1	       2	     [4, 3, 2]
# 0	       1	     [4, 3, 2, 1]