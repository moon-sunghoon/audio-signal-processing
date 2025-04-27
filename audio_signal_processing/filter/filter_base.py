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
    domain_type : Domain
        The domain type of the filter (time or frequency)
    """

    transfer_function: TransferFunction
    domain_type: Domain = Domain.FREQUENCY

    def __init__(
        self,
        enumerator: List[Union[int, float]],
        denominator: List[Union[int, float]],
        domain_type=Domain.FREQUENCY
    ):
        self.transfer_function = TransferFunction(enumerator, denominator)
        self.domain_type = domain_type
