# EduCore — Sistema de Gestión Escolar

Sistema de gestión escolar desarrollado en Python para apoyar la administración académica y organizativa de un colegio. El proyecto se enfoca en estructuras de datos y algoritmos aplicados a un caso real de gestión estudiantil.

## Descripción

EduCore permite registrar estudiantes, consultar información, registrar notas por asignatura, calcular promedios, ordenar registros y analizar resultados básicos. La versión actual corresponde a la Fase 3 del proyecto.

## Objetivo general

Desarrollar una aplicación funcional en Python para solucionar problemas de gestión escolar mediante estructuras de datos y análisis de complejidad.

## Objetivos específicos

- Gestionar información de estudiantes.
- Registrar y consultar notas por matriz.
- Ordenar estudiantes por nombre o código.
- Calcular promedios por estudiante.
- Mostrar estadísticas básicas del sistema.
- Trabajar con GitHub y buenas prácticas de programación colaborativa.

## Requisitos

- Python 3.10 o superior.
- Visual Studio Code o cualquier editor de Python.
- Git y GitHub para control de versiones.

## Cómo ejecutar

1. Abra la carpeta del proyecto en Visual Studio Code.
2. Abra una terminal en la carpeta del proyecto.
3. Ejecute:

```bash
python main.py
```

En Windows, si `python` no funciona:

```bash
py main.py
```

## Qué incluye esta versión

- Registro de estudiantes en memoria.
- Búsqueda y visualización de estudiantes.
- Registro de notas de 0.0 a 5.0 en una matriz.
- Cálculo de promedio por estudiante.
- Ordenamiento alfabético de estudiantes.
- Estadísticas básicas del sistema.
- Pruebas automáticas con `unittest`.

## Estructura del proyecto

- `main.py`: menú principal de consola.
- `modelos/estudiante.py`: clase `Estudiante`.
- `servicios/gestion_estudiantes.py`: lógica de gestión, búsqueda y ordenamiento.
- `estructuras/matriz_notas.py`: matriz de notas.
- `pruebas/test_fase1.py`: pruebas de la fase 1.
- `docs/`: documentación del proceso y uso de IA.

## Ejecutar pruebas

Desde la carpeta principal:

```bash
python -m unittest discover -s pruebas -v
```

## Complejidad inicial

- Registro de estudiantes: O(1) amortizado.
- Búsqueda por código: O(n).
- Ordenamiento burbuja: O(n²).
- Recorrido de la matriz de notas: O(f × c).

## Trabajo del equipo

Cada integrante debe ejecutar, probar y entender el código. Se recomienda documentar cambios reales, revisiones y cualquier apoyo de IA conforme a las indicaciones del curso.

## Uso de inteligencia artificial

El proyecto hace uso de IA de manera educativa y responsable para apoyar el diseño de soluciones, la revisión de errores y la documentación. Las propuestas generadas fueron revisadas y comprendidas por el equipo antes de incorporarse al proyecto.

## Licencia

Pendiente por definir según las condiciones del curso.
