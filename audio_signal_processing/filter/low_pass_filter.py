from dataclasses import dataclass
from .domain import Domain
from .filter_interface import FilterInterface


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

    def apply_filter(self, signal, domain=Domain.TIME):
        if domain == Domain.TIME:
            return self._apply_time_domain_filter(signal)
        elif domain == Domain.FREQUENCY:
            return self._apply_frequency_domain_filter(signal)
        else:
            raise ValueError(
                "Invalid domain. Use Domain.TIME or Domain.FREQUENCY."
            )

    def _apply_time_domain_filter(self, signal, alpha):
        output = [0.0]
        for n in range(1, len(signal)):
            output.append((1 - alpha) * signal[n] + alpha * signal[n - 1])
        return signal

    def _apply_frequency_domain_filter(self, signal):
        return signal
