# Clase Tareas que: (1) tenga método agregar_tarea(descripcion, prioridad) que guarde en una lista de tuplas (descripción, prioridad); 
# (2) tenga método tareas_prioritarias() que retorne solo las de prioridad alta;
# (3) tenga método eliminar_completada(descripcion) que borre la tarea de la lista.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea la descripción y prioridad de una tarea; descripción a eliminar
# Proceso: se empieza a guardar tareas como tuplas (descripción, prioridad); se filtra las de prioridad alta; se quita una tarea por descripción
# Salida: se ve la lista de tareas prioritarias y se ve la lista de tareas actualizada sin la eliminada

 
## Paso 2: Bosquejo
# tareas = [("Estudiar","alta"), ("Leer","baja")]

# ¿("Estudiar","alta")[1] == "alta"? Sí → incluir
# ¿("Leer","baja")[1] == "alta"? No → descartar
# tareas_prioritarias() = [("Estudiar","alta")]

# eliminar_completada("Leer"):
#   conservo solo las tareas cuya descripción != "Leer"
#   tareas = [("Estudiar","alta")]

## Paso 3: Descubrir el patrón

# El Método agregar_tarea(descripcion, prioridad): guarda una tupla la descripcion y prioridad  en una lista 
# la tupla agrupa dos datos relacionados que no deben modificarse por separado.

# El Método tareas_prioritarias(): comprensión de lista que accede al segundo elemento de cada tupla (tarea[1]) y compara con .lower() == 'alta'.

# El Método eliminar_completada(descripcion): reconstruye self.tareas con una comprensión de lista que excluye la tupla 
# cuyo primer elemento (tarea[0]) coincide y un patrón de "filtrar lo que NO quiero" en vez de borrar en el sitio.

# Los Conceptos aplicados: tuplas, listas de tuplas, comprensión de listas, acceso por índice a tuplas.

## Paso 4: Escribir el código
class Tareas:
	def __init__(self):
		self.tareas = []

	def agregar_tarea(self, descripcion, prioridad):
		self.tareas.append((descripcion, prioridad))

	def tareas_prioritarias(self):
		return [
			tarea for tarea in self.tareas
			if tarea[1].lower() == 'alta'
		]

	def eliminar_completada(self, descripcion):
		self.tareas = [
			tarea for tarea in self.tareas
			if tarea[0] != descripcion
		]

t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
t.tareas_prioritarias()

# Línea por línea (fragmentos clave)

# self.tareas.append((descripcion, prioridad))	   
# Guarda una tupla con dos datos relacionados dentro de la lista de tareas.

# if tarea[1].lower() == 'alta'	
# Accede al segundo elemento de la tupla (la prioridad) para filtrar.

# if tarea[0] != descripcion	
# Accede al primer elemento (la descripción) y reconstruye la lista excluyendo la tarea que coincide.


#### Paso 5: Prueba de escritorio
# Acción	                              self.tareas	          Salida
# t = Tareas()	                               []	                —
# agregar_tarea("Estudiar","alta")	  [('Estudiar','alta')]  	    —
# agregar_tarea("Leer","baja")	      [('Estudiar','alta'),         —
#                                     ('Leer','baja')] 
# tareas_prioritarias()	                 sin cambio	          [('Estudiar','alta')]
# eliminar_completada("Leer")	      [('Estudiar','alta')]	        —