/**
 *  Matrix multiplication utility class.
 * Given two matrices A and B, computes their product C = A * B using serial computation.
 * @author @traceyomphile
 * Date: 29 November 2025
 */

package MatrixMultiplication.Java;

import java.time.Duration;
import java.time.Instant;
import java.util.Random;

public class MatrixMultSerial {
    private final double[][] matrixA;
    private final double[][] matrixB;
    private final double[][] result;

    public MatrixMultSerial(double[][] A, double[][] B) {
        this.matrixA = A;
        this.matrixB = B;
        this.result = new double[A.length][B[0].length];
    }

    /**
     * Performs matrix multiplication using the dot product method.
     * Stores the result in the 'result' matrix.
     */
    private void dotProduct() {
        int columnsB = this.matrixB[0].length;
        int sharedDim = this.matrixA[0].length;

        for (int i = 0; i < this.matrixA.length; i++) {
            for (int j = 0; j < columnsB; j++) {
                double sum = 0;
                for (int k = 0; k < sharedDim; k++) {
                    sum += (this.matrixA[i][k] * this.matrixB[k][j]);
                } this.result[i][j] = sum;
            }
        }
    }

    /**
     * Static method to multiply two matrices A and B.
     * @param A First matrix.
     * @param B Second matrix.
     * @return The resulting matrix after multiplication.
     */
    public static double[][] multiply(double[][] A, double[][] B) {
        if (A[0].length != B.length) {
            throw new IllegalArgumentException("Incompatible matrix dimensions!");
        }

        MatrixMultSerial task = new MatrixMultSerial(A, B);
        task.dotProduct();
        return task.result;
    }

    /**
     * Randomly initialise a given matrix
     * @param matrix: Represents any matrix
     * @return The randomly initialised matrix
     */
    private static double[][] randomInit(double[][] matrix) {
        Random rand = new Random();

        for (double[] matrix1 : matrix) {
            for (int j = 0; j < matrix[0].length; j++) {
                matrix1[j] = rand.nextDouble();
            }
        }
        return matrix;
    }

    // Example usage
    public static void main(String[] args) {
        double[][] A = new double[50][40];
        double[][] B = new double[40][50];

        A = randomInit(A);
        B = randomInit(B);

        Instant start = Instant.now();
        double[][] C = MatrixMultSerial.multiply(A, B);
        Instant end = Instant.now();

        Duration timeElapsed = Duration.between(start, end);

        // Print the result
        for (double[] row : C) {
            for (double val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }

        System.out.println("Time taken (serial): " + timeElapsed.toMillis() + " ms.");
    }
}