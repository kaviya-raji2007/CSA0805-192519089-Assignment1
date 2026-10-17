
from decimal import Decimal

print(type(10))
print(type(10.0))
print(type("10"))
print(type(True))
print(type([10, 8.5]))

print("7 / 2 =", 7 / 2)
print("7 // 2 =", 7 // 2)
print("7 % 2 =", 7 % 2)
print("-7 // 2 =", -7 // 2)

print("Float comparison:", 0.1 + 0.2 == 0.3)
print("Decimal comparison:",
      Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))

payments = ["33.40"] * 1000 + ["0.10"] * 3

def total_decimal(items):
    total = Decimal("0.00")
    for amount in items:
        total += Decimal(amount)
    return total

print("Decimal total:", total_decimal(payments))
