"""
Compute f(x) of the given x values with the given polynomial coefficients
@traceyomphile
Date: 28 November 2025
"""

import multiprocessing
from multiprocessing import Manager
import os


class PolynomialEvaluator:
    def __init__(self, pol_coeffs: list[float], x_values: list[float]):
        self._pol_coeffs: list[float] = pol_coeffs
        self._x_values: list[float] = x_values

    @staticmethod
    def _eval(x: float, pol_coeffs: list[float], results: dict) -> None:
        if x in results:
            return
        
        length = len(pol_coeffs)
        res = 0
        for i in range(length):
            res += pol_coeffs[i] * (x ** (length - 1 - i))
        results[x] = res

    def main(self) -> dict:
        
        with Manager() as manager:
            shared_results = manager.dict()

            with multiprocessing.Pool(processes=os.cpu_count()) as pool:
                eval_args = [(x, self._pol_coeffs, shared_results) for x in self._x_values]
                pool.starmap(PolynomialEvaluator._eval, eval_args)
            return dict(shared_results)
    
def _convert_to_float_list(input: list[str]) -> list[float]:
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

    polEvaluator = PolynomialEvaluator(coeffs, x_values)
    final_res = polEvaluator.main()

    if not final_res:
        print("Result dictionary is empty!!")
    else:
        print()
        for x in final_res:
            print(f"f({x}) = {final_res[x]}")

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()

        
