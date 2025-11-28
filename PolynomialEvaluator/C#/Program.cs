/*
 * C# program that evaluates a polynomial at multiple x-values in parallel.
 * @uthor: Tracey Letlape
 * @Date: 2025-11-28
 */

using System;

/** Example use! 
     * Main method to run the polynomial evaluator.
     * Reads polynomial coefficients and x-values from user input.
     */
internal class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("Enter polynomial coefficients (from highest degree to constant term), separated by spaces:");
        string input = Console.ReadLine();

        while (string.IsNullOrWhiteSpace(input))
        {
            Console.WriteLine("Enter a non-empty set of polynomial coefficients:");
            input = Console.ReadLine();
        }

        string[] temp = input.Split(' ');
        double[] coeffs;

        try
        {
            coeffs = ConvertToDoubleArray(temp);
        }
        catch (FormatException e)
        {
            Console.WriteLine(e.Message);
            return;
        }

        Console.WriteLine("Enter x-values to evaluate the polynomial at, separated by spaces:");
        input = Console.ReadLine();

        while (string.IsNullOrWhiteSpace(input))
        {
            Console.WriteLine("Enter a non-empty set of x-values:");
            input = Console.ReadLine();
        }

        temp = input.Split(' ');
        double[] xValues;

        try
        {
            xValues = ConvertToDoubleArray(temp);
        }
        catch (FormatException e)
        {
            Console.WriteLine(e.Message);
            return;
        }

        PolynomialEvaluator polEvaluator = new PolynomialEvaluator(coeffs, xValues);
        polEvaluator.EvaluatePolynomial();

        double[] results = polEvaluator.Y_Values;

        for (int i = 0; i < xValues.Length; i++)
        {
            Console.WriteLine($"f({xValues[i]}) = {results[i]}");
        }
    }
}