# Clase GestorPersonas que: (1) tenga método agregar_persona(nombre, edad) que guarde en un diccionario;
# (2) tenga método personas_mayores(edad_minima) que retorne una lista de nombres cuya edad sea ≥;
# (3) tenga método edad_promedio() que retorne el promedio de edades.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea los valores pares nombre/edad de personas
# Proceso: se empieza a guardar en un diccionario {nombre: edad}; filtrar por edad mínima; calcular promedio
# Salida: se ve la lista de nombres que cumplen la edad mínima; promedio de edades


## Paso 2: Bosquejo
# Diccionario: {"Ana": 30, "Bob": 17}
# ¿Ana (30) ≥ 18? Sí → incluir
# ¿Bob (17) ≥ 18? No → descartar
# personas_mayores(18) = ["Ana"]

# promedio = (30 + 17) / 2 = 47/2 = 23.5

## Paso 3: Descubrir el patrón

# El Método agregar_persona(nombre, edad): asignación directa a diccionario self.personas[nombre] = edad, igual que en CarroCompras
# el mismo patrón "guardar en diccionario" se repite en varios ejercicios.

# El Método personas_mayores(edad_minima): comprensión de lista que recorre .items() y filtra con edad >= edad_minima.

# El Método edad_promedio(): sum()/len() sobre .values(), con guarda para diccionario vacío.

# Conceptos aplicados: diccionarios, comprensión de listas, operadores relacionales, manejo de caso vacío.

## Paso 4: Escribir el código
class GestorPersonas:
	def __init__(self):
		self.personas = {}

	def agregar_persona(self, nombre, edad):
		self.personas[nombre] = edad

	def personas_mayores(self, edad_minima):
		return [
			nombre
			for nombre, edad in self.personas.items()
			if edad >= edad_minima
		]

	def edad_promedio(self):
		if not self.personas:
			return None
		return sum(self.personas.values()) / len(self.personas)

gp = GestorPersonas()
gp.agregar_persona("Ana", 30)
gp.agregar_persona("Bob", 17)
print(gp.personas_mayores(18))

#### Paso 5: Prueba de escritorio
#      Acción	                self.notas	        Salida
# c = Calificador()	               []	              —
# cargar_notas(80, 50, 60)	   [80, 50, 60]	      [80, 50, 60]
# promedio()	               [80, 50, 60]	         63.33