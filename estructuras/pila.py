class Nodo:
    def __init__(self, valor):
        self.valor = valor          # Dato guardado (en EduCore, la descripción de una acción).
        self.siguiente = None       # Nodo que está debajo de este en la pila.


class Pila:
    def __init__(self):
        self.tope = None            # Último elemento apilado (el primero en salir).
        self.tamano = 0             # Cantidad de elementos almacenados.

    def apilar(self, valor):
        # El nuevo nodo se coloca encima del tope actual.
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        self.tamano += 1

    def desapilar(self):
        # Retira y devuelve el tope. Si la pila está vacía devuelve None.
        if self.tope is None:
            return None

        valor = self.tope.valor
        self.tope = self.tope.siguiente
        self.tamano -= 1
        return valor

    def consultar_tope(self):
        # Devuelve el tope sin retirarlo. Si la pila está vacía devuelve None.
        if self.tope is None:
            return None
        return self.tope.valor

    def esta_vacia(self):
        return self.tope is None

    def recorrer(self):
        # Valores desde el tope (más reciente) hasta la base (más antiguo).
        valores = []
        actual = self.tope
        while actual is not None:
            valores.append(actual.valor)
            actual = actual.siguiente
        return valores

    def mostrar_estructura(self):
        # Diagnóstico: dibuja los nodos de la pila para explicarla en la defensa.
        if self.tope is None:
            return "tope -> None (pila vacía)"

        texto = "tope"
        actual = self.tope
        while actual is not None:
            texto += f" -> [{actual.valor}]"
            actual = actual.siguiente
        texto += " -> None"
        return texto