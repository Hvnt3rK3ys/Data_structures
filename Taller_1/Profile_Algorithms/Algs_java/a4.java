/*

Big O = ( O(log n) ), donde ( n ) es el número de elementos en el array.
Esto sucede por que en cada iteración del bucle while, el tamaño del segmento de array que se está buscando se reduce a la mitad.
Implica que el número de veces que se ejecuta el bucle (es decir, el número de divisiones que se pueden hacer hasta que el segmento de array se reduzca a un solo elemento)
es logarítmico en relación con el tamaño del array.

 */


public class a4 {
    // Método principal que se ejecuta al iniciar el programa.
    public static void main(String[] args) {
        // Definimos un array de enteros.
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        // Definimos el elemento que queremos buscar en el array.
        int elementoBuscado = 7;
        // Llamamos al método 'busqueda' con el array y el elemento buscado como argumentos.
        // Guardamos el resultado en la variable 'indice'.
        int indice = busqueda(arr, elementoBuscado);
        // Imprimimos el índice del elemento buscado.
        System.out.println("El índice del elemento buscado es: " + indice);
    }

    // Método 'busqueda' que toma un array de enteros y un entero 'elementoBuscado' como argumentos.
    // Este método realiza una búsqueda binaria en el array para encontrar el 'elementoBuscado'.
    public static int busqueda(int[] arr, int elementoBuscado) {

        // Inicializamos los índices de los extremos del array.
        int izquierda = 0, derecha = arr.length - 1;

        // Mientras el índice izquierdo sea menor o igual al derecho.
        while (izquierda <= derecha) {
            // Calculamos el índice del medio.
            int medio = (izquierda + derecha) / 2;
            // Obtenemos el valor del medio.
            int medioValor = arr[medio];

            // Si el valor del medio es igual al elemento buscado, lo retornamos.
            if (medioValor == elementoBuscado) {
                return medio;
            }
            // Si el elemento buscado es menor que el valor del medio, movemos el índice derecho.
            else if (elementoBuscado < medioValor) {
                derecha = medio - 1;
            }
            // Si el elemento buscado es mayor que el valor del medio, movemos el índice izquierdo.
            else {
                izquierda = medio + 1;
            }
        }
        // Si no encontramos el elemento, retornamos -1.
        return -1;
    }
}