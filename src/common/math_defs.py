from typing import Callable
import numpy as np

DEFAULT_A: float = 1.0
DEFAULT_B: float = 2.0
DEFAULT_F_FORMULA: str = "f(x) = 3x^2"
DEFAULT_ANTIDERIV_FORMULA: str = "F(x) = x^3"
DEFAULT_EXACT_AREA: float = 7.0

def func_main(x: float | np.ndarray) -> float | np.ndarray:
    return 3.0 * (x ** 2)

def antideriv_main(x: float | np.ndarray) -> float | np.ndarray:
    return x ** 3

def antideriv_with_c(x: float | np.ndarray, c: float = 5.0) -> float | np.ndarray:
    return (x ** 3) + c

def accumulation_func(x: float | np.ndarray, a: float = DEFAULT_A) -> float | np.ndarray:
    return (x ** 3) - (a ** 3)

def riemann_sum_left(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    dx = (b - a) / n
    return sum(f(a + i * dx) * dx for i in range(n))

def riemann_sum_right(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    dx = (b - a) / n
    return sum(f(a + (i + 1) * dx) * dx for i in range(n))

def riemann_sum_midpoint(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    dx = (b - a) / n
    return sum(f(a + (i + 0.5) * dx) * dx for i in range(n))

