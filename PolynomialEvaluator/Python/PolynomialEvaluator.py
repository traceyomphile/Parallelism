"""
Compute f(x) of the given x values with the given polynomial coefficients
@traceyomphile
Date: 28 November 2025
"""

import multiprocessing
import os


class PolynomialEvaluator:
    def __init__(self, pol_coeffs: list[float], x_values: list[float]):
        self._pol_coeffs: list[float] = pol_coeffs
        self._x_values: list[float] = x_values
        self._results: dict = None

    def _eval(self, x: float) -> None:
        if x in self._results:
            return
        len = len(self._pol_coeffs)
        res = 0
        for i in range(len):
            res += self._pol_coeffs[i] * (x ** (len - 1 - i))
        self._results[x] = res

    def main(self) -> dict:
        with multiprocessing.Pool(processes=os.cpu_count()) as pool:
            pool.map(self._eval, self._x_values)
        return self._results
    
def _convert_to_float_list(input: list[str]) -> list[float]:
    res = []
    for i in range(len(input)):
        res[i] = float(input[i])
    return res

def main():
    """Example usage"""
    user_in = input("Enter a set of polynomial coefficients (space separated):\n")
    while not user_in:
        user_in = input("Enter a non-empty set of polynomial coefficients (space separated):\n")
    
    coeffs = _convert_to_float_list(user_in.split())

    user_in = input("Enter a set of x values to evaluate (space separated):\n")
    while not user_in:
        user_in = input("Enter a non-empty set of x values to evaluate (space separated):\n")

    x_values = _convert_to_float_list(user_in.split())

    polEvaluator = PolynomialEvaluator(coeffs, x_values)
    results:dict = polEvaluator.main()

    for x in results:
        print(f"f({x}) = {results[x]}")

        
