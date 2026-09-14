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
temps.registrar_multiples(20, 25, 18, 30)
print(temps.promedio())