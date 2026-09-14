class GestorTemperatura:
	def __init__(self):
		self.temperaturas = []

	def registrar_temperatura(self, temp):
		self.temperaturas.append(temp)

	def minima(self):
		return min(self.temperaturas) if self.temperaturas else None

	def maxima(self):
		return max(self.temperaturas) if self.temperaturas else None

	def promedio(self):
		if not self.temperaturas:
			return None
		return sum(self.temperaturas) / len(self.temperaturas)

	def registrar_multiples(self, *temps):
		for temp in temps:
			self.registrar_temperatura(temp)


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


class AnalizadorString:
	def __init__(self):
		self.texto_mas_largo = ''

	def solo_vocales(self, letra):
		return letra.lower() in 'aeiou'

	def contar_por_tipo(self, texto):
		if len(texto) > len(self.texto_mas_largo):
			self.texto_mas_largo = texto

		conteo = {'vocales': 0, 'consonantes': 0, 'digitos': 0}
		for caracter in texto:
			if caracter.isdigit():
				conteo['digitos'] += 1
			elif caracter.isalpha():
				if self.solo_vocales(caracter):
					conteo['vocales'] += 1
				else:
					conteo['consonantes'] += 1
		return conteo


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
