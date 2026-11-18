# GRAFO DE DEPENDENCIAS DE EDUCORE


class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_dependencia(self, nombre):
        if nombre in self.vertices:
            print("La dependencia ya existe.")
            return False

        self.vertices[nombre] = []
        print("Dependencia agregada correctamente.")
        return True

    def conectar(self, origen, destino):
        if origen not in self.vertices:
            print("La dependencia de origen no existe.")
            return False
        if destino not in self.vertices:
            print("La dependencia de destino no existe.")
            return False
        if origen == destino:
            print("No se puede conectar una dependencia consigo misma.")
            return False
        if destino in self.vertices[origen]:
            print("Estas dependencias ya estan conectadas.")
            return False

        self.vertices[origen].append(destino)
        self.vertices[destino].append(origen)
        print("Dependencias conectadas correctamente.")
        return True

    def consultar_vecinos(self, nombre):
        if not self.existe_dependencia(nombre):
            return []
        return self.vertices[nombre]

    def mostrar_grafo(self):
        if not self.vertices:
            print("El grafo no tiene dependencias.")
            return

        for nombre in self.vertices:
            print(f"{nombre} -> {self.vertices[nombre]}")

    def existe_dependencia(self, nombre):
        return nombre in self.vertices
