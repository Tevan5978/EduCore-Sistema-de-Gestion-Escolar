class Nodo:
    def __init__(self, valor):
        self.valor = valor          # Dato guardado (en EduCore, un objeto Estudiante).
        self.siguiente = None       # Nodo que viene después, o None si es el último.
        self.anterior = None        # Nodo que viene antes, o None si es el primero.


class ListaDoble:
    def __init__(self):
        self.cabeza = None          # Primer nodo de la lista.
        self.cola = None            # Último nodo de la lista.
        self.tamano = 0             # Cantidad de nodos almacenados.

    def agregar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

        self.tamano += 1

    def agregar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

        self.tamano += 1

    def esta_vacia(self):
        return self.cabeza is None

    def recorrer_adelante(self):
        valores = []
        actual = self.cabeza
        while actual is not None:
            valores.append(actual.valor)
            actual = actual.siguiente
        return valores

    def recorrer_atras(self):
        valores = []
        actual = self.cola
        while actual is not None:
            valores.append(actual.valor)
            actual = actual.anterior
        return valores

    def buscar(self, codigo):
        actual = self.cabeza
        while actual is not None:
            if actual.valor.codigo == codigo:
                return actual.valor
            actual = actual.siguiente
        return None

    def eliminar(self, codigo):
        actual = self.cabeza
        while actual is not None:
            if actual.valor.codigo == codigo:
                if actual.anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    actual.anterior.siguiente = actual.siguiente

                if actual.siguiente is None:
                    self.cola = actual.anterior
                else:
                    actual.siguiente.anterior = actual.anterior

                self.tamano -= 1
                return True
            actual = actual.siguiente
        return False

    def mostrar_estructura(self):
        # Diagnóstico: dibuja los nodos y sus enlaces en ambos sentidos.
        if self.cabeza is None:
            return "None <- (lista vacía) -> None"

        texto = "None"
        actual = self.cabeza
        while actual is not None:
            texto += f" <-> [{getattr(actual.valor, 'codigo', actual.valor)}]"
            actual = actual.siguiente
        texto += " <-> None"
        return texto