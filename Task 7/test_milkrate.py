
from milkrate import rate_per_litre, payout

assert rate_per_litre(3.5, 8.5) == 30
assert payout(10, 3.5, 8.5) == 300
assert rate_per_litre(4.2, 8.7) == 33.40
assert payout(8.5, 4.2, 8.7) == 283.90

print("All module tests passed.")
