# Importamos el módulo random para generar números aleatorios
import random
# Importamos el módulo time para trabajar con funciones relacionadas con el tiempo
import time
# Importamos el módulo memory_profiler para analizar el uso de memoria
from memory_profiler import profile

@profile
def operacion_intensiva_memoria(n):
    """
    Esta función genera una gran cantidad de uso de memoria temporalmente.

    Args:
        n (int): El número de elementos en la lista generada.

    Returns:
        float: La suma de los elementos en la lista generada.
    """
    # Generamos una lista grande con números aleatorios
    gran_lista = [random.random() for _ in range(n)]
    time.sleep(1)  # Simulamos un procesamiento
    # Devolvemos la suma de los elementos en la lista
    return sum(gran_lista)

@profile
def operacion_intensiva_cpu(n):
    """
    Esta función consume tiempo de CPU.

    Args:
        n (int): El número de iteraciones para el bucle.

    Returns:
        None
    """
    # Inicializamos un contador
    contador = 0
    # Iteramos n veces
    for _ in range(n):
        # Aumentamos el contador con un número aleatorio
        contador += random.random()
        time.sleep(0.01)  # Añade un pequeño retardo para simular procesamiento

def main():
    """
    Función principal que llama a las funciones operacion_intensiva_memoria y operacion_intensiva_cpu.

    Returns:
        None
    """
    # Definimos el número de elementos para la lista grande
    n = 500000
    # Iteramos 5 veces
    for i in range(5):
        # Imprimimos el pico de operación intensiva en memoria
        print(f"Pico {i+1}: Operación intensiva en memoria")
        # Llamamos a la función operacion_intensiva_memoria
        operacion_intensiva_memoria(n)
        # Imprimimos el pico de operación intensiva en CPU
        print(f"Pico {i+1}: Operación intensiva en CPU")
        # Llamamos a la función operacion_intensiva_cpu
        operacion_intensiva_cpu(100)

# Verificamos si este script se está ejecutando como el principal
if __name__ == "__main__":
    # Llamamos a la función main
    main()