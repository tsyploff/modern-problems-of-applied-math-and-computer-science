from typing import List, Tuple
from .cauchy_problem import CauchyProblem


class RungeKutta:
    def __init__(self, h):
        self.h = h

    def __str__(self):
        return f"RungeKutta(h={self.h})"

    def solve(self, cauchy_problem: CauchyProblem, period: float) -> Tuple[List[float], List[float]]:
        args = [cauchy_problem.arg]
        values = [cauchy_problem.value]
        for _ in range(round(period / self.h)):
            k_1 = cauchy_problem.derivative(args[-1], values[-1])
            k_2 = cauchy_problem.derivative(args[-1] + self.h / 2, values[-1] + self.h * k_1 / 2)
            k_3 = cauchy_problem.derivative(args[-1] + self.h / 2, values[-1] + self.h * k_2 / 2)
            k_4 = cauchy_problem.derivative(args[-1] + self.h, values[-1] + self.h * k_3)
            args.append(args[-1] + self.h)
            values.append(values[-1] + self.h * (k_1 + 2*k_1+2*k_3+k_4) / 6)
        return args, values
