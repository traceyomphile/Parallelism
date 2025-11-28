/*
 * C# program that evaluates a polynomial at multiple x-values in parallel.
 * @uthor: Tracey Letlape
 * @Date: 2025-11-28
 */

using System;
using System.Threading.Tasks;

public class PolynomialEvaluator
{
    private readonly double[] polCoeffs;
    private readonly double[] x_values;
    private double[] y_values;

    public double[] Y_Values { get { return y_values; } }

    public PolynomialEvaluator(double[] coefficients, double[] xValues)
    {
        this.polCoeffs = coefficients;
        this.x_values = xValues;
        this.y_values = new double[xValues.Length];
    }

    /** Evaluates the polynomial at each x-value in parallel.
     * The results are stored in the y_values array.
     * The method assumes polynomial coefficients are ordered from highest degree to constant term.
     */
    public void EvaluatePolynomial()
    {
        int powerCount = this.polCoeffs.Length;
        Parallel.For(0, this.x_values.Length, i =>
        {
            double x = this.x_values[i];
            double result = 0;
            for (int j = 0; j < powerCount; j++)
            {
                result += this.polCoeffs[j] * Math.Pow(x, powerCount - j - 1);
            }
            this.y_values[i] = result;
        });
    }

    /** Converts an array of strings to an array of doubles.
     * Throws FormatException if any string cannot be converted.
     */
    private static double[] ConvertToDoubleArray(string[] input)
    {
        double[] result = new double[input.Length];

        for (int i = 0; i < input.Length; i++)
        {
            if (!double.TryParse(input[i], out result[i]))
            {
                throw new FormatException($"Input should consist of real numbers!");
            }
        }
        return result;
    }
}
