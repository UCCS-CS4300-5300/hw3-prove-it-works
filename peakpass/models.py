from dataclasses import dataclass

@dataclass(frozen=True)
class Quote:
    eligible: bool
    base_price: float
    surcharge: float
    discount: float
    reservation_fee: float
    total: float
