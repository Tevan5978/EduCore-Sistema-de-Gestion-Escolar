from estructuras.grafo import Grafo
from servicios.recorridos_grafo import RecorridosGrafo


def mostrar_menu_grafo():
    print("\n===== DEPENDENCIAS Y RECORRIDOS =====")
    print("1. Mostrar grafo")
    print("2. Agregar dependencia")
    print("3. Conectar dependencias")
    print("4. Recorrido BFS")
    print("5. Recorrido DFS")
    print("6. Salir")
    print("7. Buscar ruta")


def ejecutar_menu_grafo(grafo=None, recorridos=None):
    if grafo is None:
        grafo = Grafo()
        grafo.agregar_dependencia("Porteria")
        grafo.agregar_dependencia("Biblioteca")
        grafo.agregar_dependencia("Salones")
        grafo.agregar_dependencia("Enfermeria")
        grafo.agregar_dependencia("Cafeteria")
        grafo.conectar("Porteria", "Biblioteca")
        grafo.conectar("Porteria", "Salones")
        grafo.conectar("Biblioteca", "Cafeteria")
        grafo.conectar("Salones", "Enfermeria")
    if recorridos is None:
        recorridos = RecorridosGrafo(grafo)

    while True:
        mostrar_menu_grafo()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            grafo.mostrar_grafo()
        elif opcion == "2":
            nombre = input("Nombre de la dependencia: ").strip()
            if nombre:
                grafo.agregar_dependencia(nombre)
            else:
                print("El nombre no puede estar vacío.")
        elif opcion == "3":
            origen = input("Dependencia de origen: ").strip()
            destino = input("Dependencia de destino: ").strip()
            grafo.conectar(origen, destino)
        elif opcion == "4":
            inicio = input("Dependencia inicial: ").strip()
            print(recorridos.bfs(inicio))
        elif opcion == "5":
            inicio = input("Dependencia inicial: ").strip()
            print(recorridos.dfs(inicio))
        elif opcion == "6":
            break
        elif opcion == "7":
            origen = input("Dependencia de origen: ").strip()
            destino = input("Dependencia de destino: ").strip()
            ruta = recorridos.buscar_ruta(origen, destino)
            if ruta is not None:
                print(" -> ".join(ruta))
            else:
                print("No existe una ruta.")
        else:
            print("Opción inválida. Intente de nuevo.")
