
import math

BASE_RATE = 30.00
FAT_STANDARD = 3.5
SNF_STANDARD = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
STEP_SIZE = 0.1

for fat, snf in [(4.2, 8.7), (3.1, 8.3), (3.5, 8.5)]:
    fat_steps = round((fat - FAT_STANDARD) / STEP_SIZE)
    snf_steps = round((snf - SNF_STANDARD) / STEP_SIZE)

    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * 0.30
    print("Fat steps:", fat_steps)
    print("SNF steps:", snf_steps)
    print("Rate:", round(rate, 2))

print("Unexpected 1:", (4.2 - 3.5) / 0.1)
print("Unexpected 2:", 0.1 + 0.2 == 0.3)
print("Unexpected 3:", -7 // 2)

print("round(-2.5):", round(-2.5))
print("int(-2.5):", int(-2.5))
print("floor(-2.5):", math.floor(-2.5))

fat = 4.2
print("Valid fat:", 2.0 <= fat <= 7.0)
