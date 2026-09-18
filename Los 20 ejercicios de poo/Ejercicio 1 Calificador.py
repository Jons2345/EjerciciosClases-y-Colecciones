# Clase Calificador que: (1) tenga método validar_nota(nota) que retorne True si 0 ≤ nota ≤ 100,
# False en caso contrario; (2) tenga método cargar_notas(*args) que reciba múltiples notas, 
# las valide, agregue solo las válidas a una lista interna, y retorne esa lista; 
# (3) tenga método promedio() que retorne el promedio de notas almacenadas.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crean varias notas (números) recibidas en cargar_notas(*args)
# Proceso: se empieza a validar que cada nota esté entre 0 y 100; se guarda solo las válidas; se calcular el promedio
# Salida: se empieza a salir la lista de notas válidas almacenadas; promedio como número


## Paso 2: Bosquejo
# Entran: 80, 50, 60
#   ¿80 está entre 0 y 100? Sí → guardar
#   ¿50 está entre 0 y 100? Sí → guardar
#   ¿60 está entre 0 y 100? Sí → guardar
# Lista final: [80, 50, 60]
# Promedio = (80+50+60) / 3 = 190/3 = 63.33

# Si entrara -5 → no cumple 0≤nota → se descarta

## Paso 3: Descubrir el patrón

# El Método validar_nota(nota): es un validador booleano. Compara con operadores relacionales (>=, <=) y retorna True/False.

# El Método cargar_notas(*args): recibe múltiples notas con *args, recorre con un for y reutiliza validar_nota() antes de hacer append. 
# Esta es la reutilización de métodos.

# El Método promedio(): usa sum() y len() sobre la lista interna acumulada en self.notas.

# Los Conceptos aplicados: operadores relacionales, control de flujo (for, if), colecciones (listas, *args), reutilización de métodos.

## Paso 4: Escribir el código
class Calificador:
    def __init__(self):
        self.notas = []
    
    def validar_nota(self, nota):
        if nota >= 0 and  nota <= 100:
            return True
        else:
            return False
        # return 0 ≤ nota ≤ 100
        
    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas
    
    def promedio(self):
        return sum(self.notas)/len(self.notas)

Calificacion = Calificador()
print(Calificacion.cargar_notas(80, 50, 60))
print (Calificacion.promedio())

#### Paso 5: Prueba de escritorio
#      Acción	                self.notas	        Salida
# c = Calificador()	               []	              —
# cargar_notas(80, 50, 60)	   [80, 50, 60]	      [80, 50, 60]
# promedio()	               [80, 50, 60]	         63.33

