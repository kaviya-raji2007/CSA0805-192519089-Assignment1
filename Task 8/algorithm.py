
def calculate_payment(litres, fat, snf):
    """Calculate payment using the milk rate formula."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    rate = 30.00 + fat_steps * 0.40 + snf_steps * 0.30
    return round(rate, 2), round(litres * rate, 2)

entries = [
    (10, 3.5, 8.5),
    (8.5, 4.2, 8.7),
    (12, 3.1, 8.3)
]

total = 0.0

for litres, fat, snf in entries:
    rate, amount = calculate_payment(litres, fat, snf)
    total += amount
    print(f"Rate: {rate:.2f}, Payment: {amount:.2f}")

print(f"Ten-day total: {total:.2f}")
