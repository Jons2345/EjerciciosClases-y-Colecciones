
# Clase AnalizadorPatrones que: (1) tenga método encontrar_palabras(texto, patron) que busque palabras que
# inicien con el patrón y retorne una lista; 
# (2) tenga método agrupar_por_longitud(texto) que retorne un diccionario {longitud: [palabras]};
# (3) tenga método palabras_unicas() usando un conjunto.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea un texto y un patrón (prefijo) de búsqueda.
# Proceso: se empieza a separar el texto en palabras en minúscula con una expresión regular; filtrar por prefijo;
# agrupar por len; quitar repetidas con set.
# Salida: lista de palabras que inician con el patrón; diccionario {longitud: [palabras]}; conjunto de palabras únicas.


## Paso 2: Bosquejo
# Texto en minúscula y sin puntos:
# la casa de la carretera casi cae la casa es grande
# Empiezan con "ca": casa, carretera, casi, cae, casa
# Por longitud:
#   2 letras: la, de, la, la, es
#   3 letras: cae
#   4 letras: casa, casi, casa
#   6 letras: grande
#   9 letras: carretera
# Únicas: quito los repetidos (la ×3, casa ×2).


## Paso 3: Descubrir el patrón

# El _extraer_palabras: método auxiliar que usa re.findall(r"\w+", texto.lower()) para obtener solo palabras (sin puntuación) 
# en minúscula. Los tres métodos lo reutilizan.

# El encontrar_palabras: patrón de filtro con p.startswith(patron) dentro de una lista por comprensión.

# El agrupar_por_longitud: patrón de agrupar con diccionario de listas, igual que en AgrupadorEdades, pero la clave es len(palabra).

# La palabras_unicas: set(self.palabras) elimina repetidas. Usa las palabras del último texto analizado, guardadas en self.palabras.

# Los Conceptos aplicados: expresiones regulares básicas, startswith, listas por comprensión, diccionarios de listas, conjuntos.


## Paso 4: Escribir el código
import re


class AnalizadorPatrones:
    def __init__(self):
        self.palabras = []

    def _extraer_palabras(self, texto):
        self.palabras = re.findall(r"\w+", texto.lower())
        return self.palabras

    def encontrar_palabras(self, texto, patron):
        palabras = self._extraer_palabras(texto)
        patron = patron.lower()
        return [p for p in palabras if p.startswith(patron)]

    def agrupar_por_longitud(self, texto):
        palabras = self._extraer_palabras(texto)
        grupos = {}
        for palabra in palabras:
            longitud = len(palabra)
            if longitud not in grupos:
                grupos[longitud] = []
            grupos[longitud].append(palabra)
        return grupos

    def palabras_unicas(self):
        return set(self.palabras)


analizador = AnalizadorPatrones()
texto = "La casa de la carretera casi cae. La casa es grande."

print(analizador.encontrar_palabras(texto, "ca"))

print(analizador.agrupar_por_longitud(texto))

print(analizador.palabras_unicas())


# LÍNEA POR LÍNEA (FRAGMENTOS CLAVE)

# re.findall(r"\w+", texto.lower())
# Pasa a minúscula y extrae solo secuencias de letras/números.

# p.startswith(patron)
# True si la palabra empieza con el patrón.

# [p for p in palabras if ...]
# Lista por comprensión: filtro en una sola línea.

# grupos[longitud].append(palabra)
# Agrega la palabra a la lista de su longitud.

# set(self.palabras)
# Convierte la lista en conjunto: sin repetidos.

#### Paso 5: Prueba de escritorio

# PALABRA	      longitud	        ¿empieza con 'ca'?	          GRUPOS
# la	             2	                  no	              {2: [la]}
# casa	             4	                  sí	              {2: [la], 4: [casa]}
# de	             2	                  no	              {2: [la, de], 4: [casa]}
# carretera	         9	                  sí	              {..., 9: [carretera]}
# casi	             4	                  sí	              {4: [casa, casi], ...}
# cae	             3	                  sí	              {..., 3: [cae]}
# grande	         6	                  no	              {..., 6: [grande]}