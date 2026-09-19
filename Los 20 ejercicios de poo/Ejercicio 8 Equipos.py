# Clase Equipos que: (1) tenga método crear_equipo(nombre_equipo) que inicie un equipo como una lista vacía en un diccionario; 
# (2) tenga método agregar_jugador(equipo, jugador) que añada el jugador al equipo;
# (3) tenga método equipo_mayor_integrantes() que retorne el nombre del equipo con más jugadores.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea operaciones sobre la temperatura  celsius, fahrenheit o kelvin
# Proceso: se empieza a encapsular celsius, exponer las 3 escalas con property y recalcular al vuelo
# Salida: se ve el estado de la temperatura en las 3 escalas
 
## Paso 2: Bosquejo
# crear_equipo("A") → equipos = {"A": []}
# agregar_jugador("A","Juan") → equipos = {"A": ["Juan"]}
# agregar_jugador("A","Pedro") → equipos = {"A": ["Juan","Pedro"]}

# Si hubiera "B": [] (vacío) y "A": [Juan, Pedro]
#   len("A")=2 > len("B")=0 → gana "A"
# equipo_mayor_integrantes() = "A"

## Paso 3: Descubrir el patrón

# El Método crear_equipo(nombre_equipo): inicializa una lista vacía como valor dentro de un diccionario  
# diccionario de listas, una estructura anidada.

# El Método agregar_jugador(equipo, jugador): accede a la lista dentro del diccionario y hace append() sobre ella.

# El Método equipo_mayor_integrantes(): usa max() con el parámetro key= y una función lambda para comparar por len() de cada lista 
# se reutiliza la estructura sin necesidad de un for explícito.

# Conceptos aplicados: diccionarios de listas (estructuras anidadas), max() con key, funciones lambda.

## Paso 4: Escribir el código

class Equipos:
	def __init__(self):
		self.equipos = {}

	def crear_equipo(self, nombre_equipo):
		self.equipos[nombre_equipo] = []

	def agregar_jugador(self, equipo, jugador):
		self.equipos[equipo].append(jugador)

	def equipo_mayor_integrantes(self):
		if not self.equipos:
			return None
		return max(self.equipos, key=lambda equipo: len(self.equipos[equipo]))

eq = Equipos()
eq.crear_equipo("A")
eq.agregar_jugador("A","Juan")
eq.agregar_jugador("A","Pedro")

#### Paso 5: Prueba de escritorio

# Acción	                      self.equipos	            Salida
# eq = Equipos()	                  {}	                  —
# crear_equipo("A")     	      {'A': []}	                  —
# agregar_jugador("A","Juan")	  {'A': ['Juan']}	          —
# agregar_jugador("A","Pedro")	  {'A': ['Juan','Pedro']}	  —
# equipo_mayor_integrantes()	  sin cambio	             "A"
