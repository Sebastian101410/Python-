"""
Ejemplo de estructura de datos tipo ARBOL aplicado a un caso real:
Organigrama jerarquico de una empresa.

Permite:
- Construir el organigrama (arbol).
- Mostrarlo con sangria segun el nivel jerarquico.
- Buscar un empleado por nombre (recorrido recursivo).
- Contar cuantas personas hay bajo un gerente (incluyendolo).
"""


class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
        self.subordinados = []  # hijos del nodo

    def agregar_subordinado(self, empleado):
        self.subordinados.append(empleado)

    def buscar(self, nombre_buscado):
        """Busca un empleado por nombre en todo el arbol (recursivo)."""
        if self.nombre == nombre_buscado:
            return self
        for sub in self.subordinados:
            resultado = sub.buscar(nombre_buscado)
            if resultado:
                return resultado
        return None

    def mostrar(self, nivel=0):
        """Imprime el arbol jerarquico con sangria segun el nivel."""
        print("    " * nivel + f"- {self.nombre} ({self.cargo})")
        for sub in self.subordinados:
            sub.mostrar(nivel + 1)

    def contar_empleados(self):
        """Cuenta cuantas personas hay bajo este nodo (incluyendolo)."""
        total = 1
        for sub in self.subordinados:
            total += sub.contar_empleados()
        return total


def main():
    # --- Caso real: estructura de una empresa ---
    gerente_general = Empleado("Ana Torres", "Gerente General")

    gerente_ventas = Empleado("Carlos Ruiz", "Gerente de Ventas")
    gerente_ti = Empleado("Laura Gomez", "Gerente de TI")

    vendedor1 = Empleado("Pedro Sanchez", "Vendedor")
    vendedor2 = Empleado("Maria Lopez", "Vendedora")

    desarrollador1 = Empleado("Juan Perez", "Desarrollador")
    desarrollador2 = Empleado("Sofia Diaz", "Desarrolladora")

    gerente_general.agregar_subordinado(gerente_ventas)
    gerente_general.agregar_subordinado(gerente_ti)

    gerente_ventas.agregar_subordinado(vendedor1)
    gerente_ventas.agregar_subordinado(vendedor2)

    gerente_ti.agregar_subordinado(desarrollador1)
    gerente_ti.agregar_subordinado(desarrollador2)

    # Mostrar el organigrama completo
    print("Organigrama de la empresa:")
    gerente_general.mostrar()

    # Buscar un empleado especifico
    print("\nBuscando a 'Juan Perez'...")
    resultado = gerente_general.buscar("Juan Perez")
    if resultado:
        print(f"Encontrado: {resultado.nombre} - {resultado.cargo}")
    else:
        print("No encontrado.")

    # Contar empleados totales
    print(f"\nTotal de personas en la empresa: {gerente_general.contar_empleados()}")


if __name__ == "__main__":
    main()
