from dataclasses import dataclass
from .transfer_function import TransferFunction
from .domain import Domain
from typing import List, Union


@dataclass
class FilterBase:
    """
    A base class for digital filters.

    Attributes
    ----------
    transfer_function : TransferFunction
        The transfer function of the filter.
    """

    transfer_function: TransferFunction

    def __init__(
        self,
        enumerator: List[Union[int, float]],
        denominator: List[Union[int, float]],
    ):
        self.transfer_function = TransferFunction(enumerator, denominator)

    def apply_filter(self, signal: List[Union[int, float]]) -> List[Union[int, float]]:
        """
        Apply the filter to a given signal.

        Parameters
        ----------
        signal : List[Union[int, float]]
            The input signal to be filtered.

        Returns
        -------
        List[Union[int, float]]
            The filtered signal.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")
