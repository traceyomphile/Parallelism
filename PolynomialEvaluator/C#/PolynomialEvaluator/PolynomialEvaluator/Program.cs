try
{
    Console.WriteLine("Enter polynomial coefficients (from highest degree to constant term), separated by spaces:");
    string? input = Console.ReadLine();

    while (string.IsNullOrWhiteSpace(input))
    {
        Console.WriteLine("Enter a non-empty set of polynomial coefficients:");
        input = Console.ReadLine();
    }

    string[] temp = input!.Split(' ');
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

    temp = input!.Split(' ');
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
catch (Exception e)
{
    Console.WriteLine(e.Message);
}


/** Converts an array of strings to an array of doubles.
     * Throws FormatException if any string cannot be converted.
     */
static double[] ConvertToDoubleArray(string[] input)
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