from servicios.operaciones_recursivas import contar_solicitudes


def mostrar_menu_fase3():
    print("\n===== SOLICITUDES DE ESTUDIANTES =====")
    print("1. Registrar solicitud")
    print("2. Atender siguiente solicitud")
    print("3. Consultar siguiente solicitud")
    print("4. Mostrar solicitudes pendientes")
    print("5. Contar solicitudes pendientes")
    print("0. Volver al menú principal")


def ejecutar_menu_fase3(solicitudes, historial):
    while True:
        mostrar_menu_fase3()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre del estudiante: ").strip()
            motivo = input("Motivo de la solicitud: ").strip()
            if nombre == "" or motivo == "":
                print("El nombre y el motivo no pueden estar vacíos.")
                continue
            turno = solicitudes.siguiente_turno
            solicitudes.registrar_solicitud(nombre, motivo)
            historial.registrar_accion(f"Solicitud registrada: turno {turno}, {nombre} ({motivo})")

        elif opcion == "2":
            # Se consulta antes de atender para dejar el dato en el historial.
            primera = solicitudes.solicitudes.consultar_primero()
            solicitudes.atender_siguiente()
            if primera is not None:
                historial.registrar_accion(f"Solicitud atendida: turno {primera['turno']}, {primera['nombre']}")

        elif opcion == "3":
            solicitudes.consultar_primera()

        elif opcion == "4":
            solicitudes.mostrar_pendientes()

        elif opcion == "5":
            solicitudes.contar_pendientes()
            print("Conteo recursivo:", contar_solicitudes(solicitudes.solicitudes))

        elif opcion == "0":
            break

        else:
            print("Opción inválida. Intente de nuevo.")