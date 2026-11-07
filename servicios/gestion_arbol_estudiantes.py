from estructuras.arbol_binario import ArbolBinario


class GestionArbolEstudiantes:
    def __init__(self):
        self.arbol = ArbolBinario()

    def insertar(self, estudiante):
        return self.arbol.insertar(estudiante.codigo, estudiante)

    def buscar(self, codigo):
        return self.arbol.buscar(codigo)
