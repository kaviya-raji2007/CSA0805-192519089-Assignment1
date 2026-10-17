
from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STANDARD = Decimal("3.5")
SNF_STANDARD = Decimal("8.5")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STEP_SIZE = Decimal("0.1")
CENT = Decimal("0.01")

def calculate_rate(fat, snf):
    """Calculate the rate with exact decimal arithmetic."""
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))
    fat_steps = ((fat - FAT_STANDARD) / STEP_SIZE).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    snf_steps = ((snf - SNF_STANDARD) / STEP_SIZE).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    return (BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE).quantize(CENT, rounding=ROUND_HALF_UP)

def calculate_payment(litres, fat, snf):
    """Calculate the final farmer payment."""
    return (Decimal(str(litres)) * calculate_rate(fat, snf)).quantize(CENT, rounding=ROUND_HALF_UP)

if __name__ == "__main__":
    test_entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
    total = Decimal("0.00")

    for litres, fat, snf in test_entries:
        amount = calculate_payment(litres, fat, snf)
        total += amount
        print(f"Payment: Rs {amount:.2f}")

    print(f"Total: Rs {total:.2f}")
