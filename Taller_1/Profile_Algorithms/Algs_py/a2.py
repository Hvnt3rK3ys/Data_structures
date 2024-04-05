# Importamos el módulo memory_profiler para analizar el uso de memoria
from memory_profiler import profile

# Decoramos la función con @profile para analizar su uso de memoria
@profile
def mi_algoritmo(n):
    """
    Esta función genera una lista de pares a partir de un rango dado.

    Args:
        n (int): El rango para generar la lista de pares.

    Returns:
        list: Una lista de tuplas que representan los pares.
    """
    # Creamos una lista con el rango proporcionado
    lista = list(range(n))
    # Inicializamos una lista vacía para almacenar los pares
    pares = []
    # Iteramos sobre cada elemento en la lista
    for i in lista:
        # Para cada elemento, iteramos nuevamente sobre la lista
        for j in lista:
            # Añadimos el par (i, j) a la lista de pares
            pares.append((i, j))
    # Devolvemos la lista de pares
    return pares

# Verificamos si este script se está ejecutando como el principal
if __name__ == "__main__":
    # Llamamos a la función mi_algoritmo con 1000 como argumento
    mi_algoritmo(1000)
