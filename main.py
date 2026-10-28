from modelos.estudiante import Estudiante
from servicios.gestion_estudiantes import GestionEstudiantes
from estructuras.matriz_notas import MatrizNotas
from servicios.gestion_historial import GestionHistorial


def mostrar_menu():
    print("\n========== EDUCORE: GESTIÓN ESCOLAR ==========")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Registrar nota")
    print("5. Mostrar matriz de notas")
    print("6. Calcular promedio de un estudiante")
    print("7. Ordenar estudiantes por nombre")
    print("8. Mostrar estadísticas básicas")
    print("9. Eliminar estudiante")
    print("10. Ver historial de acciones")
    print("11. Consultar la última acción")
    print("12. Retirar la última acción")
    print("0. Salir")


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada inválida. Escriba un número entero.")


def buscar_posicion_estudiante(gestion):
    codigo = input("Código del estudiante: ").strip()
    estudiante = gestion.buscar(codigo)
    if estudiante is None:
        print("No se encontró un estudiante con ese código.")
        return None
    return gestion.estudiantes.index(estudiante)

def elegir_posicion():
    print("¿Dónde desea registrar al estudiante?")
    print("1. Al inicio de la lista")
    print("2. Al final de la lista")
    while True:
        opcion = input("Seleccione 1 o 2: ").strip()
        if opcion == "1":
            return True
        if opcion == "2":
            return False
        print("Opción inválida. Escriba 1 o 2.")


def main():
    gestion = GestionEstudiantes()
    notas = MatrizNotas()
    historial = GestionHistorial()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            al_inicio = elegir_posicion()
            codigo = input("Código: ").strip()
            nombre = input("Nombre completo: ").strip()
            edad = leer_entero("Edad: ")
            programa = input("Programa académico: ").strip()

            estudiante = Estudiante(codigo, nombre, edad, programa)
            if gestion.registrar(estudiante, al_inicio):
                if al_inicio:
                    notas.agregar_estudiante_al_inicio()
                else:
                    notas.agregar_estudiante()
                historial.registrar_accion(f"Registro del estudiante {codigo} - {nombre}")
                print("Estudiante registrado correctamente.")
            else:
                print("No se pudo registrar. Revise que el código no esté repetido y los datos sean válidos.")
        elif opcion == "2":
            gestion.mostrar_todos()

        elif opcion == "3":
            codigo = input("Código del estudiante que desea buscar: ").strip()
            estudiante = gestion.buscar(codigo)
            if estudiante is None:
                print("Estudiante no encontrado.")
            else:
                estudiante.mostrar()

        elif opcion == "4":
            if len(gestion.estudiantes) == 0:
                print("Primero debe registrar al menos un estudiante.")
                continue
            posicion = buscar_posicion_estudiante(gestion)
            if posicion is not None:
                cantidad = notas.cantidad_asignaturas()
                if cantidad == 0:
                    cantidad = leer_entero("¿Cuántas asignaturas desea registrar en la matriz? ")
                    if cantidad <= 0:
                        print("La cantidad debe ser mayor que cero.")
                        continue
                    notas.definir_asignaturas(cantidad)
                asignatura = leer_entero(f"Posición de la asignatura (1 a {notas.cantidad_asignaturas()}): ")
                if asignatura < 1 or asignatura > notas.cantidad_asignaturas():
                    print("Posición de asignatura inválida.")
                    continue
                try:
                    nota = float(input("Nota (0.0 a 5.0): "))
                except ValueError:
                    print("La nota debe ser numérica.")
                    continue
                if notas.registrar_nota(posicion, asignatura - 1, nota):
                    historial.registrar_accion(f"Nota {nota} registrada a {gestion.estudiantes[posicion].nombre} (asignatura {asignatura})")
                    print("Nota registrada correctamente.")
                else:
                    print("No se pudo registrar la nota. Debe estar entre 0.0 y 5.0.")

        elif opcion == "5":
            notas.mostrar(gestion.estudiantes)

        elif opcion == "6":
            if len(gestion.estudiantes) == 0:
                print("No hay estudiantes registrados.")
                continue
            posicion = buscar_posicion_estudiante(gestion)
            if posicion is not None:
                promedio = notas.calcular_promedio(posicion)
                if promedio is None:
                    print("Este estudiante todavía no tiene notas registradas.")
                else:
                    print(f"Promedio de {gestion.estudiantes[posicion].nombre}: {promedio:.2f}")

        elif opcion == "7":
            orden = gestion.ordenar_por_nombre()
            notas.reordenar(orden)
            historial.registrar_accion("Ordenamiento de estudiantes por nombre")
            print("Estudiantes ordenados alfabéticamente.")
            gestion.mostrar_todos()

        elif opcion == "8":
            print(f"Cantidad de estudiantes: {len(gestion.estudiantes)}")
            print(f"Cantidad de asignaturas en la matriz: {notas.cantidad_asignaturas()}")
            print(f"Cantidad total de notas registradas: {notas.contar_notas()}")

        elif opcion == "9":
            if len(gestion.estudiantes) == 0:
                print("No hay estudiantes registrados.")
                continue
            codigo = input("Código del estudiante que desea eliminar: ").strip()
            estudiante = gestion.buscar(codigo)
            if estudiante is None:
                print("Estudiante no encontrado.")
            else:
                posicion = gestion.estudiantes.index(estudiante)
                gestion.eliminar(codigo)
                notas.eliminar_estudiante(posicion)
                historial.registrar_accion(f"Eliminación del estudiante {codigo} - {estudiante.nombre}")
                print("Estudiante eliminado correctamente.")

        elif opcion == "10":
            historial.mostrar_historial()

        elif opcion == "11":
            ultima = historial.consultar_ultima()
            if ultima is None:
                print("No hay acciones registradas.")
            else:
                print(f"Última acción: {ultima}")
                print(f"Acciones en el historial: {historial.cantidad()}")

        elif opcion == "12":
            retirada = historial.retirar_ultima()
            if retirada is None:
                print("No hay acciones para retirar.")
            else:
                print(f"Acción retirada del historial: {retirada}")
                print(f"Acciones restantes: {historial.cantidad()}")

        elif opcion == "0":
            print("Gracias por usar EduCore.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()