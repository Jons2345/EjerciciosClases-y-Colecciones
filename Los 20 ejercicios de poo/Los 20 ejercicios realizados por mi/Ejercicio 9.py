# Crea una clase AnalizadorFrase que:

# 1) Tenga un método es_signo(caracter) que retorne True si el carácter es un 
# signo de puntuación (. , ! ? ; : etc.) y False si no.
# 2) Tenga un método contar_por_categoria(texto) que retorne un diccionario:
# {'mayusculas': cant, 'minusculas': cant, 'espacios': cant, 'signos': cant}
# reutilizando es_signo. Los dígitos y otros caracteres se ignoran.
# 3) Tenga un atributo texto_mas_signos que guarde el texto analizado con más 
# signos de puntuación. Si hay empate, se queda el primero que llegó.


import string

class AnalizadorFrase:
    def __init__(self):
        self.texto_mas_signos = ""
        self.max_signos = 0
        self.total_analisis = 0

    def es_signo(self, caracter):
        return caracter in string.punctuation

    def contar_por_categoria(self, texto):
        conteo = {"mayusculas": 0, "minusculas": 0, "espacios": 0, "signos": 0}

        for caracter in texto:
            if caracter.isupper():
                conteo["mayusculas"] += 1
            elif caracter.islower():
                conteo["minusculas"] += 1
            elif caracter.isspace():
                conteo["espacios"] += 1
            elif self.es_signo(caracter):
                conteo["signos"] += 1

        self.total_analisis += 1

        if conteo["signos"] > self.max_signos:
            self.max_signos = conteo["signos"]
            self.texto_mas_signos = texto

        return conteo

a = AnalizadorFrase()

print(a.es_signo("!"))     
print(a.es_signo("a"))    

print(a.contar_por_categoria("Hola, Mundo!"))
print(a.texto_mas_signos)   

print(a.contar_por_categoria("Hola!!!"))
print(a.texto_mas_signos)   

print(a.total_analisis)     





