# Guía breve para la defensa oral — Fase 1

## 1. Vector de estudiantes

`self.estudiantes = []` crea un vector usando una lista de Python. Cada posición contiene un objeto `Estudiante`.

## 2. Búsqueda lineal

El método `buscar` recorre el vector desde el primer elemento. Compara el código de cada estudiante con el código solicitado. Si coincide, devuelve el estudiante; si termina el recorrido, devuelve `None`.

Complejidad: O(n) en el peor caso.

## 3. Matriz de notas

La matriz tiene una fila por estudiante y una columna por asignatura. `None` significa que todavía no se ha registrado una nota en esa casilla.

## 4. Promedio

Se suman únicamente las notas que no sean `None`. La suma se divide por la cantidad de notas ingresadas. Si no hay notas, el método devuelve `None` para evitar dividir entre cero.

## 5. Ordenamiento burbuja

Se comparan nombres vecinos. Si están en orden incorrecto, se intercambian. Cada pasada deja uno de los nombres mayores hacia el final.

Complejidad: O(n²) en el promedio y peor caso.

## 6. Validaciones

- No se permiten códigos vacíos ni repetidos.
- El nombre no puede quedar vacío.
- La edad debe ser mayor que cero.
- Las notas deben estar entre 0.0 y 5.0.

## 7. Limitación actual

Los datos solo existen en memoria mientras el programa está ejecutándose. No hay base de datos ni archivos de persistencia en esta fase.
