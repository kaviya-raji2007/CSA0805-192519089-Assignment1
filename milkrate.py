
from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STANDARD = Decimal("3.5")
SNF_STANDARD = Decimal("8.5")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STEP_SIZE = Decimal("0.1")
CENT = Decimal("0.01")

def rate_per_litre(fat, snf):
    """Return the milk rate per litre."""
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))
    fat_steps = ((fat - FAT_STANDARD) / STEP_SIZE).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    snf_steps = ((snf - SNF_STANDARD) / STEP_SIZE).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    return rate.quantize(CENT, rounding=ROUND_HALF_UP)

def payout(litres, fat, snf):
    """Return the payment rounded to paise."""
    return (Decimal(str(litres)) * rate_per_litre(fat, snf)).quantize(CENT, rounding=ROUND_HALF_UP)

if __name__ == "__main__":
    for litres, fat, snf in [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]:
        rate = rate_per_litre(fat, snf)
        pay = payout(litres, fat, snf)
        print(f"{litres:5} L  fat {fat}  snf {snf}  rate {rate:6.2f}  pay {pay:8.2f}")
