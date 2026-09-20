# Crea una clase AnalizadorTextos que:

# 1) Tenga un método es_palindromo(palabra) que retorne True si la palabra se 
# lee igual al derecho y al revés (ej: "reconocer"), o False si no.
# 2) Tenga un método separar(*palabras) que retorne un 
# diccionario {'palindromos': [...], 'normales': [...]}, reutilizando es_palindromo.
# 3) Tenga un método cantidad_palindromos_normales() que retorne una tupla (cant_palindromos, cant_normales).

class AnalizadorTextos:
    
    def __init__(self):
        self.palindromos = []
        self.normales = []
    
    def es_palindromo(self, palabra):
        return palabra == palabra[::-1]
    
    def separar(self, *palabras):  
        self.palindromos = []
        self.normales = []
              
        for p in palabras:
            if self.es_palindromo(p):
                self.palindromos.append(p)
            else:
                self.normales.append(p)
        return {'palindromos': self.palindromos, 'normales': self.normales}
    
    def cantidad_palindromos_normales(self):
        return (len(self.palindromos), len(self.normales)) 
            
analisis = AnalizadorTextos()
print(analisis.separar("casa", "radar"))









