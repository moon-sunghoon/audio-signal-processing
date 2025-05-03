from dataclasses import dataclass
from .filter_interface import FilterInterface


@dataclass
class LowPassFilter(FilterInterface):
    """
    A class representing a low-pass filter.

    Attributes
    ----------
    cutoff_frequency : float
        The cutoff frequency of the filter.
    order : int
        The order of the filter.
    """

    cutoff_frequency: float
    order: int

    def __init__(self, cutoff_frequency: float, order: int):
        super().__init__(enumerator=[1], denominator=[1])
        self.cutoff_frequency = cutoff_frequency
        self.order = order