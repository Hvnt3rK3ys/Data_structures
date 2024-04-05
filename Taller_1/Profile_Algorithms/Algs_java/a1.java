/*

BIg O = O(n), donde n es el número de elementos en el array 'lista'.
El código itera sobre cada elemento del array exactamente una vez.
La operación dentro del bucle, que es imprimir el elemento, se considera una operación de tiempo constante, es decir, O(1).
Por lo tanto, se tiene n elementos en el array, realizarando n operaciones de tiempo constante, lo que resulta en una complejidad de tiempo total de O(n).

 */

public class a1 {
    public class Main {
        public static void main(String[] args) {

            // Declaración e inicialización de un array de enteros llamado 'lista' con un único elemento '2'.
            int[] lista = {2};

            // Llamada al método 'imprimir' con 'lista' como argumento.
            imprimir(lista);
        }

        // Declaración del método 'imprimir' que toma un array de enteros como entrada.
        // @param lista Este es un array de enteros.
        public static void imprimir(int[] lista) {

            // Bucle for que itera sobre cada elemento 'n' en el array 'lista'.
            for (int n : lista) {

                // Se imprime el valor de 'n' en la consola.
                System.out.println(n);
            }
        }
    }
}


