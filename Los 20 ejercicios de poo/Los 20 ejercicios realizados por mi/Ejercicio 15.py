# Crea una clase PrimeAnalyzer que:

# Tenga un método es_primo(numero) que retorne True si el número es primo y False si no lo es.
# Tenga un método factores_primos(numero) que retorne una tupla con los factores primos del número, incluyendo repeticiones.
# Tenga un método analizar_multiples(*numeros) que retorne un diccionario {número: tupla_factores_primos}.

class PrimeAnalyzer:

    def es_primo(self, numero):
        if numero < 2:
            return False
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True

    def factores_primos(self, numero):
        factores = []
        d = 2
        while numero > 1:
            if numero % d == 0:
                factores.append(d)
                numero //= d
            else:
                d += 1
        return tuple(factores)

    def analizar_multiples(self, *numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.factores_primos(numero)
        return resultado

analyzer = PrimeAnalyzer()

print(analyzer.es_primo(7))          
print(analyzer.es_primo(12))
print(analyzer.factores_primos(12))  
print(analyzer.factores_primos(7))  
print(analyzer.analizar_multiples(12, 30, 7))