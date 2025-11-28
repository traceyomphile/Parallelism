/**
 * Compute f(x) for given x values and given polynomial coefficients
 * @author @traceyomphile
 * Date: 28 November 2011
 */
import java.util.Scanner;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveAction;

public class PolynomialEvaluator extends RecursiveAction {
    private final double[] polCoeffs;
    private final double[] x_values;
    private final double[] res;
    private static double THRESHOLD;
    private int start, end;

    public PolynomialEvaluator(double[] polCoeffs, double[] x_values) {
        this(polCoeffs, x_values, new double[x_values.length], 0, x_values.length, Math.max((x_values.length * 0.10), 1));
    }

    public PolynomialEvaluator(double[] polCoeffs, double[] x_values, double[] res, int start, int end, double threshold) {
        this.polCoeffs = polCoeffs;
        this.x_values = x_values;
        this.res = res;
        this.start = start;
        this.end = end;
        PolynomialEvaluator.THRESHOLD = threshold;
    }

    /**
     * Compute the f(x) for the x values in the given range.
     * @param start: represents the starting index of the range.
     * @param end: represents the ending index of the range.
     */
    public void eval(int start, int end) {
        int len = this.polCoeffs.length;

        for (int i = start; i < end; i++) {
            double result = 0;
            for (int j = 0; j < len; j++) {
                result += (this.polCoeffs[j] * Math.pow(this.x_values[i], (len - 1 - j)));
            } this.res[i] = result; 
        }
    }

    /**
     * Implement the main computation performed by PolynomialEvaluator tasks.
     */
    @Override
    protected void compute() {
        if ((this.end - this.start) <= PolynomialEvaluator.THRESHOLD) {
            eval(this.start, this.end);
        } else {
            int mid = (this.end + this.start) / 2;

            PolynomialEvaluator left = new PolynomialEvaluator(this.polCoeffs, this.x_values, this.res, this.start, mid, PolynomialEvaluator.THRESHOLD);
            PolynomialEvaluator right = new PolynomialEvaluator(this.polCoeffs, this.x_values, this.res, mid, this.end, PolynomialEvaluator.THRESHOLD);

            left.fork();
            right.compute();
            left.join();
        }
    }

    /**
     * Converts a given input array to a double array. Throws NumberFormatException.
     * @param localRes: represents the results array.
     * @param input: represents the input string array.
     * @return double array
     */
    private static double[] convert(double[] localRes, String[] input) {
        localRes = new double[input.length];
        for (int i = 0; i < input.length; i++) {
            try {
                localRes[i] = Double.parseDouble(input[i]);
            } catch (NumberFormatException e) {
                throw new NumberFormatException("Input should consist of real numbers!");
            }
        } return localRes;
    }

    /**
     * Example usage of the PolynomialEvaluator
     * @param args: can be anything.
     */
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {

            System.out.println("Enter a set of polynomial coefficients (space separated):");
            String input = scanner.nextLine();
            while (input.isEmpty()) {
                System.out.println("Enter a non-empty set of polynomial coefficients (space separated):");
                input = scanner.nextLine();
            }

            String[] temp = input.split(" ");
            double[] coeffs = new double[temp.length];
            try {
                coeffs = convert(coeffs, temp);
            } catch (NumberFormatException e) {
                System.err.println(e.getMessage());
                System.exit(0);
            }

            System.out.println("Enter a set of x values to evaluate (space separated):");
            input = scanner.nextLine();
            while (input.isEmpty()) {
                System.out.println("Enter a non-empty set of x values (space separated):");
                input = scanner.nextLine();
            }

            temp = input.split(" ");
            double[] xValues = new double[temp.length];
            try {
                xValues = convert(xValues, temp);
            } catch (NumberFormatException e) {
                System.err.println(e.getMessage());
                System.exit(0);
            }
            
            ForkJoinPool pool = ForkJoinPool.commonPool();
            PolynomialEvaluator polEvaluator = new PolynomialEvaluator(coeffs, xValues);
            pool.invoke(polEvaluator);
            for (int i = 0; i < polEvaluator.res.length; i++) {
                System.out.println("f(" + polEvaluator.x_values[i] + ") = " + polEvaluator.res[i]);
            }
        }
    }
}