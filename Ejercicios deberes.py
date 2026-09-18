
# Clase InversorSecuencia que: (1) tenga método invertir_lista(lista) que retorne la lista 
# invertida sin usar reversed() (usa manual con bucles); 
# (2) tenga método invertir_multiples(*listas) que reutilice el anterior para invertir 
# varias listas y retorne un diccionario {lista_original: lista_invertida}.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea operaciones sobre la temperatura  celsius, fahrenheit o kelvin
# Proceso: se empieza a encapsular celsius, exponer las 3 escalas con property y recalcular al vuelo
# Salida: se ve el estado de la temperatura en las 3 escalas
 
## Paso 2: Bosquejo


## Paso 3: Descubrir el patrón

# Solo existe un atributo real: _celsius ya que las propiedades fahrenheit y kelvin no guardan su propio valor ademas,
# cada una tiene un getter que calcula su valor a partir de _celsius, y un setter que convierte el valor recibido y lo guarda en _celsius.

# Mas importante, sin importar cuál de las tres propiedades se les asigne, siempre se termina actualizando a la misma fuente de verdad. 
# Y como los getters recalculan cada vez que se leen, las tres escalas siempre están sincronizadas y
# nunca puede haber un valor de Fahrenheit que no corresponda al Celsius actual.

# Al tener setter en las tres que son celsius, fahrenheit, kelvin, la clase permite escribir por cualquier puerta lado
# pero siempre llevan al mismo lugar (_celsius).

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
#      Acción	                self.notas	        Salida
# c = Calificador()	               []	              —
# cargar_notas(80, 50, 60)	   [80, 50, 60]	      [80, 50, 60]
# promedio()	               [80, 50, 60]	         63.33


# Clase AnalizadorNumeros que: (1) tenga método es_par(numero) que retorne True/False;
# (2) tenga método separar(*numeros) que retorne un diccionario {'pares': [...], 'impares': [...]} reutilizando es_par;
# (3) tenga método cantidad_pares_impares() que retorne una tupla (cant_pares, cant_impares).

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea operaciones sobre la temperatura  celsius, fahrenheit o kelvin
# Proceso: se empieza a encapsular celsius, exponer las 3 escalas con property y recalcular al vuelo
# Salida: se ve el estado de la temperatura en las 3 escalas
 
## Paso 2: Bosquejo


## Paso 3: Descubrir el patrón

# Solo existe un atributo real: _celsius ya que las propiedades fahrenheit y kelvin no guardan su propio valor ademas,
# cada una tiene un getter que calcula su valor a partir de _celsius, y un setter que convierte el valor recibido y lo guarda en _celsius.

# Mas importante, sin importar cuál de las tres propiedades se les asigne, siempre se termina actualizando a la misma fuente de verdad. 
# Y como los getters recalculan cada vez que se leen, las tres escalas siempre están sincronizadas y
# nunca puede haber un valor de Fahrenheit que no corresponda al Celsius actual.

# Al tener setter en las tres que son celsius, fahrenheit, kelvin, la clase permite escribir por cualquier puerta lado
# pero siempre llevan al mismo lugar (_celsius).

## Paso 4: Escribir el código        
class AnalizadorNumeros:
    def __init__(self):
        self.resultado = {'pares': [], 'impares': []}
 
    def es_par(self, numero):
        return numero % 2 == 0
        
    def separar(self, *numeros):
        pares = []
        impares = []
        for numero in numeros:
            if self.es_par(numero):
                pares.append(numero)
            else:
                impares.append(numero)
         
        self.resultado = {'pares': pares, 'impares': impares}
        return self.resultado
 
    def cantidad_pares_impares(self):
        cant_par = len(self.resultado['pares'])
        cant_impar = len(self.resultado['impares'])
        return (cant_par, cant_impar) 
    
resul = AnalizadorNumeros()
print(resul.es_par(2))   
print(resul.separar(2,3,4,5,6,7,8)) 
print(resul.cantidad_pares_impares())

#### Paso 5: Prueba de escritorio
#      Acción	                self.notas	        Salida
# c = Calificador()	               []	              —
# cargar_notas(80, 50, 60)	   [80, 50, 60]	      [80, 50, 60]
# promedio()	               [80, 50, 60]	         63.33


# Clase GestorTemperatura que: (1) tenga método registrar_temperatura(temp) que guarde en una lista; 
# (2) tenga método minima()`, `maxima()`, `promedio() que calculen estadísticas; 
# (3) tenga método registrar_multiples(*temps) que reutilice el registro para varias temperaturas.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea operaciones sobre la temperatura  celsius, fahrenheit o kelvin
# Proceso: se empieza a encapsular celsius, exponer las 3 escalas con property y recalcular al vuelo
# Salida: se ve el estado de la temperatura en las 3 escalas
 
## Paso 2: Bosquejo


## Paso 3: Descubrir el patrón

# Solo existe un atributo real: _celsius ya que las propiedades fahrenheit y kelvin no guardan su propio valor ademas,
# cada una tiene un getter que calcula su valor a partir de _celsius, y un setter que convierte el valor recibido y lo guarda en _celsius.

# Mas importante, sin importar cuál de las tres propiedades se les asigne, siempre se termina actualizando a la misma fuente de verdad. 
# Y como los getters recalculan cada vez que se leen, las tres escalas siempre están sincronizadas y
# nunca puede haber un valor de Fahrenheit que no corresponda al Celsius actual.

# Al tener setter en las tres que son celsius, fahrenheit, kelvin, la clase permite escribir por cualquier puerta lado
# pero siempre llevan al mismo lugar (_celsius).

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
#      Acción	                self.notas	        Salida
# c = Calificador()	               []	              —
# cargar_notas(80, 50, 60)	   [80, 50, 60]	      [80, 50, 60]
# promedio()	               [80, 50, 60]	         63.33









