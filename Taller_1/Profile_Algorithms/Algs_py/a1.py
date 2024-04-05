# Importamos el módulo memory_profiler para analizar el uso de memoria
from memory_profiler import profile

# Decoramos la función con @profile para analizar su uso de memoria
@profile
def imprimir(lista):
    """
    Esta función imprime la lista proporcionada.

    Big O = O(1), Esto se debe a que a pesar del tamaño de la lista,
    la función solo realiza una operación: imprimir la lista

    Args:
        lista (list): La lista a imprimir.

    Returns:
        None
    """
    # Asignamos la lista a la variable n
    n = lista
    # Imprimimos la lista
    print(lista)

# Verificamos si este script se está ejecutando como el principal
if "__main__" == __name__:
    # Creamos una lista
    lista = 2
    # Llamamos a la función imprimir con la lista como argumento
    imprimir(lista)
