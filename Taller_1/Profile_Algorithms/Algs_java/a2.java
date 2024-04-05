/*

Big O = O(n^2), donde n es el número de elementos en la lista.
Ell código contiene dos bucles anidados que iteran sobre la lista. En el peor de los casos, para cada elemento en la lista, el código itera sobre todos los elementos de la lista una vez más.
Esto da como resultado una complejidad de tiempo de O(n^2).

 */



// Importamos la clase ArrayList y la interfaz List de la biblioteca java.util
import java.util.ArrayList;
import java.util.List;





public class a2 {
    public static void main(String[] args) {
        // Creamos una lista de pares utilizando el método 'miAlgoritmo' con 1000 como argumento.
        List<Pair> pairs = miAlgoritmo(1000);
        // Iteramos sobre cada par en la lista de pares.
        for (Pair pair : pairs) {
            // Imprimimos cada par en la consola.
            System.out.println(pair);
        }
    }

    // Método 'miAlgoritmo' que toma un entero 'n' como argumento y devuelve una lista de pares.
    public static List<Pair> miAlgoritmo(int n) {
        // Creamos una lista de enteros.
        List<Integer> lista = new ArrayList<>();
        // Llenamos la lista con enteros desde 0 hasta 'n'.
        for (int i = 0; i < n; i++) {
            lista.add(i);
        }

        // Creamos una lista de pares.
        List<Pair> pares = new ArrayList<>();
        // Iteramos sobre cada entero 'i' en la lista.
        for (int i : lista) {
            // Iteramos sobre cada entero 'j' en la lista.
            for (int j : lista) {
                // Añadimos un nuevo par con 'i' y 'j' a la lista de pares.
                pares.add(new Pair(i, j));
            }
        }

        // Devolvemos la lista de pares.
        return pares;
    }
}

// Declaración de la clase 'Pair'.
class Pair {
    // Variables privadas 'first' y 'second' para almacenar los dos enteros de un par.
    private int first;
    private int second;

    // Constructor de la clase 'Pair' que toma dos enteros como argumentos.
    public Pair(int first, int second) {
        // Asignamos los argumentos a las variables de la clase.
        this.first = first;
        this.second = second;
    }

    // Sobrescribimos el método 'toString' para imprimir el par en un formato específico.
    @Override
    public String toString() {
        // Devolvemos una cadena de caracteres con el formato "(first, second)".
        return "(" + first + ", " + second + ")";
    }
}