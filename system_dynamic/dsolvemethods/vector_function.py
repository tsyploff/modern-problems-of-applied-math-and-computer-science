from typing import List


class VectorFunction:
    def __init__(self, functions):
        """
        Gives the vector-function
        :param functions: list of lambda expressions
        for example

        VectorFunction([lambda x: 6 * x, lambda x: 3 * x**2, lambda x: x**3])
        """
        self.functions = functions
        self.dim = len(functions)

    def __call__(self, *args) -> List[float]:
        return [f(*args) for f in self.functions]
