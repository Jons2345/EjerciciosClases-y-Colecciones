# Clase AgrupadorEdades que: (1) tenga método clasificar_edad(edad) que retorne la categoría ("niño", "adolescente", "adulto", "mayor");
# (2) tenga método agrupar_por_categoria(*edades) que retorne un diccionario con {categoría: [edades]};
# (3) tenga método edad_promedio_categoria(categoria).

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea una edad, o varias edades con *edades; una categoría para el promedio.
# Proceso: se empieza a decidir la categoría con if/elif/else; 
# agregar cada edad a la lista de su categoría; promediar con suma / cantidad.
# Salida: se ve una categoría (texto); diccionario {categoría: [edades]}; el promedio (o None).


## Paso 2: Bosquejo
# Reglas: <12 niño · <18 adolescente · <60 adulto · resto mayor
#   5 → niño        15 → adolescente   30 → adulto
#   8 → niño        70 → mayor         45 → adulto
# Grupos: niño [5, 8] · adolescente [15] · adulto [30, 45] · mayor [70]
# Promedio adulto: (30 + 45) / 2 = 37.5

## Paso 3: Descubrir el patrón
# El clasificar_edad: una cadena if / elif / else ordenada de menor a mayor. 
# Cada elif solo se evalúa si el anterior fue falso, por eso basta con el límite superior. Una edad negativa lanza ValueError.

# El agrupar_por_categoria(*edades): patrón de agrupar: si la categoría no es clave, se crea con lista vacía; luego se hace append.

# La edad_promedio_categoria: usa .get(categoria, []); si la lista está vacía retorna None (evita dividir entre cero).

# El Atributo grupos: guarda el último agrupamiento para que el promedio pueda consultarlo.

# Los Conceptos aplicados: condicionales encadenados, diccionarios de listas, *args, sum/len, excepciones.

## Paso 4: Escribir el código
class AgrupadorEdades:
    def __init__(self):
        self.grupos = {}

    def clasificar_edad(self, edad):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        if edad < 12:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 60:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        self.grupos = {}
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            if categoria not in self.grupos:
                self.grupos[categoria] = []
            self.grupos[categoria].append(edad)
        return self.grupos

    def edad_promedio_categoria(self, categoria):
        edades = self.grupos.get(categoria, [])
        if not edades:
            return None
        return sum(edades) / len(edades)


a = AgrupadorEdades()
print(a.agrupar_por_categoria(5, 15, 30, 8, 70, 45))
print(a.edad_promedio_categoria("adulto"))   
print(a.edad_promedio_categoria("niño"))     
print(a.edad_promedio_categoria("mayor"))    

# LÍNEA POR LÍNEA (FRAGMENTOS CLAVE)

# raise ValueError(...)
# Detiene el método con un error si la edad es negativa.

# elif edad < 18:
# Solo llega aquí si edad ≥ 12, por eso basta con el límite superior.

# if categoria not in self.grupos:
# Si la categoría aún no existe, crea su lista vacía.

# self.grupos[categoria].append(edad)
# Agrega la edad a la lista de su categoría.

# sum(edades) / len(edades)
# Promedio: suma de edades dividida entre la cantidad.

#### Paso 5: Prueba de escritorio

# EDAD	              CATEGORÍA	               GRUPOS
# 5	                   niño	                {niño: [5]}
# 15	             adolescente	    {niño: [5], adolescente: [15]}
# 30	               adulto	            {..., adulto: [30]}
# 8	                   niño	            {niño: [5, 8], ...}
# 70	               mayor	            {..., mayor: [70]}
# 45	               adulto	     {..., adulto: [30, 45], mayor: [70]}
# promedio('adulto') 	 —	              (30 + 45) / 2 = 37.5