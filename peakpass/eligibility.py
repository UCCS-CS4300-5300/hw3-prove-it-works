def validate_request(*, visitor_age: int, activity: str, party_size: int, nights: int, has_adult: bool) -> None:
    if visitor_age < 0:
        raise ValueError("visitor_age must be non-negative")
    if party_size < 1 or party_size > 8:
        raise ValueError("party_size must be between 1 and 8")
    if activity not in {"DAY_PASS", "CAMPING"}:
        raise ValueError("activity must be DAY_PASS or CAMPING")
    if activity == "CAMPING":
        if nights < 1 or nights > 7:
            raise ValueError("camping nights must be between 1 and 7")
        if not has_adult:
            raise ValueError("camping requires at least one adult")
    elif nights != 0:
        raise ValueError("DAY_PASS reservations must use nights=0")
