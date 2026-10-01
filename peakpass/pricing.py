def base_price(*, activity: str, party_size: int, nights: int) -> float:
    if activity == "DAY_PASS":
        return 8.00 * party_size
    return (20.00 * nights) + (3.00 * party_size * nights)

def weekend_surcharge(*, activity: str, weekend: bool, base: float) -> float:
    if activity == "CAMPING" and weekend:
        return round(base * 0.25, 2)
    return 0.0

def discount_amount(*, visitor_age: int, resident: bool, subtotal: float) -> float:
    resident_discount = round(subtotal * 0.10, 2) if resident else 0.0
    senior_discount = round(subtotal * 0.15, 2) if visitor_age > 65 else 0.0
    return round(resident_discount + senior_discount, 2)
