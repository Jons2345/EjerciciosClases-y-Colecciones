# Crea una clase CodificadorAtbash que:

# 1) Tenga un método codificar_letra(letra) que retorne la letra "espejo" en el alfabeto. 
# Respeta mayúsculas y deja intactos los caracteres que no son letras.
# 2) Tenga un método codificar_frase(frase) que reutilice codificar_letra para toda la frase.
# 3) Tenga un diccionario como atributo que cuente cuántas veces se ha codificado cada letra (por ejemplo {'h': 2, 'o': 1}).


class CodificadorAtbash:
    ALFABETO = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self):
        self.contador = {}

    def codificar_letra(self, letra):
        es_mayuscula = letra.isupper()
        minuscula = letra.lower()

        if minuscula not in self.ALFABETO:
            return letra

        self.contador[minuscula] = self.contador.get(minuscula, 0) + 1

        posicion = self.ALFABETO.index(minuscula)
        posicion_espejo = 25 - posicion
        nueva_letra = self.ALFABETO[posicion_espejo]

        return nueva_letra.upper() if es_mayuscula else nueva_letra

    def codificar_frase(self, frase):
        resultado = ""
        for letra in frase:
            resultado += self.codificar_letra(letra)
        return resultado

atbash = CodificadorAtbash()

print(atbash.codificar_letra("a"))         
print(atbash.codificar_letra("M"))         
print(atbash.codificar_frase("Hola mundo")) 
print(atbash.contador)         






