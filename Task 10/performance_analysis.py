
from decimal import Decimal
from time import perf_counter

def float_total(items):
    total = 0.0
    for item in items:
        total += float(item)
    return total

def decimal_total(items):
    total = Decimal("0.00")
    for item in items:
        total += Decimal(item)
    return total

for size in [300, 6000, 150000]:
    payments = ["33.40"] * size

    start = perf_counter()
    f_total = float_total(payments)
    float_time = perf_counter() - start

    start = perf_counter()
    d_total = decimal_total(payments)
    decimal_time = perf_counter() - start

    print("Payments:", size)
    print("Float total:", f_total)
    print("Decimal total:", d_total)
    print("Difference:", Decimal(str(f_total)) - d_total)
    print("Float time:", float_time)
    print("Decimal time:", decimal_time)
    print()
