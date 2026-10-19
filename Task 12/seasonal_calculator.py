
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
STEP_SIZE = Decimal("0.1")
FAT_STANDARD = Decimal("3.5")
SNF_STANDARD = Decimal("8.5")
SNF_STEP_VALUE = Decimal("0.30")
BONUS_THRESHOLD = Decimal("500")
BONUS_RATE = Decimal("0.50")

RATE_CARDS = {
    "normal": {
        "base": Decimal("30.00"),
        "fat_step": Decimal("0.40"),
    },
    "april_june": {
        "base": Decimal("32.00"),
        "fat_step": Decimal("0.45"),
    },
}

def calculate_rate(fat, snf, season="normal"):
    """Calculate the milk rate for the selected season."""
    if season not in RATE_CARDS:
        raise ValueError("Unknown season")

    fat = Decimal(str(fat))
    snf = Decimal(str(snf))
    card = RATE_CARDS[season]

    fat_steps = ((fat - FAT_STANDARD) / STEP_SIZE).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    snf_steps = ((snf - SNF_STANDARD) / STEP_SIZE).quantize(Decimal("1"), rounding=ROUND_HALF_UP)

    rate = card["base"] + fat_steps * card["fat_step"] + snf_steps * SNF_STEP_VALUE
    return rate.quantize(CENT, rounding=ROUND_HALF_UP)

def calculate_ten_day_payment(litres, fat, snf, season="normal"):
    """Calculate payment including the eligible ten-day volume bonus."""
    litres = Decimal(str(litres))
    rate = calculate_rate(fat, snf, season)
    amount = (litres * rate).quantize(CENT, rounding=ROUND_HALF_UP)

    if litres > BONUS_THRESHOLD:
        amount += (litres * BONUS_RATE).quantize(CENT, rounding=ROUND_HALF_UP)

    return rate, amount.quantize(CENT, rounding=ROUND_HALF_UP)

if __name__ == "__main__":
    tests = [
        (100, 3.5, 8.5, "normal"),
        (100, 4.2, 8.7, "april_june"),
        (600, 3.5, 8.5, "normal"),
        (600, 3.5, 8.5, "april_june"),
    ]

    for litres, fat, snf, season in tests:
        rate, amount = calculate_ten_day_payment(litres, fat, snf, season)
        print(f"{season:12} {litres:6} L  rate Rs {rate:6.2f}  payment Rs {amount:9.2f}")
