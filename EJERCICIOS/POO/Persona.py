"""
¿En qué consiste la Programación Orientada a Objetos?
- En trasladar la naturaleza de los objetos de la vida real a código
de programación (en algún lenguaje de programación, como Python).

Los objetos de la realidad tienen características (atributos o propiedades)
y funcionalidades o comportamientos (funciones o métodos).

Ventajas:
- Modularización (división en pequeñas partes) de un programa completo.
- Código fuente muy reutilizable.
- Código fuente más fácil de incrementar en el futuro y mantener.
- Si existe un fallo en una pequeña parte del código el programa completo
no debe fallar necesariamente. Además, es más fácil de corregir esos fallos.
- Encapsulamiento: Ocultamiento del funcionamiento interno de un objeto.
"""


class Persona():
    # Propiedades, características o atributos:
    apellidos = ""
    nombres = ""
    edad = 0
    despierta = False

    # Funcionalidades:
    def despertar(self):
        # self: Parámetro que hace referencia a la instancia perteneciente a la clase.
        self.despierta = True
        print("Buen día.")


