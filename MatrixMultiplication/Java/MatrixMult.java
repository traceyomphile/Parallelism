/**
 * Matrix multiplication using ForkJoin framework for parallelism.
 * Given two matrices A and B, computes their product C = A * B.
 * @author @traceyomphile
 * Date: 29 November 2025
 */

package MatrixMultiplication.Java;

import java.time.Duration;
import java.time.Instant;
import java.util.Random;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveTask;

public class MatrixMult extends RecursiveTask<double[][]> {
    private Integer THRESHOLD;

    private final double[][] matrixA;
    private final double[][] matrixB;
    private final double[][] result;

    private final int rowStart;
    private final int rowEnd;

    public MatrixMult(double[][] A, double[][] B) {
        this(A, B, new double[A.length][B[0].length], 0, A.length, Math.max(1, (int)(A.length * 0.1)));
    }

    public MatrixMult(double[][] A, double[][] B, double[][] res, int rowSt, int rowEnd, int threshold) {
        this.matrixA = A;
        this.matrixB = B;
        this.result = res;
        this.rowStart = rowSt;
        this.rowEnd = rowEnd;
        this.THRESHOLD = threshold;
    }

    /**
     * Computes the matrix multiplication using ForkJoin parallelism.
     * @return The resulting matrix after multiplication.
     */
    @Override
    protected double[][] compute() {
        int nuRows = rowEnd - rowStart;

        // Base case: compute these rows sequentially
        if (nuRows <= THRESHOLD) {
            dotProduct(this.rowStart, this.rowEnd);
            return this.result;
        }

        // Split in half
        int mid = (this.rowStart + rowEnd) / 2;

        MatrixMult left = new MatrixMult(this.matrixA, this.matrixB, this.result, this.rowStart, mid, this.THRESHOLD);
        MatrixMult right = new MatrixMult(this.matrixA, this.matrixB, this.result, mid, this.rowEnd, this.THRESHOLD);
        
        left.fork();
        right.compute();
        left.join();

        return this.result;
    }

    /**
     * Computes the dot product for the specified range of rows.
     * @param start: starting row index (inclusive)
     * @param end: ending row index (exclusive)
     */
    private void dotProduct(int start, int end) {
        int columnsB = this.matrixB[0].length;
        int sharedDim = this.matrixA[0].length;

        for (int i = start; i < end; i++) {
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
     * @param A: first matrix
     * @param B: second matrix
     * @return The resulting matrix after multiplication.
     */
    public static double[][] multiply(double[][] A, double[][] B) {
        if (A[0].length != B.length) {
            throw new IllegalArgumentException("Incompatible matrix dimensions!");
        }

        ForkJoinPool pool = ForkJoinPool.commonPool();
        MatrixMult task = new MatrixMult(A, B);
        return pool.invoke(task);
    }

    /**
     * Randomly initialise a given array
     * @param matrix: Represents any matrix
     * @return The randomly initialised matrix
     */
    private static double[][] randomInit(double[][] matrix) {
        Random rand = new Random();

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                matrix[i][j] = rand.nextDouble();
            }
        } return matrix;
    }

    // Example usage
    public static void main(String[] args) {
        double[][] A = new double[50][40];
        double[][] B = new double[40][50];

        A = randomInit(A);
        B = randomInit(B);

        Instant start = Instant.now();
        double[][] C = MatrixMult.multiply(A, B);
        Instant end = Instant.now();

        Duration timeElapsed = Duration.between(start, end);

        /**
        // Print the result
        for (double[] row : C) {
            for (double val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
        */

        System.out.println("Time take (parallel): " + timeElapsed.toMillis() + " ms.");
    }
}