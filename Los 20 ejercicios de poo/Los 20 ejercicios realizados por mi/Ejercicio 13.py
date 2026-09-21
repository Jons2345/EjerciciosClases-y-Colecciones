# Crea una clase FusionadorListas que:

# 1) Tenga un método fusionar(lista1, lista2) que reciba dos listas ya ordenadas de menor a mayor
# y retorne una única lista, también ordenada, con todos los elementos de ambas.
# 2) Tenga un método fusionar_multiples(*listas) que reutilice fusionar para combinar cualquier 
# cantidad de listas ordenadas.

class FusionadorListas:

    def fusionar(self, lista1, lista2):
        if not self.es_ordenada(lista1) or not self.es_ordenada(lista2):
            raise ValueError("Ambas listas deben estar ordenadas")

        resultado = []
        i = 0
        j = 0

        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1

        resultado.extend(lista1[i:])
        resultado.extend(lista2[j:])
        return resultado

    def fusionar_multiples(self, *listas):
        if not listas:
            return []

        resultado = list(listas[0])
        for lista in listas[1:]:
            resultado = self.fusionar(resultado, lista)
        return resultado


f = FusionadorListas()

print(f.fusionar([1, 3, 5], [2, 4, 6]))       
print(f.fusionar([1, 2, 3], [10, 20]))       
print(f.fusionar([], [1, 2]))                 
print(f.fusionar([], []))                     
print(f.fusionar([1, 1], [1, 2]))           

print(f.fusionar_multiples([1, 4], [2, 5], [3, 6]))  
print(f.fusionar_multiples())                        
print(f.fusionar_multiples([7, 8]))                  

print(f.es_ordenada([1, 2, 2, 3]))            
print(f.es_ordenada([3, 1, 2]))               

try:
    f.fusionar([3, 1], [2, 4])
except ValueError as e:
    print("Error:", e)                        