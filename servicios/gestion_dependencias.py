from estructuras.grafo import Grafo


class GestionDependencias:
    def __init__(self, grafo=None):
        # Si ya existe un grafo (el que usa RecorridosGrafo) se trabaja sobre ese mismo,
        # para no construir un segundo grafo distinto.
        if grafo is None:
            grafo = Grafo()
        self.grafo = grafo

    def agregar_dependencia(self, nombre):
        return self.grafo.agregar_dependencia(nombre)

    def conectar(self, origen, destino):
        return self.grafo.conectar(origen, destino)

    def listar_dependencias(self):
        return self.grafo.consultar_dependencias()

    def cantidad_dependencias(self):
        return len(self.grafo.vertices)

    def cantidad_conexiones(self):
        # Cada camino aparece en la lista de dos dependencias, por eso se divide entre 2.
        total = 0
        for nombre in self.grafo.vertices:
            total += len(self.grafo.vertices[nombre])
        return total // 2

    def mostrar_dependencias(self):
        dependencias = self.listar_dependencias()
        if len(dependencias) == 0:
            print("No hay dependencias registradas.")
            return

        print("\nDEPENDENCIAS DE LA INSTITUCIÓN")
        posicion = 1
        for nombre in dependencias:
            print(f"{posicion}. {nombre}")
            posicion += 1
        print(f"Total: {self.cantidad_dependencias()} dependencias y {self.cantidad_conexiones()} caminos.")

    def mostrar_vecinos(self, nombre):
        nombre = nombre.strip()
        if not self.grafo.existe_dependencia(nombre):
            print("La dependencia no existe.")
            return

        vecinos = self.grafo.consultar_vecinos(nombre)
        if len(vecinos) == 0:
            print(f"{nombre} no está conectada con ninguna dependencia.")
            return

        print(f"Vecinos de {nombre}:")
        for vecino in vecinos:
            print(f"- {vecino}")
