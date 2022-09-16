# https://sobolevn.me/2019/03/enforcing-srp

from typing_extensions import final
from attr import dataclass

@final
@dataclass(frozen=True, slots=True)
class CalculatePrice(object):
    def __init__(self, callback: Callable[[Decimal], Decimal]) -> None:
        self._callback = callback

    def __call__(self, products: List[Product]) -> Decimal:
        price = 0
        for product in products:
            price += product.price
        return self._callback(price)
