# Crea una clase AnalizadorTemperaturas que:

# Tenga un método promedio(t1, t2) que reciba dos temperaturas (números) y retorne su promedio.
# Tenga un método temperatura_mas_alta(*temperaturas) que retorne la temperatura más alta de todas las recibidas.
# Tenga un atributo historial (una lista) donde se guarde cada promedio calculado.


class AnalizadorTemperaturas:
    def __init__(self):
        self.historial = []

    def promedio(self, t1, t2):
        resultado = (t1 + t2) / 2
        self.historial.append(resultado)
        return resultado

    def temperatura_mas_alta(self, *temperaturas):
        if not temperaturas:
            return "No se recibieron temperaturas"
        return max(temperaturas)

    def temperatura_mas_baja(self, *temperaturas):
        if not temperaturas:
            return "No se recibieron temperaturas"
        return min(temperaturas)


analizador = AnalizadorTemperaturas()

print(analizador.promedio(20, 30))                   
print(analizador.promedio(15, 25))                   
print(analizador.temperatura_mas_alta(18, 32, 25))  
print(analizador.temperatura_mas_baja(18, 32, 25))   
print(analizador.temperatura_mas_alta())             
print(analizador.historial)                         















