# Clase CalculadorDistancia que: (1) tenga método distancia_euclidiana(p1, p2) que reciba dos tuplas (x,y) y calcule la distancia; 
# (2) tenga método punto_mas_cercano(referencia, *puntos) que retorne el punto más cercano a referencia; 
# (3) tenga un atributo lista para guardar todas las distancias calculadas.


## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crean dos tuplas (x, y); una referencia y varios puntos con *puntos.
# Proceso: se empieza  decidir la categoría con if/elif/else; agregar cada edad a la lista de su categoría; promediar con suma / cantidad.
# Salida: se ve  una categoría (texto); diccionario {categoría: [edades]}; el promedio (o None).


## Paso 2: Bosquejo
# Reglas: <12 niño · <18 adolescente · <60 adulto · resto mayor
#   5 → niño        15 → adolescente   30 → adulto
#   8 → niño        70 → mayor         45 → adulto
# Grupos: niño [5, 8] · adolescente [15] · adulto [30, 45] · mayor [70]
# Promedio adulto: (30 + 45) / 2 = 37.5

## Paso 3: Descubrir el patrón
# El clasificar_edad: una cadena if / elif / else ordenada de menor a mayor. Cada elif solo se evalúa si el anterior fue falso,
# por eso basta con el límite superior. Una edad negativa lanza ValueError.

# El agrupar_por_categoria(*edades): patrón de agrupar: si la categoría no es clave, se crea con lista vacía; luego se hace append.

# La edad_promedio_categoria: usa .get(categoria, []); si la lista está vacía retorna None (evita dividir entre cero).

# El Atributo grupos: guarda el último agrupamiento para que el promedio pueda consultarlo.

# La Conceptos aplicados: condicionales encadenados, diccionarios de listas, *args, sum/len, excepciones.


## Paso 4: Escribir el código
import math

class CalculadorDistancia:
    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.distancias.append(distancia)
        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        if not puntos:
            return None

        mas_cercano = puntos[0]
        menor_distancia = self.distancia_euclidiana(referencia, puntos[0])

        for punto in puntos[1:]:
            d = self.distancia_euclidiana(referencia, punto)
            if d < menor_distancia:
                menor_distancia = d
                mas_cercano = punto

        return mas_cercano


calc = CalculadorDistancia()

print(calc.distancia_euclidiana((0, 0), (3, 4)))               
print(calc.punto_mas_cercano((0, 0), (5, 5), (1, 1), (3, 4)))  
print(calc.distancias) 

# LÍNEA POR LÍNEA (FRAGMENTOS CLAVE)

# x1, y1 = p1
# Desempaqueta la tupla en sus dos coordenadas.

# math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
# Fórmula de la distancia euclidiana.

# self.distancias.append(distancia)
# Guarda cada distancia calculada en el historial.

# for punto in puntos[1:]:
# Recorre desde el segundo punto (el primero ya es el candidato).

# if d < menor_distancia:
# Si encuentra uno más cerca, actualiza distancia y punto.

#### Paso 5: Prueba de escritorio

# EDAD	              CATEGORÍA	               GRUPOS
# 5	                    niño	            {niño: [5]}
# 15	              adolescente	 {niño: [5], adolescente: [15]}
# 30	                 adulto	      {..., adulto: [30]}
# 8	                     niño	      {niño: [5, 8], ...}
# 70	                 mayor	      {..., mayor: [70]}
# 45	                 adulto	      {..., adulto: [30, 45], mayor: [70]}
# promedio('adulto')   	  —	          (30 + 45) / 2 = 37.5

