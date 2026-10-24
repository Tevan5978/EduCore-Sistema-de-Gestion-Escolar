
# COLA DOBLEMENTE ENLAZADA

class Cola:

    class Nodo:
        def __init__(self, info=None):
            self.info = info
            self.anterior = None
            self.siguiente = None

    def __init__(self):
        # Nodos centinela: marcan el inicio y el final
        self.cabeza = self.Nodo()
        self.cola = self.Nodo()

        self.cabeza.siguiente = self.cola
        self.cola.anterior = self.cabeza

        self.cantidad = 0

    def esta_vacia(self):
        return self.cantidad == 0

    def encolar(self, info):
        nuevo = self.Nodo(info)

        # Insertar antes del centinela final
        ultimo = self.cola.anterior

        ultimo.siguiente = nuevo
        nuevo.anterior = ultimo

        nuevo.siguiente = self.cola
        self.cola.anterior = nuevo

        self.cantidad += 1

    def consultar_primero(self):
        if self.esta_vacia():
            return None

        return self.cabeza.siguiente.info

    def desencolar(self):
        if self.esta_vacia():
            return None

        primero = self.cabeza.siguiente
        info = primero.info

        # Quitar el primer nodo y reconectar los enlaces
        self.cabeza.siguiente = primero.siguiente
        primero.siguiente.anterior = self.cabeza

        self.cantidad -= 1

        return info

    def numero_elementos(self):
        return self.cantidad


    def mostrar(self):
        if self.esta_vacia():
            print("No hay solicitudes pendientes.")
            return

        actual = self.cabeza.siguiente

        while actual != self.cola:
            solicitud = actual.info

            print("------------------------------")
            print("Turno:", solicitud["turno"])
            print("Estudiante:", solicitud["nombre"])
            print("Motivo:", solicitud["motivo"])
            print("------------------------------")

            actual = actual.siguiente
