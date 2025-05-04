from dataclasses import dataclass
from .transfer_function import TransferFunction
from typing import List, Union
from abc import ABC, abstractmethod


@dataclass
class FilterInterface(ABC):
    """A base class for digital filters.

    Args:
        transfer_function : The transfer function of the filter.
    """

    transfer_function: TransferFunction
    sampling_rate: int

    def __init__(
        self,
        enumerator: List[Union[int, float]],
        denominator: List[Union[int, float]],
        sampling_rate: int
    ):
        self.transfer_function = TransferFunction(enumerator, denominator)
        self.sampling_rate = sampling_rate

    @abstractmethod
    def apply_filter(
        self, signal: List[Union[int, float]]
    ) -> List[Union[int, float]]:
        pass
