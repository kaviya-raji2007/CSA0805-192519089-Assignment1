
BASE_RATE = 30.00
FAT_STANDARD = 3.5
SNF_STANDARD = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
STEP_SIZE = 0.1
MIN_FAT = 2.0
MAX_FAT = 7.0

farmer_id = "F101"
litres = 10
fat = 4.2
snf = 8.7

print("Base rate:", BASE_RATE)
print("Fat standard:", FAT_STANDARD)
print("SNF standard:", SNF_STANDARD)
print("Farmer ID:", farmer_id)
print("Quantity:", litres)
print("Fat:", fat)
print("SNF:", snf)

a = 10
b = 20
a, b = b, a
print("After swapping:", a, b)

value = 10
print(value, type(value))
value = "ten"
print(value, type(value))
