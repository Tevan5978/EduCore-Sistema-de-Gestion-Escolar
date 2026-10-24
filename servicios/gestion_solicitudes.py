
# GESTION DE SOLICITUDES DE ESTUDIANTES

from estructuras.cola import Cola


class GestionSolicitudes:

    def __init__(self):
        self.solicitudes = Cola()
        self.siguiente_turno = 1

    def registrar_solicitud(self, nombre, motivo):
        solicitud = {
            "turno": self.siguiente_turno,
            "nombre": nombre,
            "motivo": motivo
        }

        self.solicitudes.encolar(solicitud)
        print("Solicitud registrada correctamente.")
        print("Turno asignado:", self.siguiente_turno)

        self.siguiente_turno += 1

    def atender_siguiente(self):
        solicitud = self.solicitudes.desencolar()

        if solicitud is None:
            print("No hay solicitudes para atender.")
            return

        print("\nSolicitud atendida:")
        print("Turno:", solicitud["turno"])
        print("Estudiante:", solicitud["nombre"])
        print("Motivo:", solicitud["motivo"])

    def consultar_primera(self):
        solicitud = self.solicitudes.consultar_primero()

        if solicitud is None:
            print("No hay solicitudes pendientes.")
            return

        print("\nSiguiente solicitud:")
        print("Turno:", solicitud["turno"])
        print("Estudiante:", solicitud["nombre"])
        print("Motivo:", solicitud["motivo"])

    def mostrar_pendientes(self):
        print("\n--- SOLICITUDES PENDIENTES ---")
        self.solicitudes.mostrar()

    def contar_pendientes(self):
        cantidad = self.solicitudes.numero_elementos()
        print("Solicitudes pendientes:", cantidad)
        return cantidad
