from modelos.estudiante import Estudiante
from servicios.gestion_estudiantes import GestionEstudiantes
from estructuras.matriz_notas import MatrizNotas


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
            gestion.ordenar_por_nombre()
            print("Estudiantes ordenados alfabéticamente.")
            gestion.mostrar_todos()

        elif opcion == "8":
            print(f"Cantidad de estudiantes: {len(gestion.estudiantes)}")
            print(f"Cantidad de asignaturas en la matriz: {notas.cantidad_asignaturas()}")
            print(f"Cantidad total de notas registradas: {notas.contar_notas()}")

        elif opcion == "0":
            print("Gracias por usar EduCore.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
