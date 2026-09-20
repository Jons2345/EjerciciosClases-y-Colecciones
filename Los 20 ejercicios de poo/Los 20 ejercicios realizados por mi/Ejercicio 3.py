# Crea una clase Estudiante que administre las notas de un alumno. 
# Cada materia tiene una nota, guardadas en un diccionario {materia: nota}.

# La clase debe tener:
# 1) agregar_nota(materia, nota): guarda la materia y su nota en el diccionario.
# 2) promedio(): retorna el promedio de todas las notas. (Pista: necesitas la suma y también saber cuántas notas hay.)
# 3) materias_por_rango(nota_min, nota_max): retorna una lista con los nombres de las materias
# cuya nota esté dentro del rango (ambos incluidos).

class Estudiante:
    def __init__(self):
        self.notas = {}
        
    def agregar_nota(self, materia, nota):
        self.notas[materia] = nota
        
    def promedio(self):
        return sum(self.notas.values()) / len(self.notas)
    
    def materias_por_rango(self, nota_min, nota_max):
        result = []
        for materia, nota in self.notas.items():
            if nota_min <= nota <= nota_max:
                result.append(materia)
        return result
            
            
est = Estudiante()
est.agregar_nota("Matemáticas", 8.5)
est.agregar_nota("Historia", 6.0)
est.agregar_nota("Física", 9.0)
est.agregar_nota("Inglés", 7.5)

print(est.promedio())                 
print(est.materias_por_rango(7, 9)) 






