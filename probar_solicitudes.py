
from servicios.gestion_solicitudes import GestionSolicitudes

gestion = GestionSolicitudes()

gestion.registrar_solicitud("Ana", "Problema con las notas")
gestion.registrar_solicitud("Carlos", "Solicitud de certificado")
gestion.registrar_solicitud("Laura", "Actualizar datos")

gestion.mostrar_pendientes()

print("\n--- CONTAR SOLICITUDES ---")
gestion.contar_pendientes()

print("\n--- ATENDER SIGUIENTE ---")
gestion.atender_siguiente()

print("\n--- VERIFICAR LA COLA ---")
gestion.mostrar_pendientes()

print("\n--- CANTIDAD FINAL ---")
gestion.contar_pendientes()
