# Clase CodificadorCesar que: (1) tenga método codificar_letra(letra, desplazamiento) que retorne 
# la letra desplazada en el alfabeto (usar operador %); 
# (2) tenga método codificar_palabra(palabra, desplazamiento) que reutilice para toda la palabra;
# (3) tenga un diccionario como atributo para historial de codificaciones.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea una letra o palabra y un desplazamiento (positivo o negativo).
# Proceso: se empieza a convertir la letra a su posición 0–25, sumar el desplazamiento con % 26 para dar 
# la vuelta y volver a convertir a letra.
# Salida: se ve la letra o palabra codificada; el historial de codificaciones.


## Paso 2: Bosquejo
# Alfabeto: a=0, b=1, c=2 ... z=25
# Codificar "h" con desplazamiento 3:
#   h está en la posición 7
#   7 + 3 = 10 → posición 10 = "k"
# ¿Y "z" con +3?
#   25 + 3 = 28 → 28 % 26 = 2 → "c"   (da la vuelta)
# Los espacios y símbolos no se tocan.

## Paso 3: Descubrir el patrón

# codificar_letra: si no es letra ASCII se retorna igual. Si es mayúscula la base es ord('A'),
# si es minúscula ord('a'). Fórmula: (posicion + desplazamiento) % 26.

# El operador % hace que el alfabeto sea circular y también funciona con desplazamientos negativos (decodificar).

# codificar_palabra: recorre cada letra, llama a codificar_letra y construye el resultado. Es la reutilización.

# historial: diccionario con clave (palabra, desplazamiento) y valor el resultado.

# Conceptos aplicados: operador %, ord/chr, cadenas, bucles, diccionarios con tuplas como clave.

## Paso 4: Escribir el código
class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if not (letra.isascii() and letra.isalpha()):
            return letra
        base = ord('A') if letra.isupper() else ord('a')
        posicion = ord(letra) - base
        nueva_posicion = (posicion + desplazamiento) % 26
        return chr(base + nueva_posicion)

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""
        for letra in palabra:
            resultado += self.codificar_letra(letra, desplazamiento)
        self.historial[(palabra, desplazamiento)] = resultado
        return resultado

    def mostrar_historial(self):
        for (palabra, desp), resultado in self.historial.items():
            print(f"'{palabra}' con desplazamiento {desp} -> '{resultado}'")


codi = CodificadorCesar()
print(codi.codificar_palabra("Hola Mundo", 3))    
print(codi.codificar_palabra("Krod Pxqgr", -3))   
codi.mostrar_historial()

# LÍNEA POR LÍNEA (FRAGMENTOS CLAVE)

# letra.isascii() and letra.isalpha()
# Solo se codifican letras A–Z; espacios y símbolos pasan igual.

# ord(letra) - base
# Convierte la letra a su posición 0–25.

# (posicion + desplazamiento) % 26
# Suma el desplazamiento y da la vuelta al alfabeto.

# chr(base + nueva_posicion)
# Convierte la nueva posición otra vez a letra.

# self.historial[(palabra, desplazamiento)] = resultado
# Guarda la codificación con una tupla como clave.


#### Paso 5: Prueba de escritorio


# LETRA	        POSICIÓN	      (pos + 3) % 26	    RESULTADO
# H	               7	                10	                K
# o	               14	                17	                r
# l	               11	                14	                o
# a	               0	                3	                d
# (espacio)	       —	             no es letra	    (espacio)
# z (ejemplo)	   25	             28 % 26 = 2	        c