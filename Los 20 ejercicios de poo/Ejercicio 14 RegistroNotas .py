# Clase RegistroNotas que: (1) tenga método registrar(estudiante, nota) que guarde en un diccionario; 
# (2) tenga método estudiantes_aprobados(nota_minima) que retorne lista de estudiantes; 
# (3) tenga método mejor_estudiante() que retorne nombre y nota del que tiene mayor calificación.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crean nombre y nota para registrar; una nota mínima para filtrar.
# Proceso: se empieza a guardar en diccionario {estudiante: nota}; se empieza a recorrer comparando;
# llevar la mejor nota vista hasta ahora. 
# el elemento de cada lista, si esa lista todavía lo tiene.
# Salida: se ve la lista de aprobados; tupla (nombre, nota) del mejor.


## Paso 2: Bosquejo
# daniela 98, josue 70, emilia 60
# ¿Aprobados con mínimo 65?
#   98 ≥ 65 sí, 70 ≥ 65 sí, 60 ≥ 65 no
# ¿El mejor? Empiezo con "mejor = nadie, nota -1"
#   daniela 98 > -1 → ahora es la mejor
#   josue 70 > 98 no
#   emilia 60 > 98 no
# Mejor: daniela con 98.

## Paso 3: Descubrir el patrón

# El registrar: asigna self.notas[estudiante] = nota; si el estudiante ya existía, la nota se actualiza.

# El estudiantes_aprobados: patrón de filtro: lista vacía, for sobre .items(), if nota >= nota_minima y append.

# El mejor_estudiante: patrón de máximo: una variable guarda la mejor nota vista y otra el nombre; 
# se actualizan solo cuando aparece una nota mayor.

# El Caso vacío: si no hay notas se retorna None.

# Los Conceptos aplicados: diccionarios, .items(), filtros con if, patrón de búsqueda del máximo, tuplas como retorno.

## Paso 4: Escribir el código
class RegistroNotas:
    def __init__(self):
        self.notas = {}
    
    def registrar(self,estudiante, nota):
        self.notas[estudiante] = nota
    
    def estudiantes_aprobados(self, nota_minima):
        aprobados = []
        
        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)
        return aprobados
    
    
    def  mejor_estudiante(self):
        if not self.notas:
            return None

        mejor_nombre = None
        mejor_nota = -1

        for estudiante, nota in self.notas.items():
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = estudiante

        return mejor_nombre, mejor_nota

registro = RegistroNotas()
registro.registrar("daniela", 98)
registro.registrar("josue", 70)
registro.registrar("emilia", 60)

print(registro.mejor_estudiante())

# LÍNEA POR LÍNEA (FRAGMENTOS CLAVE)

# self.notas[estudiante] = nota
# Guarda o actualiza la nota de ese estudiante.

# for estudiante, nota in self.notas.items():
# Recorre cada par nombre/nota del diccionario.

# if nota >= nota_minima:
# Condición de aprobado (incluye la nota mínima exacta).

# mejor_nota = -1
# Valor inicial menor que cualquier nota posible.

# return mejor_nombre, mejor_nota
# Retorna dos valores; Python los empaqueta en una tupla.

#### Paso 5: Prueba de escritorio

# ESTUDIANTE	    NOTA	   ¿nota > mejor_nota?	    MEJOR (nombre, nota)
# (inicio)	         —	              —	                   (None, -1)
# daniela	         98	          98 > -1 ✓	              (daniela, 98)
# josue	             70	          70 > 98 ✗	              (daniela, 98)
# emilia	         60	          60 > 98 ✗	              (daniela, 98)
# return	          —                —	              ('daniela', 98)

