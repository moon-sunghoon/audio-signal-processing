from dataclasses import dataclass


@dataclass
class TransferFunction:
    """
    A class to represent a transfer function in z domain, H(z) = B(z) / A(z).

    Attributes
    ----------
    numerator : list
        Coefficients of the numerator polynomial.
    denominator : list
        Coefficients of the denominator polynomial.
    """

    numerator: list[int | float | None]
    denominator: list[int | float]

    def __post_init__(self):
        if not isinstance(self.numerator, list) or not isinstance(
            self.denominator, list
        ):
            raise TypeError("Numerator and denominator must be lists of coefficients.")
        if len(self.denominator) == 0:
            raise ValueError("Denominator cannot be empty.")
        if not all(isinstance(coef, (int, float)) for coef in self.numerator):
            raise ValueError(
                "All elements in the numerator must be integers or floats."
            )
        if not all(isinstance(coef, (int, float)) for coef in self.denominator):
            raise ValueError(
                "All elements in the denominator must be integers or floats."
            )
