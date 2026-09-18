# Clase AnalizadorTexto que: (1) tenga método agregar_palabra(palabra) que agregue la 
# palabra a un conjunto (para evitar duplicados) y a una lista (para el orden); 
# (2) tenga método contar_palabras() que retorne cuántas palabras únicas hay; 
# (3) tenga método agregar_multiples(*args) que reutilice agregar_palabra para varios.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: se crea una o varias palabras (texto)
# Proceso: se empieza a evitar duplicados con un set; se conservar el orden con una list
# Salida: se recibe la lista de palabras en orden de llegada; cantidad de palabras únicas 
 
## Paso 2: Bosquejo
# Entran: "joel", "ana", "joel"
#   "joel" → ¿está en el set? No → agregar a set y a lista
#   "ana"  → ¿está en el set? No → agregar a set y a lista
#   "joel" → ¿está en el set? Sí → NO se repite

# Lista final (orden): ['joel', 'ana']
# Set final (sin duplicados): {'joel', 'ana'} → cuenta = 2

## Paso 3: Descubrir el patrón

# El Método agregar_palabra(palabra): usa dos estructuras a la vez, un set para deduplicar en O(1) y una list para preservar el orden de inserción.

# El Método contar_palabras(): reutiliza el tamaño del set con len(), sin recorrer nada de nuevo.

# El Método agregar_multiples(*args): recorre *args y llama a agregar_palabra() por cada una y se reutilización de método.

# Los Conceptos aplicados: colecciones (set vs. list y cuándo usar cada una), control de flujo, reutilización de métodos.

## Paso 4: Escribir el código
class AnalizadorTexto:
    def __init__(self):
        self.palabras = set()
        self.lista = []
        
    def agregar_palabra(self, palabra):
        if palabra not in self.palabras:
            self.palabras.add(palabra)
            self.lista.append(palabra)

    def contar_palabras(self):
        return len(self.palabras)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)

pal = AnalizadorTexto()
pal.agregar_multiples("joel", "ana", "joel")
print(pal.lista)
print(pal.contar_palabras())

#### Paso 5: Prueba de escritorio
#      Acción	                        self.notas	        Salida
# a = AnalizadorTexto()	                 set()	             []
# agregar_palabra("joel")                {'joel'}	        ['joel']
# agregar_palabra("ana")	             {'joel','ana'}	    ['joel','ana']
# agregar_palabra("joel") otra vez       sin cambio         sin cambio
# contar_palabras()                        —                retorna 2

