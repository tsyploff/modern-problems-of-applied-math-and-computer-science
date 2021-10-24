import numpy as np
from .vector_function import VectorFunction


class CauchyProblem:
    """Gives the Cauchy problem defined by

    y'(x) = f(x, y)
    y(x_0) = y_0

    """

    def __init__(self, function: VectorFunction, arg: float, values: np.ndarray):
        self.function = function
        self.arg = arg
        self.values = values

    def __str__(self):
        string = f"y'(x) = f(x, y), where f is {self.function}\n"
        for i in range(len(self.values)):
            string += f"y_{i}({self.arg}) = {self.values[i]}"
        return string

    def derivative(self, arg: float, values: np.ndarray):
        return self.function(arg, values)
