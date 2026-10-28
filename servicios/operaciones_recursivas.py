def contar_solicitudes(cola):
    # Arranca en el primer nodo real (el que está después del centinela de inicio).
    return _contar_desde(cola.cabeza.siguiente, cola.cola)


def _contar_desde(nodo, centinela_final):
    # CASO BASE: llegamos al centinela final, ya no quedan solicitudes.
    if nodo is centinela_final:
        return 0

    # LLAMADA RECURSIVA: cuenta este nodo (1) y deja el resto del problema
    # al siguiente nodo, que es una cola más corta.
    return 1 + _contar_desde(nodo.siguiente, centinela_final)