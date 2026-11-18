# RECORRIDOS DEL GRAFO DE EDUCORE

from estructuras.cola import Cola


class RecorridosGrafo:
    def __init__(self, grafo):
        self.grafo = grafo

    def bfs(self, inicio):
        if not self.grafo.existe_dependencia(inicio):
            print("La dependencia no existe.")
            return []

        visitados = []
        cola = Cola()
        cola.encolar(inicio)
        visitados.append(inicio)

        while not cola.esta_vacia():
            actual = cola.desencolar()
            for vecino in self.grafo.consultar_vecinos(actual):
                if vecino not in visitados:
                    visitados.append(vecino)
                    cola.encolar(vecino)

        return visitados

    def dfs(self, inicio):
        if not self.grafo.existe_dependencia(inicio):
            print("La dependencia no existe.")
            return []

        visitados = []

        def recorrer(actual):
            visitados.append(actual)
            for vecino in self.grafo.consultar_vecinos(actual):
                if vecino not in visitados:
                    recorrer(vecino)

        recorrer(inicio)
        return visitados

    def buscar_ruta(self, origen, destino):
        if not self.grafo.existe_dependencia(origen):
            print("La dependencia de origen no existe.")
            return None
        if not self.grafo.existe_dependencia(destino):
            print("La dependencia de destino no existe.")
            return None

        cola = Cola()
        cola.encolar([origen])
        visitados = [origen]

        while not cola.esta_vacia():
            ruta = cola.desencolar()
            actual = ruta[-1]

            if actual == destino:
                return ruta

            for vecino in self.grafo.consultar_vecinos(actual):
                if vecino not in visitados:
                    visitados.append(vecino)
                    cola.encolar(ruta + [vecino])

        return None
