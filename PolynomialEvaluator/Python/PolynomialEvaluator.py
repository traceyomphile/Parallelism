"""
Compute f(x) of the given x values with the given polynomial coefficients in parallel
--- IGNORE ---
@traceyomphile
Date: 29 November 2025
"""

import multiprocessing
from multiprocessing import Manager
import os
import time


class PolynomialEvaluator:
    def __init__(self, pol_coeffs: list[float], x_values: list[float]):
        self._pol_coeffs: list[float] = pol_coeffs
        self._x_values: list[float] = x_values

    @staticmethod
    def _eval(x: float, pol_coeffs: list[float], results: dict) -> None:
        """
        Compute f(x) for the given x, and write the result to results dict
        Parameters:
            x: A float representing an x value to be evaluated
            pol_coeffs: A list of floats representing polynomial coefficients
            results: A dictionary storing different f of x_values
        Returns:
            None
        """
        if x in results:
            return
        
        length = len(pol_coeffs)
        res = 0
        for i in range(length):
            res += pol_coeffs[i] * (x ** (length - 1 - i))
        results[x] = res

    def main(self) -> dict:
        """
        Computes the f(x) for different x values in parallel.
        """
        with Manager() as manager:
            shared_results = manager.dict()

            with multiprocessing.Pool(processes=os.cpu_count()) as pool:
                eval_args = [(x, self._pol_coeffs, shared_results) for x in self._x_values]
                pool.starmap(PolynomialEvaluator._eval, eval_args)
            return dict(shared_results)
    
def _convert_to_float_list(input: list[str]) -> list[float]:
    """
    Convert a string list to a float list.
    Parameters:
        input: A list of strings
    Returns:
        A list of floating-point numbers
    """
    res = []
    for i in range(len(input)):
        res.append(float(input[i]))
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

    start_time = time.perf_counter()
    polEvaluator = PolynomialEvaluator(coeffs, x_values)
    final_res = polEvaluator.main()
    end_time = time.perf_counter()

    if not final_res:
        print("Result dictionary is empty!!")
    else:
        print()
        for x in final_res:
            print(f"f({x}) = {final_res[x]}")
    print(f"\nTime taken (in seconds): {end_time - start_time:.4f}")

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()

        
