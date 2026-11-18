from modelos.estudiante import Estudiante


def mostrar_menu_arbol():
    print("\n===== ÁRBOL BINARIO DE ESTUDIANTES =====")
    print("1. Insertar estudiante")
    print("2. Buscar estudiante por código")
    print("3. Mostrar cantidad de estudiantes")
    print("0. Volver al menú principal")


def ejecutar_menu_arbol(gestion, gestion_arbol, notas, historial):
    while True:
        mostrar_menu_arbol()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            codigo = input("Código: ").strip()
            nombre = input("Nombre completo: ").strip()
            edad = input("Edad: ").strip()
            programa = input("Programa académico: ").strip()

            if not codigo or not nombre or not edad or not programa:
                print("Todos los datos son obligatorios.")
                continue

            try:
                edad = int(edad)
            except ValueError:
                print("La edad debe ser un número entero.")
                continue
            if edad <= 0:
                print("La edad debe ser mayor que cero.")
                continue

            estudiante = Estudiante(codigo, nombre, edad, programa)
            if gestion.registrar(estudiante):
                gestion_arbol.insertar(estudiante)
                notas.agregar_estudiante()
                historial.registrar_accion(
                    f"Registro del estudiante {codigo} - {nombre}"
                )
                print("Estudiante registrado y insertado en el árbol.")
            else:
                print("Ya existe un estudiante con ese código.")

        elif opcion == "2":
            codigo = input("Código del estudiante: ").strip()
            estudiante = gestion_arbol.buscar(codigo)
            if estudiante is None:
                print("No se encontró un estudiante con ese código.")
            else:
                estudiante.mostrar()

        elif opcion == "3":
            print(f"Estudiantes almacenados en el árbol: {gestion_arbol.arbol.cantidad}")

        elif opcion == "0":
            break

        else:
            print("Opción inválida. Intente de nuevo.")
