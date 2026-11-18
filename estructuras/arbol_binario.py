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

    def eliminar(self, codigo):
        padre = None
        actual = self.raiz

        while actual is not None and codigo != actual.codigo:
            padre = actual
            if codigo < actual.codigo:
                actual = actual.izquierda
            else:
                actual = actual.derecha

        if actual is None:
            return False

        if actual.izquierda is not None and actual.derecha is not None:
            sucesor_padre = actual
            sucesor = actual.derecha
            while sucesor.izquierda is not None:
                sucesor_padre = sucesor
                sucesor = sucesor.izquierda

            actual.codigo = sucesor.codigo
            actual.informacion = sucesor.informacion
            if sucesor_padre.izquierda is sucesor:
                sucesor_padre.izquierda = sucesor.derecha
            else:
                sucesor_padre.derecha = sucesor.derecha
        else:
            reemplazo = actual.izquierda
            if reemplazo is None:
                reemplazo = actual.derecha

            if padre is None:
                self.raiz = reemplazo
            elif padre.izquierda is actual:
                padre.izquierda = reemplazo
            else:
                padre.derecha = reemplazo

        self.cantidad -= 1
        return True
