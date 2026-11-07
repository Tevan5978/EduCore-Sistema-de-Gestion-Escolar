class Nodo:
    def __init__(self, codigo, informacion):
        self.codigo = codigo
        self.informacion = informacion
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None
        self.cantidad = 0

    def esta_vacio(self):
        return self.raiz is None

    def insertar(self, codigo, informacion):
        nuevo = Nodo(codigo, informacion)

        if self.raiz is None:
            self.raiz = nuevo
            self.cantidad += 1
            return True

        actual = self.raiz
        while actual is not None:
            if codigo == actual.codigo:
                return False
            if codigo < actual.codigo:
                if actual.izquierda is None:
                    actual.izquierda = nuevo
                    self.cantidad += 1
                    return True
                actual = actual.izquierda
            else:
                if actual.derecha is None:
                    actual.derecha = nuevo
                    self.cantidad += 1
                    return True
                actual = actual.derecha

    def buscar(self, codigo):
        actual = self.raiz
        while actual is not None:
            if codigo == actual.codigo:
                return actual.informacion
            if codigo < actual.codigo:
                actual = actual.izquierda
            else:
                actual = actual.derecha
        return None
