# Clase GestorTemperatura que: (1) tenga método registrar_temperatura(temp) que guarde en una lista; 
# (2) tenga método minima()`, `maxima()`, `promedio() que calculen estadísticas; 
# (3) tenga método registrar_multiples(*temps) que reutilice el registro para varias temperaturas.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea una o varias temperaturas (números)
# Proceso: se empieza a guardar cada temperatura registrada; calcular mínima, máxima y promedio
# Salida: se ve los valores mínimo, máximo y promedio (o None si no hay datos)

 
## Paso 2: Bosquejo
# Entran: 20, 30, 40
# temperaturas = [20, 30, 40]
# mínima = 20
# máxima = 40
# promedio = (20+30+40)/3 = 90/3 = 30.0

# Caso vacío: temperaturas = [] → min()/max() fallarían
#   → hay que verificar "if self.temperaturas" antes

## Paso 3: Descubrir el patrón

# El Método registrar_temperatura(temp): se aplica append() a la lista interna.

# El Métodos minima() / maxima() / promedio(): usan las funciones nativas min(), max(), sum()/len() sobre self.temperaturas, 
# con una guarda (if not self.temperaturas: return None) para evitar errores con la lista vacía.

# El Método registrar_multiples(*temps): recorre *args y reutiliza registrar_temperatura() 
# para cada valor, en vez de repetir la lógica de append.

# Los Conceptos aplicados: funciones nativas de agregación (min, max, sum, len), manejo de caso vacío, *args, reutilización de métodos.

## Paso 4: Escribir el código
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
        
temps = GestorTemperatura()
temps.registrar_multiples(20,30, 40)
print(temps.promedio())

#### Paso 5: Prueba de escritorio
# Acción	                       self.temperaturas	Salida
# t = GestorTemperatura()	        []	                  —
# registrar_multiples(20,30,40)  	[20, 30, 40]	      —
# minima()	                        sin cambio	          20
# maxima()	                        sin cambio	          40
# promedio()	                    sin cambio	         30.0