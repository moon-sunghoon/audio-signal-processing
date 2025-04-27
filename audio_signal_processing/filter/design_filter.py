import numpy as np


def get_filter_coefficients(
    zeros: complex, poles: complex
) -> tuple[list[float], list[float]]:
    b = np.poly(zeros)
    a = np.poly(poles)
    return a, b
