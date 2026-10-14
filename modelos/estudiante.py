class Estudiante:
    def __init__(self, codigo, nombre, edad, programa):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad
        self.programa = programa

    def mostrar(self):
        print("----------------------------------------")
        print("Código:", self.codigo)
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Programa:", self.programa)

    def __str__(self):
        return f"{self.codigo} | {self.nombre} | {self.edad} años | {self.programa}"
