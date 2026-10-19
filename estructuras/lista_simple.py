class Nodo:
    def __init__(self, valor):
        self.valor = valor          # Dato guardado (en EduCore, un objeto Estudiante).
        self.siguiente = None       # Apunta al nodo que sigue, o None si es el último.


class ListaSimple:
    def __init__(self):
        self.cabeza = None          # Primer nodo de la lista.
        self.cola = None            # Último nodo de la lista.
        self.tamano = 0             # Cantidad de nodos almacenados.

    def agregar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)

        if self.cabeza is None:
            # Lista vacía: el nodo es a la vez cabeza y cola.
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

        self.tamano += 1

    def agregar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

        self.tamano += 1

    def esta_vacia(self):
        return self.cabeza is None

    def recorrer(self):
        valores = []
        actual = self.cabeza
        while actual is not None:
            valores.append(actual.valor)
            actual = actual.siguiente
        return valores

    def mostrar_estructura(self):
        # Diagnóstico: dibuja los nodos y sus enlaces para explicarlos en la defensa.
        if self.cabeza is None:
            return "cabeza -> None (lista vacía)"

        texto = "cabeza"
        actual = self.cabeza
        while actual is not None:
            texto += f" -> [{getattr(actual.valor, 'codigo', actual.valor)}]"
            actual = actual.siguiente
        texto += " -> None"
        texto += f"  (cola: {getattr(self.cola.valor, 'codigo', self.cola.valor)})"
        return texto