# Clase Calificador que: (1) tenga método validar_nota(nota) que retorne True si 0 ≤ nota ≤ 100,
# False en caso contrario; (2) tenga método cargar_notas(*args) que reciba múltiples notas, 
# las valide, agregue solo las válidas a una lista interna, y retorne esa lista; 
# (3) tenga método promedio() que retorne el promedio de notas almacenadas.


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


# Clase AnalizadorTexto que: (1) tenga método agregar_palabra(palabra) que agregue la 
# palabra a un conjunto (para evitar duplicados) y a una lista (para el orden); 
# (2) tenga método contar_palabras() que retorne cuántas palabras únicas hay; 
# (3) tenga método agregar_multiples(*args) que reutilice agregar_palabra para varios.


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



# Clase CarroCompras que: (1) tenga método agregar_articulo(nombre, precio) que guarde en un diccionario {nombre: precio}; 
# (2) tenga método total_carrito() que retorne la suma de todos los precios; 
# (3) tenga método articulos_por_rango(precio_min, precio_max) que retorne una lista con artículos dentro del rango.


class CarroCompras:
    def __init__(self):
        self.articulos = {}
    
    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio
        
    def total_carrito(self):
        return sum(self.articulos.values())
    
    def articulos_por_rango(self, precio_min, precio_max):
        return [
            nombre
            for nombre, precio in self.articulos.items()
            if precio_min <= precio <= precio_max
        ]
        
artic = CarroCompras()
artic.agregar_articulo("libro", 20)
artic.agregar_articulo("lapiz", 5)
print(artic.total_carrito())
        
# Clase InversorSecuencia que: (1) tenga método invertir_lista(lista) que retorne la lista 
# invertida sin usar reversed() (usa manual con bucles); 
# (2) tenga método invertir_multiples(*listas) que reutilice el anterior para invertir 
# varias listas y retorne un diccionario {lista_original: lista_invertida}.

class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            resultado[tuple(lista)] = self.invertir_lista(lista)
        return resultado

secuencia = InversorSecuencia()
secuencia.invertir_lista([1, 2, 3, 4])

# Clase AnalizadorNumeros que: (1) tenga método es_par(numero) que retorne True/False;
# (2) tenga método separar(*numeros) que retorne un diccionario {'pares': [...], 'impares': [...]} reutilizando es_par;
# (3) tenga método cantidad_pares_impares() que retorne una tupla (cant_pares, cant_impares).
        
class AnalizadorNumeros:
    def __init__(self):
        self.resultado = {'pares': [], 'impares': []}
 
    def es_par(self, numero):
        return numero % 2 == 0
        
    def separar(self, *numeros):
        pares = []
        impares = []
        for numero in numeros:
            if self.es_par(numero):
                pares.append(numero)
            else:
                impares.append(numero)
         
        self.resultado = {'pares': pares, 'impares': impares}
        return self.resultado
 
    def cantidad_pares_impares(self):
        
        cant_par = len(self.resultado['pares'])
        cant_impar = len(self.resultado['impares'])
        return (cant_par, cant_impar) 
    
resul = AnalizadorNumeros()
print(resul.es_par(2))   
print(resul.separar(2,3,4,5,6,7,8)) 
print(resul.cantidad_pares_impares())

# Clase GestorTemperatura que: (1) tenga método registrar_temperatura(temp) que guarde en una lista; 
# (2) tenga método minima()`, `maxima()`, `promedio() que calculen estadísticas; 
# (3) tenga método registrar_multiples(*temps) que reutilice el registro para varias temperaturas.


# Clase GestorPersonas que: (1) tenga método agregar_persona(nombre, edad) que guarde en un diccionario;
# (2) tenga método personas_mayores(edad_minima) que retorne una lista de nombres cuya edad sea ≥;
# (3) tenga método edad_promedio() que retorne el promedio de edades.



# Clase Equipos que: (1) tenga método crear_equipo(nombre_equipo) que inicie un equipo como una lista vacía en un diccionario; 
# (2) tenga método agregar_jugador(equipo, jugador) que añada el jugador al equipo;
# (3) tenga método equipo_mayor_integrantes() que retorne el nombre del equipo con más jugadores.



# Clase AnalizadorString que: (1) tenga método solo_vocales(letra) que retorne True si es vocal;
# (2) tenga método contar_por_tipo(texto) que retorne un diccionario 
# {'vocales': cant, 'consonantes': cant, 'digitos': cant} reutilizando métodos; 
# (3) tenga atributo que guarde el texto más largo analizado.



# Clase Tareas que: (1) tenga método agregar_tarea(descripcion, prioridad) que guarde en una lista de tuplas (descripción, prioridad); 
# (2) tenga método tareas_prioritarias() que retorne solo las de prioridad alta;
# (3) tenga método eliminar_completada(descripcion) que borre la tarea de la lista.































