# Importamos el módulo memory_profiler para analizar el uso de memoria
from memory_profiler import profile

def generar_subconjuntos(conjunto):
    """
    Esta función genera todos los subconjuntos posibles de un conjunto dado.

    Args:
        conjunto (list): El conjunto original.

    Returns:
        list: Una lista de todos los subconjuntos posibles.
    """
    # Inicializamos con el conjunto vacío
    subconjuntos = [[]]

    # Iteramos sobre cada elemento en el conjunto original
    for elemento in conjunto:
        nuevos_subconjuntos = []

        # Iteramos sobre cada subconjunto existente
        for subconjunto in subconjuntos:
            # Creamos una copia del subconjunto actual
            nuevo_subconjunto = subconjunto[:]
            # Agregamos el elemento actual al nuevo subconjunto
            nuevo_subconjunto.append(elemento)
            # Agregamos el nuevo subconjunto a la lista de nuevos subconjuntos
            nuevos_subconjuntos.append(nuevo_subconjunto)

        # Agregamos todos los nuevos subconjuntos a la lista de subconjuntos
        subconjuntos.extend(nuevos_subconjuntos)

    # Retornamos la lista de todos los subconjuntos posibles
    return subconjuntos

# Verificamos si este script se está ejecutando como el principal
if __name__ == "__main__":
    # Definimos un conjunto
    conjunto = [1, 2, 3]
    # Generamos y almacenamos todos los subconjuntos posibles de nuestro conjunto
    subconjuntos = generar_subconjuntos(conjunto)
    # Imprimimos los subconjuntos generados
    print("Subconjuntos:", subconjuntos)