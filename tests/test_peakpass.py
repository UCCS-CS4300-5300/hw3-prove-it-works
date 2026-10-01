import pytest
from peakpass import quote_reservation

class StubFees:
    def __init__(self, amount): self.amount = amount
    def reservation_fee(self, activity): return self.amount

def test_basic_day_pass():
    q=quote_reservation(visitor_age=30,resident=False,activity="DAY_PASS",party_size=2)
    assert q.total == 18.00

def test_basic_camping():
    q=quote_reservation(visitor_age=30,resident=False,activity="CAMPING",party_size=2,nights=2)
    assert q.total == 57.00

def test_weekend_camping_costs_more():
    q=quote_reservation(visitor_age=30,resident=False,activity="CAMPING",party_size=2,nights=2,weekend=True)
    assert q.total > q.base_price

def test_resident_gets_discount():
    q=quote_reservation(visitor_age=30,resident=True,activity="DAY_PASS",party_size=4)
    assert q.discount > 0

def test_senior_gets_discount():
    q=quote_reservation(visitor_age=70,resident=False,activity="DAY_PASS",party_size=2)
    assert q.discount > 0

def test_resident_senior_gets_discount():
    q=quote_reservation(visitor_age=70,resident=True,activity="DAY_PASS",party_size=2)
    assert q.discount > 0

def test_party_size_too_small_rejected():
    with pytest.raises(ValueError): quote_reservation(visitor_age=30,resident=False,activity="DAY_PASS",party_size=0)

def test_party_size_too_large_rejected():
    with pytest.raises(ValueError): quote_reservation(visitor_age=30,resident=False,activity="DAY_PASS",party_size=9)

def test_camping_requires_adult():
    with pytest.raises(ValueError): quote_reservation(visitor_age=17,resident=False,activity="CAMPING",party_size=2,nights=1,has_adult=False)

def test_fee_schedule_can_be_replaced():
    q=quote_reservation(visitor_age=30,resident=False,activity="DAY_PASS",party_size=1,fee_schedule=StubFees(9.0))
    assert q.reservation_fee == 9.0
