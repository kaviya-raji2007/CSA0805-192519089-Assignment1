FAT_STANDARD = 3.5
SNF_STANDARD = 8.5
BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

farmer_id = input("Enter farmer ID: ")
litres = float(input("Enter milk quantity in litres: "))
fat = float(input("Enter fat percentage: "))
snf = float(input("Enter SNF percentage: "))
shift = input("Enter shift (Morning/Evening): ")

print("\nMilk Entry Details")
print("Farmer ID:", farmer_id)
print("Quantity:", litres, "litres")
print("Fat:", fat, "%")
print("SNF:", snf, "%")
print("Shift:", shift)
