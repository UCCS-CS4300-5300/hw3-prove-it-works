# PeakPass Behavioral Specification

PeakPass calculates reservation quotes for a fictional park system. **This specification is the authority for expected behavior.**

## DAY_PASS
- Base price: **$8.00 per person**.
- `nights` must be **0**.
- Reservation fee: **$2.00**.
- Weekend status does not change day-pass pricing.

## CAMPING
- Base price: **$20.00 per night + $3.00 per person per night**.
- Reservations must be **1-7 nights**, inclusive.
- At least one adult must be present (`has_adult=True`).
- Reservation fee: **$5.00**.
- Weekend camping adds a **25% surcharge to the base price** before discounts.

## Request validity
- `visitor_age` must be non-negative.
- `party_size` must be **1-8**, inclusive.
- Unknown activities are invalid.
- Invalid requests raise `ValueError`.

## Discounts
Discounts are calculated from the subtotal after any weekend surcharge.
- Colorado resident: **10%** when `resident=True`.
- Senior: **15%** for visitors age **65 or older**.
- **Discounts do not stack.** If both apply, use only the larger discount.

## Total
`total = base price + surcharge - discount + reservation fee`

Money is rounded to two decimal places where needed.
