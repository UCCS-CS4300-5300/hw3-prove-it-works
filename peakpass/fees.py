class FeeSchedule:
    def reservation_fee(self, activity: str) -> float:
        if activity == "DAY_PASS":
            return 2.00
        if activity == "CAMPING":
            return 5.00
        raise ValueError(f"Unknown activity: {activity}")
