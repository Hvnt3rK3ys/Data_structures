/*


Big O =  O(2^n), donde n es el número de elementos en el conjunto.
El código genera todos los subconjuntos posibles de un conjunto dado.
Para un conjunto de tamaño n, hay 2^n posibles subconjuntos (incluyendo el conjunto vacío y el conjunto mismo).

 */





// Importamos las clases ArrayList y List de la biblioteca java.util
import java.util.ArrayList;
import java.util.List;

// Declaración de la clase pública 'a5'.
public class a5 {
    // Método principal que se ejecuta al iniciar el programa.
    public static void main(String[] args) {
        // Creamos una lista de enteros.
        List<Integer> conjunto = List.of(1, 2, 3);
        // Llamamos al método 'generarSubconjuntos' con el conjunto como argumento.
        // Guardamos el resultado en la variable 'subconjuntos'.
        List<List<Integer>> subconjuntos = generarSubconjuntos(conjunto);
        // Imprimimos los subconjuntos en la consola.
        System.out.println("Subconjuntos: " + subconjuntos);
    }

    // Método 'generarSubconjuntos' que toma una lista de enteros 'conjunto' como argumento.
    // Este método genera todos los subconjuntos posibles del conjunto.
    public static List<List<Integer>> generarSubconjuntos(List<Integer> conjunto) {
        // Inicializamos con el conjunto vacío.
        List<List<Integer>> subconjuntos = new ArrayList<>();
        subconjuntos.add(new ArrayList<>());

        // Iteramos sobre cada elemento en el conjunto original.
        for (Integer elemento : conjunto) {
            // Creamos una lista para almacenar los nuevos subconjuntos.
            List<List<Integer>> nuevosSubconjuntos = new ArrayList<>();

            // Iteramos sobre cada subconjunto existente.
            for (List<Integer> subconjunto : subconjuntos) {
                // Creamos una copia del subconjunto actual.
                List<Integer> nuevoSubconjunto = new ArrayList<>(subconjunto);
                // Agregamos el elemento actual al nuevo subconjunto.
                nuevoSubconjunto.add(elemento);
                // Agregamos el nuevo subconjunto a la lista de nuevos subconjuntos.
                nuevosSubconjuntos.add(nuevoSubconjunto);
            }

            // Agregamos todos los nuevos subconjuntos a la lista de subconjuntos.
            subconjuntos.addAll(nuevosSubconjuntos);
        }

        // Retornamos la lista de todos los subconjuntos posibles.
        return subconjuntos;
    }
}