# Crea una clase Playlist que:

# Guarde canciones en una lista. Cada canción es un diccionario con titulo y duracion (en segundos).
# Tenga agregar(titulo, duracion).
# Tenga duracion_total() que devuelva la suma de las duraciones.
 
class Playlist:
    def __init__(self):
        self.canciones = []

    def agregar(self, titulo, duracion):
        self.canciones.append({"titulo": titulo, "duracion": duracion})

    def duracion_total(self):
        return sum(c["duracion"] for c in self.canciones)


mi_playlist = Playlist()

mi_playlist.agregar("Canción A", 210)
mi_playlist.agregar("Canción B", 185)
mi_playlist.agregar("Canción C", 240)

print("Canciones:", len(mi_playlist.canciones))
print("Duración total:", mi_playlist.duracion_total())
 
 
 
 