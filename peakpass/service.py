from .eligibility import validate_request
from .fees import FeeSchedule
from .models import Quote
from .pricing import base_price, discount_amount, weekend_surcharge

def quote_reservation(*, visitor_age: int, resident: bool, activity: str, party_size: int, nights: int = 0, weekend: bool = False, has_adult: bool = True, fee_schedule: FeeSchedule | None = None) -> Quote:
    validate_request(visitor_age=visitor_age, activity=activity, party_size=party_size, nights=nights, has_adult=has_adult)
    fees = fee_schedule or FeeSchedule()
    base = base_price(activity=activity, party_size=party_size, nights=nights)
    surcharge = weekend_surcharge(activity=activity, weekend=weekend, base=base)
    subtotal = base + surcharge
    discount = discount_amount(visitor_age=visitor_age, resident=resident, subtotal=subtotal)
    reservation_fee = fees.reservation_fee(activity)
    total = round(subtotal - discount + reservation_fee, 2)
    return Quote(True, base, surcharge, discount, reservation_fee, total)
