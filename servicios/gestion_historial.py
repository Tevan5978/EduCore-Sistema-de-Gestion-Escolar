from estructuras.pila import Pila


class GestionHistorial:
    def __init__(self):
        self.pila = Pila()

    def registrar_accion(self, descripcion):
        if descripcion.strip() == "":
            return False
        self.pila.apilar(descripcion.strip())
        return True

    def consultar_ultima(self):
        return self.pila.consultar_tope()

    def retirar_ultima(self):
        return self.pila.desapilar()

    def cantidad(self):
        return self.pila.tamano

    def mostrar_historial(self):
        if self.pila.esta_vacia():
            print("El historial de acciones está vacío.")
            return

        print("\nHISTORIAL DE ACCIONES (de la más reciente a la más antigua)")
        posicion = 1
        for accion in self.pila.recorrer():
            print(f"{posicion}. {accion}")
            posicion += 1

        print("\nESTRUCTURA DE LA PILA")
        print(self.pila.mostrar_estructura())