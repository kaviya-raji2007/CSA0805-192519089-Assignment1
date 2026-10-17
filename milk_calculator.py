
from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STANDARD = Decimal("3.5")
SNF_STANDARD = Decimal("8.5")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STEP_SIZE = Decimal("0.1")
CENT = Decimal("0.01")

def calculate_payment(litres, fat, snf):
    """Validate an entry and calculate its payment."""
    litres = Decimal(str(litres))
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))

    if litres <= 0:
        raise ValueError("Litres must be positive")
    if not Decimal("2.0") <= fat <= Decimal("7.0"):
        raise ValueError("Fat must be between 2.0 and 7.0")
    if snf < 0:
        raise ValueError("SNF cannot be negative")

    fat_steps = ((fat - FAT_STANDARD) / STEP_SIZE).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    snf_steps = ((snf - SNF_STANDARD) / STEP_SIZE).quantize(Decimal("1"), rounding=ROUND_HALF_UP)

    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    rate = rate.quantize(CENT, rounding=ROUND_HALF_UP)
    amount = (litres * rate).quantize(CENT, rounding=ROUND_HALF_UP)
    return rate, amount

entries = []

while True:
    farmer_id = input("Farmer ID (or done): ").strip()
    if farmer_id.lower() == "done":
        break

    try:
        litres = input("Litres: ")
        fat = input("Fat percentage: ")
        snf = input("SNF percentage: ")
        rate, amount = calculate_payment(litres, fat, snf)
        entries.append((farmer_id, rate, amount))
        print(f"Rate: Rs {rate:.2f}, Payment: Rs {amount:.2f}")
    except Exception as error:
        print("Invalid entry:", error)

total = sum((entry[2] for entry in entries), Decimal("0.00"))
print("Accepted entries:", len(entries))
print(f"Ten-day total: Rs {total:.2f}")
