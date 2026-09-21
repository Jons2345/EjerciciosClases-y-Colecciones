# Crea una clase AgrupadorNotas que:

# 1) Tenga un método clasificar_nota(nota) que retorne la categoría según estos rangos:
# "reprobado": de 0 a 59
# "regular": de 60 a 74
# "bueno": de 75 a 89
# "excelente": de 90 a 100
# Si la nota es menor que 0 o mayor que 100, debe lanzar un ValueError.
# 2) Tenga un método agrupar_por_categoria(*notas) que retorne un diccionario con {categoría: [notas]}.
# 3) Tenga un método nota_promedio_categoria(categoria) que retorne el promedio de las notas de esa categoría (o None si no hay datos).

class AgrupadorNotas:
    def __init__(self):
        self.grupos = {}

    def clasificar_nota(self, nota):
        if nota < 0 or nota > 100:
            raise ValueError("La nota debe estar entre 0 y 100")
        elif nota < 60:
            return "reprobado"
        elif nota < 75:
            return "regular"
        elif nota < 90:
            return "bueno"
        else:
            return "excelente"

    def agrupar_por_categoria(self, *notas):
        self.grupos = {}

        for nota in notas:
            categoria = self.clasificar_nota(nota)
            self.grupos.setdefault(categoria, []).append(nota)

        return self.grupos

    def nota_promedio_categoria(self, categoria):
        if categoria not in self.grupos or len(self.grupos[categoria]) == 0:
            return None

        notas = self.grupos[categoria]
        return sum(notas) / len(notas)

    def mejor_categoria(self):
        if not self.grupos:
            return None

        return max(self.grupos, key=self.nota_promedio_categoria)

    def porcentaje_aprobados(self):
        total = sum(len(lista) for lista in self.grupos.values())

        if total == 0:
            return None

        reprobados = len(self.grupos.get("reprobado", []))
        return (total - reprobados) / total * 100


agrupador = AgrupadorNotas()

print(agrupador.clasificar_nota(45))    
print(agrupador.clasificar_nota(70))    
print(agrupador.clasificar_nota(88))    
print(agrupador.clasificar_nota(95))    

resultado = agrupador.agrupar_por_categoria(30, 55, 65, 80, 85, 92, 100)
print(resultado)

print(agrupador.nota_promedio_categoria("bueno"))        
print(agrupador.nota_promedio_categoria("excelente"))    
print(agrupador.nota_promedio_categoria("inexistente"))  

print(agrupador.mejor_categoria())                      
print(round(agrupador.porcentaje_aprobados(), 2))       

                              













