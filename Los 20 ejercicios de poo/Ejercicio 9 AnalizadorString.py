# Clase AnalizadorString que: (1) tenga método solo_vocales(letra) que retorne True si es vocal;
# (2) tenga método contar_por_tipo(texto) que retorne un diccionario 
# {'vocales': cant, 'consonantes': cant, 'digitos': cant} reutilizando métodos; 
# (3) tenga atributo que guarde el texto más largo analizado.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea una letra (para solo_vocales); un texto completo (para contar_por_tipo)
# Proceso: se empieza a clasificar cada carácter en vocal, consonante o dígito; recordar el texto más largo analizado

# Salida: se ve el estado True/False; diccionario con los conteos; atributo con el texto más largo
 
## Paso 2: Bosquejo
# Texto: "Hola123"
#   H → letra, no vocal → consonante
#   o → letra, vocal → vocal
#   l → letra, no vocal → consonante
#   a → letra, vocal → vocal
#   1 → dígito
#   2 → dígito
#   3 → dígito
# vocales=2, consonantes=2, digitos=3

# "Hola123" tiene 7 caracteres, más que el texto_mas_largo
#   vacío ('') inicial → se actualiza a "Hola123"

## Paso 3: Descubrir el patrón

# El Método solo_vocales(letra): validador booleano que usa el operador in sobre el string 'aeiou', 
# normalizando con .lower() primero.

# El Método contar_por_tipo(texto): recorre cada carácter con un for y usa .isdigit(), .isalpha() y reutiliza solo_vocales() 
# para decidir en cuál contador (vocales, consonantes, digitos) sumar.

# El Atributo texto_mas_largo: se compara con len() al inicio de contar_por_tipo(), y se actualiza 
# si el nuevo texto es más largo, el estado persiste entre llamadas.

# Los Conceptos aplicados: métodos de string (isdigit, isalpha, lower, in), diccionarios como contador, atributos de estado, reutilización de métodos.

## Paso 4: Escribir el código
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

astr = AnalizadorString()
astr.contar_por_tipo("Hola123")

#### Paso 5: Prueba de escritorio

# Carácter	      Tipo	                    conteo
# H	             consonante	    {'vocales':0,'consonantes':1,'digitos':0}
# o	             vocal	        {'vocales':1,'consonantes':1,'digitos':0}
# l          	 consonante	    {'vocales':1,'consonantes':2,'digitos':0}
# a	             vocal	        {'vocales':2,'consonantes':2,'digitos':0}
# 1,2,3	         dígitos	    {'vocales':2,'consonantes':2,'digitos':3}