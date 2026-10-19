
from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STANDARD = Decimal("3.5")
SNF_STANDARD = Decimal("8.5")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STEP_SIZE = Decimal("0.1")
CENT = Decimal("0.01")

def rate_per_litre(fat, snf):
    """Calculate the milk rate per litre."""
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))
    fat_steps = ((fat - FAT_STANDARD) / STEP_SIZE).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    snf_steps = ((snf - SNF_STANDARD) / STEP_SIZE).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    return rate.quantize(CENT, rounding=ROUND_HALF_UP)

def payout(litres, fat, snf):
    """Calculate the payment for a milk entry."""
    amount = Decimal(str(litres)) * rate_per_litre(fat, snf)
    return amount.quantize(CENT, rounding=ROUND_HALF_UP)

def ten_day_total(payments):
    """Return the total of ten-day payments."""
    return sum((Decimal(str(p)).quantize(CENT) for p in payments), Decimal("0.00"))

print("Rate:", rate_per_litre(4.2, 8.7))
print("Payment:", payout(8.5, 4.2, 8.7))
print("Ten-day total:", ten_day_total([300, 283.9, 333.6]))
