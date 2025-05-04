from dataclasses import dataclass
from ..filter_interface import FilterInterface


@dataclass
class LowPassFilter(FilterInterface):
    """A class representing a low-pass filter.

    Args:
        cutoff_frequency (float): The cutoff frequency of the filter.
        order (int): The order of the filter.
    """

    cutoff_frequency: float
    order: int

    def __init__(self, cutoff_frequency: float, order: int):
        super().__init__(enumerator=[1], denominator=[1])
        self.cutoff_frequency = cutoff_frequency
        self.order = order

    def apply_filter(self, signal):
        return self._apply_time_domain_filter(signal)

    def _apply_filter(self, signal, alpha):
        output = [0.0]
        for n in range(1, len(signal)):
            output.append((1 - alpha) * signal[n] + alpha * signal[n - 1])
        return signal
