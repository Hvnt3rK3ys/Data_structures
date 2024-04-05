/*

Big O total = O(n) + O(1) = O(n)

`operacionIntensivaMemoria`
Big O = O(n), contiene un bucle que se ejecuta 'n' veces, donde 'n' es el tamaño de la lista `granLista`.
Dentro de este bucle, se realiza una operación de tiempo constante (añadir un elemento a la lista), por lo que la complejidad total es O(n).


`operacionIntensivaCPU`
Big O = O(1),  a pesar del tamaño de la entrada, siempre realiza 100 operaciones (el bucle se ejecuta 100 veces).

 */


// Importamos las clases ArrayList y List, y la clase Random de la biblioteca java.util
import java.util.ArrayList;
import java.util.List;
import java.util.Random;



public class a3 {
    // Método principal que se ejecuta al iniciar el programa.
    public static void main(String[] args) throws InterruptedException {
        // Definimos un entero 'n' con el valor de 500000.
        int n = 500000;
        // Bucle for que se ejecuta 5 veces.
        for (int i = 0; i < 5; i++) {
            // Imprimimos en consola el inicio de una operación intensiva en memoria.
            System.out.println("Pico " + (i + 1) + ": Operación intensiva en memoria");
            // Llamamos al método 'operacionIntensivaMemoria' con 'n' como argumento.
            operacionIntensivaMemoria(n);
            // Imprimimos en consola el inicio de una operación intensiva en CPU.
            System.out.println("Pico " + (i + 1) + ": Operación intensiva en CPU");
            // Llamamos al método 'operacionIntensivaCPU' con 100 como argumento.
            operacionIntensivaCPU(100);
        }
    }

    // Método 'operacionIntensivaMemoria' que toma un entero 'n' como argumento y devuelve un double.
    // Este método simula una operación intensiva en memoria.
    public static double operacionIntensivaMemoria(int n) throws InterruptedException {
        // Creamos un objeto 'rand' de la clase Random.
        Random rand = new Random();
        // Creamos una lista de Doubles.
        List<Double> granLista = new ArrayList<>();
        // Bucle for que se ejecuta 'n' veces.
        for (int i = 0; i < n; i++) {
            // Añadimos un número double aleatorio a 'granLista'.
            granLista.add(rand.nextDouble());
        }
        // Hacemos que el hilo actual se duerma durante 1000 milisegundos.
        Thread.sleep(1000);
        // Devolvemos la suma de todos los elementos en 'granLista'.
        return granLista.stream().mapToDouble(Double::doubleValue).sum();
    }

    // Método 'operacionIntensivaCPU' que toma un entero 'n' como argumento.
    // Este método simula una operación intensiva en CPU.
    public static void operacionIntensivaCPU(int n) throws InterruptedException {
        // Creamos un objeto 'rand' de la clase Random.
        Random rand = new Random();
        // Creamos un contador y lo inicializamos en 0.
        double contador = 0;
        // Bucle for que se ejecuta 'n' veces.
        for (int i = 0; i < n; i++) {
            // Añadimos un número double aleatorio al contador.
            contador += rand.nextDouble();
        }
        // Hacemos que el hilo actual se duerma durante 10 milisegundos.
        Thread.sleep(10);
    }
}