# Crea una clase AnalizadorNumeros que:

# 1) Tenga un método encontrar_multiplos(numeros, divisor) que reciba una lista de enteros y 
# devuelva una lista con los que sean múltiplos del divisor.
# 2) Tenga un método agrupar_por_paridad(numeros) que devuelva un diccionario con dos claves:
# {"pares": [...], "impares": [...]}.
# 3) Tenga un método numeros_unicos() (sin parámetros) que devuelva un conjunto con los números 
# del último análisis, sin repetidos.

class AnalizadorNumeros:
    def __init__(self):
        self.numeros = []

    def encontrar_multiplos(self, numeros, divisor):
        if divisor == 0:
            raise ValueError("El divisor no puede ser cero")
        self.numeros = numeros
        return [n for n in numeros if n % divisor == 0]

    def agrupar_por_paridad(self, numeros):
        self.numeros = numeros
        grupos = {"pares": [], "impares": []}
        for n in numeros:
            if n % 2 == 0:
                grupos["pares"].append(n)
            else:
                grupos["impares"].append(n)
        return grupos



analizador = AnalizadorNumeros()
datos = [3, 6, 9, 12, 6, 15, 3, 8]

print(analizador.encontrar_multiplos(datos, 3))

print(analizador.agrupar_por_paridad(datos))


