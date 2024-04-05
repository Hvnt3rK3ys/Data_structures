# Importamos el módulo memory_profiler para analizar el uso de memoria
from memory_profiler import profile

# Definimos la función de búsqueda binaria
def busqueda(arr, elemento_buscado):
    """
    Esta función realiza una búsqueda binaria en un array ordenado.

    Args:
        arr (list): El array en el que buscar.
        elemento_buscado (int): El elemento a buscar.

    Returns:
        int: El índice del elemento buscado en el array, o -1 si no se encuentra.
    """
    # Inicializamos los índices de los extremos del array
    izquierda, derecha = 0, len(arr) - 1

    # Mientras el índice izquierdo sea menor o igual al derecho
    while izquierda <= derecha:
        # Calculamos el índice del medio
        medio = (izquierda + derecha) // 2
        # Obtenemos el valor del medio
        medio_valor = arr[medio]

        # Si el valor del medio es igual al elemento buscado, lo retornamos
        if medio_valor == elemento_buscado:
            return medio
        # Si el elemento buscado es menor que el valor del medio, movemos el índice derecho
        elif elemento_buscado < medio_valor:
            derecha = medio - 1
        # Si el elemento buscado es mayor que el valor del medio, movemos el índice izquierdo
        else:
            izquierda = medio + 1
    # Si no encontramos el elemento, retornamos -1
    return -1

# Verificamos si este script se está ejecutando como el principal
if __name__ == "__main__":
    # Realizamos una búsqueda en un array y almacenamos el resultado en la variable índice
    indice = busqueda([1, 2, 3, 4, 5, 6, 7, 8, 9], 7)