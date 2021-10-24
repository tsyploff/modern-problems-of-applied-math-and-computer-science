class CauchyProblem:
    """Gives the Cauchy problem defined by

    y'(x) = f(x, y)
    y(x_0) = y_0

    """
    def __init__(self, function, arg: float, value: float):
        self.function = function
        self.arg = arg
        self.value = value

    def __str__(self):
        return f"y'(x) = f(x, y), where f is {self.function}\ny({self.arg}) = {self.value}"

    def derivative(self, arg: float, value: float):
        return self.function(arg, value)
