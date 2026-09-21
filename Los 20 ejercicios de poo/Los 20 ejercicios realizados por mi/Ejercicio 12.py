# Crea una clase GestorEtiquetas que:

# 1) Tenga un método extraer_etiquetas(texto) que reciba un texto y retorne una tupla con 
# las palabras del texto en minúsculas, sin repetidas y sin signos de puntuación (, y .). Conserva el orden de aparición.
# Ejemplo: extraer_etiquetas("Python es genial. Python es rápido, genial") → ('python', 'es', 'genial', 'rápido')

# 2) Tenga un método etiquetas_en_todos(*textos) que reciba varios textos y retorne una lista
# ordenada alfabéticamente con las etiquetas que aparecen en todos los textos.
# Ejemplo: etiquetas_en_todos("Python es genial", "Java es genial", "Go es genial y rápido") → ['es', 'genial']

# 3) Tenga un método etiquetas_exclusivas(texto_a, texto_b) que retorne una tupla de dos listas ordenadas: 
# las etiquetas que solo están en texto_a y las que solo están en texto_b.
# Ejemplo: etiquetas_exclusivas("Python es genial", "Java es rápido") → (['genial', 'python'], ['java', 'rápido'])


class GestorEtiquetas:
    def extraer_etiquetas(self, texto):
        limpio = texto.lower().replace(",", "").replace(".", "")
        vistas = set()
        resultado = []
        for palabra in limpio.split():
            if palabra not in vistas:
                vistas.add(palabra)
                resultado.append(palabra)
        return tuple(resultado)

    def etiquetas_en_todos(self, *textos):
        if not textos:
            return []
        conjuntos = [set(self.extraer_etiquetas(t)) for t in textos]
        return sorted(set.intersection(*conjuntos))

    def etiquetas_exclusivas(self, texto_a, texto_b):
        a = set(self.extraer_etiquetas(texto_a))
        b = set(self.extraer_etiquetas(texto_b))
        return (sorted(a - b), sorted(b - a))


g = GestorEtiquetas()

print(g.extraer_etiquetas("Python es genial. Python es rápido, genial"))

print(g.etiquetas_en_todos("Python es genial", "Java es genial", "Go es genial y rápido"))

print(g.etiquetas_exclusivas("Python es genial", "Java es rápido"))









