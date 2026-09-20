# Crea una clase ProcesadorTexto que:

# Tenga un método contar_vocales(texto) que retorne cuántas 
# vocales (a, e, i, o, u) tiene el texto, sin usar .count(). Usa un bucle manual. Debe funcionar con mayúsculas y minúsculas.
# Tenga un método contar_vocales_multiples(*textos) que reutilice el 
# método anterior para procesar varios textos y retorne un diccionario {texto: cantidad_de_vocales}.

class ProcesadorTexto:
    def __init__(self):
        self.VOCALES = "aeiouáéíóúü"

    def contar_vocales(self, texto):
        contador = 0
        for letra in texto:
            if letra.lower() in self.VOCALES:
                contador += 1
        return contador

    def contar_vocales_multiples(self, *textos):
        resultado = {}
        total = 0
        for texto in textos:
            cantidad = self.contar_vocales(texto)
            resultado[texto] = cantidad
            total += cantidad
        resultado["total"] = total
        return resultado

p = ProcesadorTexto()

print(p.contar_vocales("Hola Mundo"))

print(p.contar_vocales_multiples("casa", "Python", "AEIOU"))





